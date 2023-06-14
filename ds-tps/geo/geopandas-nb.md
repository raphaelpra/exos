---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Un peu de geopandas

+++

comme son nom l'indique, geopandas <https://geopandas.org/en/stable/> est une librairie pour faire .. un peu de géo

pour faire court, elle permet de manipuler un dataframe avec des coordonnées géographiques

+++ {"tags": ["framed_cell"]}

## géolocalisation

pour obtenir des coordonnées latitude/longitude à partir d'une adresse, en France on peut utiliser un service public et gratuit ici

<https://adresse.data.gouv.fr/api-doc/adresse>

lisez bien cette page, et notamment tout en bas il y a une zone où vous pouvez faire une recherche en ligne

```{code-cell}
# for starters, we only need the 'regular fit' pandas

import pandas as pd
```

vous pouvez charger le fichier `addresses.csv`; toutes ces adresses sont situées à PARIS

```{code-cell}
# load the data in addresses.csv

# your code here
```

et la première chose qu'on va faire, c'est naturellement d'utiliser cette API pour géolocaliser ces adresses

mais avant cela, je vous recommande de produire un fichier `addresses-small.csv` qui contient un petit extrait, disons les 10 ou 20 premières lignes; ce sera très utile pour débugger

```{code-cell}
# produce a small extract into addresses-small.csv

# your code here
```

### une par une

+++

c'est très pratique de pouvoir faire une recherche 'un par un'; voici comment ça se présenterait

```{code-cell}
# requests is the swiss knife for doing http
import requests

def localize_one(num, typ, nom):

    # we build the URL which directly contains the address pieces
    url = f"https://api-adresse.data.gouv.fr/search/?q={num}+{typ}+{nom},Paris&limit=1"
    print(f"localize_one is fetching page\n{url}")
    
    # sending request to the web server
    response = requests.get(url)

    # if all is OK, http returns a code in the [200 .. 300[ range
    if not (200 <= response.status_code < 300):
        print("WHOOPS....")

    # we can then read the answer - remember it's a JSON string
    # so we can decode it on the fly
    return response.json()
```

```{code-cell}
# and here is how we could use it

localize_one(18, 'rue', 'BERNARDINS')
```

````{admonition} ***MAIS***
on ne va pas faire comme ça... pourquoi d'après vous ?

```{hint}
* mesurez combien de temps ça a pris de résoudre cette adresse
    * pour cela vous pouvez utiliser la *magic* `%%timeit`
    * ou encore le module `time`, sachant que `time.time()` compte des secondes
* combien de temps il faudrait pour faire ça 30.000 fois ?
* pourquoi est-ce que c'est aussi lent de faire comme ça ?
```
````

+++

```{attention}
pour vous faire réfléchir, il se passerait quoi si par exemple dans la colonne `name` il y avait un caractère `&`
```

+++

### en un seul coup

si vous avez bien lu la page qui décrit l'API, vous devez avoir remarqué qu'il y a une autre façon de lui soumettre une recherche

c'est ce qui est indiqué ici:
```
curl -X POST -F data=@path/to/file.csv -F columns=voie -F columns=ville https://api-adresse.data.gouv.fr/search/csv/
```

+++

***mais comment ça se lit ce bidule ?***

* `curl` est un programme qu'on peut utiliser directement dans le terminal pour faire des requêtes http
* dans son utilisation la plus simple, il permet par exemple d'aller chercher une page web: vous copiez l'URL depuis le navigateur, et vous la donnez à `curl`, qui peut ranger la page dans un fichier

  ```bash
  curl -o lapageweb.html http://github.com/flotpython/
  ```
* quand on utilise une API, comme on vient de le faire pour aller chercher la position de la rue des bernardins, on doit **passer des paramètres** à l'API; pour faire ça dans une requête http, il y a deux mécanismes: GET et POST

+++ {"tags": ["framed_cell"]}

#### GET

**`GET`**: c'est le comportement par défaut de `curl`; dans ce mode de fonctionnement les paramètres sont passés **directement dans l'URL** comme on l'a fait tout à l'heure quand on a vu ceci
```console
localize_one is fetching page
https://api-adresse.data.gouv.fr/search/?q=18+rue+BERNARDINS,Paris&limit=1
```

et ici d'ailleurs, pour information, la syntaxe générale c'est 
```
http://le.host.name/le/path?param1=truc&param2=bidule&param3=machinechose
```
et donc on a défini deux paramètres, `q` (for *query*) et `limit` (pour avoir seulement la première réponse)

