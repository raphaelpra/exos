---
jupytext:
  cell_metadata_filter: all, -hidden, -heading_collapsed, -run_control, -trusted
  encoding: '# -*- coding: utf-8 -*-'
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,
    -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
    -language_info.file_extension, -language_info.mimetype, -toc
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
nbhosting:
  show_up_down_buttons: true
  title: exo marathon
---

# outils

```{code-cell} ipython3
import pandas as pd
```

on utilise ici un utilitaire pour regarder le début d'un fichier texte

```{code-cell} ipython3
# sur les plateformes Unix on peut faire simplement
# 
# ! head -5 data/marathon.txt
#
# mais sur Windows ça ne fonctionne pas, alors...

from head import head

help(head)
```

# TP: une dataframe simple

+++

On va étudier un jeu de données trouvé sur Internet

```{code-cell} ipython3
URL = "http://www.xavierdupre.fr/enseignement/complements/marathon.txt"
```

## chargement

+++

Le premier réflexe pour charger un fichier de ce genre, c'est d'utiliser la fonction `read_csv` de pandas

```{code-cell} ipython3
# votre cellule de code
# qu'on va faire descendre
# et raffiner au fur et à mesure

df0 = pd.read_csv(URL)
df0.head()
```

c'est un début, mais ça ne marche pas franchement bien !

+++

il faut donc bien regarder la doc

```{code-cell} ipython3
# pd.read_csv?
```

et pour commencer je vous invite à préciser le séparateur:

```{code-cell} ipython3
# à vous de modifier cette première approche

df1 = pd.read_csv(URL)
```

```{code-cell} ipython3
:hide_input: false

# prune-cell

df1 = pd.read_csv(URL, sep='\t')
```

```{code-cell} ipython3
# pour vérifier, ceci doit afficher True
df1.shape == (358, 4) and df1.iloc[0, 0] == 'PARIS' and df1.columns[0] == 'PARIS'
```

c'est mieux, mais les noms des colonnes ne sont pas corrects

en effet par défaut, `read_csv` utilise la première ligne pour déterminer les noms des colonnes

or dans le fichier texte il n'y a pas le nom des colonnes !

```{code-cell} ipython3
head("data/marathon.txt", 5)
```

du coup ce serait pertinent de donner un nom aux colonnes

```{code-cell} ipython3
NAMES = ["city", "year", "duration", "seconds"]
```

```{code-cell} ipython3
# à vous de créer une donnée bien propre
df = pd.read_csv(URL)
```

```{code-cell} ipython3
:hide_input: false

# prune-cell
# si en plus on précise le nom des colonnes 
# ça commence à être franchement mieux

df = pd.read_csv(URL, sep="\t", names=NAMES)
```

```{code-cell} ipython3
# pour vérifier, ceci doit afficher True
df.shape == (359, 4) and df.iloc[0, 0] == 'PARIS' and df.columns[0] == 'city'
```

```{code-cell} ipython3
# ce qui maintenant nous donne ceci
df.head(2)
```

## sauvegarde dans un fichier csv

+++

dans l'autre sens quand on a produit une dataframe et qu'on veut sauver le résultat dans un fichier texte

```{code-cell} ipython3
# df.to_csv?
```

par exemple je crée ici un fichier qu'on peut relire sous excel

```{code-cell} ipython3
:hide_input: false

loop = "marathon-loop.csv"
df.to_csv(loop, sep=";", index=False)
```

```{code-cell} ipython3
# pour voir un aperçu
head(loop, 4)
```

## des recherches

+++

### les éditions de 1971

```{code-cell} ipython3
# à vous de calculer les éditions de 1971
df_1971 = ...
```

```{code-cell} ipython3
:hide_input: false

# prune-cell
df_1971 = df[df.year == 1971]
```

```{code-cell} ipython3
# ceci doit retourner True
df_1971.shape == (3, 4) and df_1971.seconds.max() == 8574
```

+++ {"tags": ["level_basic"]}

### l'édition de 1981 à Londres

```{code-cell} ipython3
# à vous
df_london_1981 = ...
```

```{code-cell} ipython3
:hide_input: false

# prune-cell
df_london_1981 = df[(df.city == 'LONDON') & (df.year == 1981)]
```

```{code-cell} ipython3
# ceci doit retourner True
df_london_1981.shape == (1, 4) and df_london_1981.iloc[0].seconds == 7908
```

### trouver toutes les villes

+++

on veut construire une collection de toutes les villes qui apparaissent au moins une fois

```{code-cell} ipython3
# à vous

cities = ...
```

```{code-cell} ipython3
:hide_input: false

# prune-cell
cities = df.city.unique()
cities
```

```{code-cell} ipython3
# intéressez-vous au type du résultat

# la version la plus naïve retourne un ndarray
import numpy as np

isinstance(cities, np.ndarray)
```

## des extraits

```{code-cell} ipython3
# attention mes numéros de ligne commencent à 1
head("data/marathon.txt", 12)
```

### extrait #1

+++ {"tags": ["level_basic"]}

les entrées correspondant aux lignes 10 à 12 inclusivement

```{code-cell} ipython3
# à vous
df_10_to_12 = ...
```

```{code-cell} ipython3
:hide_input: false

# prune-cell
df_10_to_12 = df.iloc[9:12]
df_10_to_12
```

```{code-cell} ipython3
# ceci doit retourner True
df_10_to_12.shape == (3, 4) and df_10_to_12.iloc[0].year == 2002 and df_10_to_12.iloc[-1].year == 2000
```

### extrait #2

+++ {"tags": ["level_basic"]}

une Series correspondant aux événements à Paris après 2000 (inclus), 
dans laquelle on n'a gardé que l'année