+++ {"tags": ["framed_cell"]}

#### POST

**`POST`**: dans ce mode-là, on ne passe plus les paramètres dans l'URL, mais dans le header http; bon je sais ça ne vous parle pas forcément, et ce n'est pas hyper important de savoir exactement ce que ça signifie, mais le point important c'est qu'on ne va plus passer les paramètres de la même façon

et donc pour revenir à notre phrase:

```
curl -X POST -F data=@path/to/file.csv -F columns=voie -F columns=ville https://api-adresse.data.gouv.fr/search/csv/
```

ce qui se passe ici, c'est qu'on utilise `curl` pour envoyer une requête `POST` avec des paramètres `data` et `columns`; le bon sens nous dit que

* `data` désigne le nom d'un fichier csv qui contient les données à géolocaliser, une par ligne
* `columns` désigne les noms des colonnes qui contiennent l'adresse

+++

#### en Python

sauf que nous, on ne veut pas utiliser `curl`, on veut faire cette requête en Python; voici comment on va s'y prendre

+++

1. en une seule requête à l'API, on va envoyer **tout le fichier** csv, en lui indiquant juste quelles sont les colonnes qui contiennent les morceaux de l'adresse
2. le résultat - toujours au format csv - peut être également transformé en dataframe
3. qu'il ne restera plus qu'à `merge` (ou `join` si vous préférez) avec la dataframe de départ, pour ajouter les résultats de la géolocalisation dans les données de départ
   pour cette étape on peut envisager de ne garder que certaines colonnes de la géolocalisation (assez bavarde par ailleurs), je vous recommande de conserver uniquement:
   * `latitude`, `longitude` - *of course*
   * `result_city` pour pouvoir vérifier la validité des résultats - ici on devrait toujours avoir `Paris`
   * `result_type` qui devrait toujours renvoyer `housenumber`, ça permet à nouveau de vérifier qu'on a bien une adresse connue

+++

````{tip}
* pour envoyer un POST avec des paramètres, on peut faire
  ```python
  response = requests.post(url, file=some_dict, data=another_dict)
  ```
* et donc dans notre cas, puisque `data` est un paramètre de type fichier, alors que `columns` est un paramètre usuel, on fera
  ```python
  response = requests.post(url, file={'data': filename}, data={'columns': ['col1', ...]})
  ```
* enfin, `pd.read_csv` s'attend à un paramètre de type fchier, i.e. du genre de ce qu'on obtient avec `open()`  
  et du coup pour reconstruire une dataframe à partir du texte obtenu dans la requête http, on a deux choix
  1. soit on commence par sauver le texte dans un fichier temporaire (juste faire attention à choisir un nom de fichier qui n'existe pas, de préférence dans un dossier temporaire, voir le module `tempfile`)
  1. soit on triche un peu, et grâce à `io.StringIO` on peut transformer une chaine en fichier !
  
  c'est ce qu'on va faire dans notre solution, mais la première option est tout à fait raisonnable aussi 
````

+++

je vous recommande d'y aller pas à pas, commencez par juste l'étape 1, puis 1 et 2, et enfin de 1 à 3

c'est utile aussi de commencer par une toute petite dataframe pour ne pas attendre des heures pendant la mise au point...

```{code-cell}
# your code here

def search_and_join(filename, col_number, col_type, col_name, col_city):
    """
    calls the https://api-adresse.data.gouv.fr API
    and returns an augmented dataframe with 4 new columns
    latitude, longitude, result_city and result_type

    Parameters:
      filename:
        the name of the input csv file
      col_number:
      col_type:
      col_name:
      col_city:
        you must provide the names of the 4 columns where to find
        street number, street type, street name and city name
        to be used for geolocating
    """
    
    pass
```

```{code-cell}
# try your code on the small sample for starters

# geoloc_small = search_and_join("addresses-small.csv", "number", "type", "name", "city")
# geoloc_small
```

```{code-cell}
# sanity check : make sure that all the entries have 
# result_city == 'Paris'
# and
# result_type == 'housenumber'

# your code
```

```{code-cell}
# when you think you're ready, go full scale
# be ready to wait for at least 40-60s 

# geoloc = search_and_join("addresses.csv", "number", "type", "name", "city")
```

```{code-cell}
# sanity check 

# len(geoloc)
```

```{code-cell}
# at this point you should store the data
# it's just good practice, as you've done one important step of the process

# store geoloc in addresses-geoloc.csv

# your code
```

## afficher sur une carte

+++

à présent qu'on a une position, on va pouvoir afficher ces adresses sur une carte

et pour ça il y a plein de libs disponibles, on va choisir `folium`

si nécessaire, il faut l'installer (comment on fait déjà ?)

```{code-cell}
import folium
```

pour commencer, allez chercher la documentation; le plus simple c'est de demander à google `folium python`

Question subsidiaire: comment j'ai fait d'après vous pour [embarquer cette recherche dans un lien hypertexte](https://www.google.com/search?q=folium+python) ?

et surtout (regardez les deux premiers pour l'instant):

* l'objet `Map` <https://python-visualization.github.io/folium/quickstart.html#Getting-Started>
* l'objet `Marker` <https://python-visualization.github.io/folium/quickstart.html#Markers>
* et un peu plus tard on utilisera aussi des overlays <https://python-visualization.github.io/folium/quickstart.html#GeoJSON/TopoJSON-Overlays>

```{code-cell}
# ~ chatelet 

CENTER = 48.856542, 2.347614
```

### le fond de carte

```{code-cell}
# pour commencer on va recharger la dataframe précédente
import pandas as pd

geoloc = pd.read_csv("addresses-geoloc.csv")

# et en faire un petit échantillon

geoloc_small = geoloc.sample(n=20)
```

```{code-cell}
# créez une map centrée sur ce point et de zoom 13
# n'oubliez pas de l'afficher,
# et vérifiez que voyez bien Paris, 
# que vous pouvez zoomer et vous déplacer, ...

# votre code
def paris_map():
    ...

# pour l'afficher
paris_map()
```

### on ajoute les adresses

```{code-cell}
:tags: [framed_cell]

# pareil mais vous ajoutez les adresses
# éventuellement vous pouvez comme sur l'exemple ajouter un tooltip avec l'adresse complète

# faites bien attention à prendre une PETITE dataframe
# car avec cette méthode si on essaie d'afficher les 
# dizaines de milliers d'adresses ça va ramer big time !

# votre code
# def map_addresses(geoloc_small):
#    pass
```

```{code-cell}
# et essayez-le

map_addresses(geoloc_small)
```

### on sauve la carte

une fonction très sympatique de `folium`, c'est qu'on peut sauver cette carte sous la forme d'un fichier html, on dit *standalone*, c'est-à-dire autosuffisant, pas besoin de Python ni de Jupyter pour la regarder

```{code-cell}
map_small = map_addresses(geoloc_small)
map_small.save("map-small.html")
```

et maintenant pour voir le résultat, ouvrez le fichier dans un autre tab du navigateur

+++

## les quartiers de Paris

maintenant on va ranger les adresses par quartier; pour cela nous avons le fichier `quartiers_paris.shp` (en fait avec son compagnon `quartiers_paris.shx`, les deux sont nécessaires) qui contient la définition de 80 quartiers qui recouvrent Paris intra-muros

ça se présente comme ceci:

```{code-cell}
# à ce stade on a besoin de geopandas
# installez-le si besoin

import geopandas as gpd
```

```{code-cell}
# ça se lit facilement
quartiers = gpd.read_file("quartiers_paris.shp")

# et le résultat est .. une dataframe
type(quartiers)
```

```{code-cell}
# qu'on peut afficher normalement

quartiers.head(2)
```

```{code-cell}
# et on peut même l'afficher sommairement avec matplotlib

# bon c'est loin d'être parfait mais ça nous suffit à ce stade
# on va voir plus loin comment incorporer ça dans la carte

quartiers.plot();
```

pour afficher cela sur la carte, il faut se livrer à une petite gymnastique

1. on construit la map comme on l'a vu jusqu'ici
2. on transforme la geo-dataframe (`quartiers`) en JSON
3. que l'on peut passer alors à `folium.GeoJson()` pour créer un objet
4. qu'on ajoute dans la map

ce qui nous donne ceci:

```{code-cell}
def map_addresses_in_quartiers_1(geoloc):
    # create a new map object containing a few points
    map = map_addresses(geoloc)

    # translate the geo-dtaframe into a JSON string
    quartiers_json = quartiers.to_json()

    # create a folium JSON object from that
    folium.GeoJson(data=quartiers_json,
                   # optionnally we can tweak things on the way
                   # try to uncomment these
                   # style_function=lambda x: {"fillColor": "orange"}
                   # they have no name
                   # tooltip="Hey !",
            # and add it to the map
            ).add_to(map)

    # and that's it
    return map
```

```{code-cell}
map_addresses_in_quartiers_1(geoloc_small)
```

```{code-cell}

```