```{code-cell} ipython3
# à vous
s_paris_2000 = ...
```

```{code-cell} ipython3
:hide_input: false

# prune-cell

# pour bien décortiquer, en deux temps

df_paris_2000 = df[(df.city == 'PARIS') & (df.year >= 2000)]

# plusieurs possibilités
#paris_2000['year']
#paris_2000.loc[:, 'year']
# le plus simple ici est le mieux
s_paris_2000 = df_paris_2000.year
```

```{code-cell} ipython3
s_paris_2000
```

```{code-cell} ipython3
# ceci doit retourner True
isinstance(s_paris_2000, pd.Series) and len(s_paris_2000) == 12 and s_paris_2000.iloc[-1] == 2000
```

### extrait #3

+++ {"tags": ["level_basic"]}

une DataFrame correspondant aux événements à Paris après 2000, 
dans laquelle on n'a gardé que les deux colonnes `year` et `seconds`

```{code-cell} ipython3
df_paris_2000_ys = ...
```

```{code-cell} ipython3
:hide_input: false

# prune-cell

# on peut repartir de paris_2000
df_paris_2000_ys = df_paris_2000[['year', 'seconds']]
```

```{code-cell} ipython3
# ceci doit retourner True
(isinstance(df_paris_2000_ys, pd.DataFrame)
 and df_paris_2000_ys.shape == (12, 2) 
 and df_paris_2000_ys.iloc[-2].seconds == 7780)
```

+++ {"hide_input": true}

## aggrégats

+++

### moyenne

+++ {"tags": ["level_basic"]}

ce serait quoi la moyenne de la colonne `seconds` ?

```{code-cell} ipython3
# calculer la moyenne de la colonne 'seconds'

seconds_average = ...
```

```{code-cell} ipython3
:cell_style: center
:hide_input: false

# prune-cell

# more on this later

seconds_average = df.seconds.mean()
```

```{code-cell} ipython3
# pour vérifier
import math
math.isclose(seconds_average, 7933.660167130919)
```

****

```{code-cell} ipython3
# en guise de révision de Python, transformez cette valeur en chaine
# au format 2h 12' 13''

formatted_average = ...
```

```{code-cell} ipython3
:cell_style: center
:hide_input: false

# prune-cell

hours = int(seconds_average // 3600)
minutes = int(seconds_average % 3600 // 60)
seconds = int(seconds_average % 60)

formatted_average = f"{hours}h {minutes}' {seconds}''"
```

```{code-cell} ipython3
# pour vérifier
formatted_average == "2h 12' 13''"
```

### combien de marathons par an

+++ {"hide_input": false, "tags": ["level_basic"]}

si maintenant je veux produire une série qui compte par année combien il y a eu de marathons

```{code-cell} ipython3

```

```{code-cell} ipython3
# à vous

count_by_year = ...
```

```{code-cell} ipython3
# prune-cell

# toutes les colonnes vont contenir les mêmes infos, on peut en prendre une au hasard
count_by_year = df.groupby(by='year').count().city

# il y a plein de variantes, on peut inverser le count() et le city
# on peut appeler .agg('count')
# ...
```

```{code-cell} ipython3
# pour vérifier
(isinstance(count_by_year, pd.Series)
 and len(count_by_year) == 65
 and count_by_year.loc[1947] == 1
 and count_by_year.loc[2007] == 9
 and count_by_year.loc[2011] == 5)
```

## les durées

+++

### `read_csv(parse_dates=)`

+++

dans `read_csv` il y a une option `parse_dates`; mais regardez ce que ça donne

```{code-cell} ipython3
df_broken = pd.read_csv(URL, sep='\t', 
                        names=['city', 'year', 'duration', 'seconds'], 
                        parse_dates=['duration'])
df_broken
```

**ça ne va pas !**

le truc c'est que ici, on n'a **pas une date** mais c'est une **durée**

```{code-cell} ipython3
# repartons des données de départ

df.dtypes
```

non, pour fabriquer un objet `datetime64` on va utiliser `pd.to_timedelta`

```{code-cell} ipython3
df.duration = pd.to_timedelta(df.duration)
```

```{code-cell} ipython3
df.head(5)
```

```{code-cell} ipython3
# et cette fois-ci
df.dtypes
```

### duration == seconds ?

+++

on va simplement vérifier que la colonne `seconds` correspond bien à ce qu'on croit

```{code-cell} ipython3
total_seconds = df.duration.dt.total_seconds()
```

```{code-cell} ipython3
# ça matche presque
total_seconds.head(5), df.seconds.head(5)
```

```{code-cell} ipython3
# mais on ne peut pas faire juste == à cause des types
(df.duration.dt.total_seconds() == df.seconds).head(5)
```

***
***
***

+++

**DIGRESSION**

+++

ce qui d'ailleurs est particulièrement bizarre car on peut en général comparer deux types distincts et ça fonctionne

```{code-cell} ipython3
import numpy as np

# ----
df1 = pd.DataFrame([{'a': 1}, {'a': 2}])
df2 = pd.DataFrame({'a': df1.a.astype(np.float64)})

df1.dtypes, df2.dtypes
```

```{code-cell} ipython3
df1 == df2
```

**FIN DIGRESSION**

+++

***
***
***

+++

**MAIS REPRENONS**

+++

comme souvent dans ces cas-là le réflexe est d'utiliser isclose

```{code-cell} ipython3
import numpy as np
np.isclose(df.duration.dt.total_seconds(), df.seconds)
```

```{code-cell} ipython3
# du coup comment feriez-vous pour vérifier
# l'égalité sur toute la dataframe

# ...
```

```{code-cell} ipython3
# prune-cell
np.all(np.isclose(df.duration.dt.total_seconds(), df.seconds))
```

****
