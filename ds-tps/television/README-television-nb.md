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
  title: exo nettoyage
---

# television (nettoyage)

+++

pour réaliser ce TP localement sur votre ordi, {download}`commencez par télécharger le zip<./ARTEFACTS-television.zip>`

+++

cet exercice est originellement proposé ici:

<http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/notebooks/td1a_cenonce_session_10.html#exercice-1-creer-un-fichier-excel>

+++

## imports

```{code-cell} ipython3
import numpy as np
import pandas as pd
```

```{code-cell} ipython3
# juste un utilitaire pour regarder le début d'un fichier

def head(filename, nb_lines=5):
    with open(filename) as f:
        for lineno, line in enumerate(f, 1):
            print(f"{lineno:02d}", line, end="")
            if lineno >= nb_lines:
                break
```

## la source

+++

l'idée est de se mettre en vraie situation; les données qu'on trouve ici ou là sont souvent très sales !

```{code-cell} ipython3
# de prime abord ça a l'air pas trop mal

# NOTE: si vous n'avez pas le module head, ouvrez le fichier dans votre éditeur favori

head("data/television.txt", 10)
```

```{code-cell} ipython3
# sauf que si on le charge: ouh là !

df = pd.read_csv("data/television.txt", sep="\t")
df
```

```{code-cell} ipython3
# et en particulier, ceci n'est pas du tout ce qu'on veut

df.shape
```

## survol de ce qu'il faut faire

le TP comporte plusieurs étapes

1. enlever les colonnes pleines de vide; pour fixer les idées, nous nettoyons **les colonnes qui contiennent seulement des n/a ou des 0**
 
   dans le corrigé on va voir deux méthodes
  * rapide
  * manuelle: comment on ferait si le nettoyage devait être fait sur un critère plus spécifique; on verra comment faire sur la base d'une fonction qui, pour une colonne, indique si elle doit être gardée ou pas

1. calculer les valeurs uniques de la colonne `cLT2FREQ`; le texte de l'exercice suggère qu'on doit trouver une poignée de valeurs

1. à ce stade, combien de lignes ont leur `cLT2FREQ` non renseignée ?  
  combien doit-on avoir de lignes si on nettoie sur cette base ?  
  (i.e. si on enlève toutes les lignes qui n'ont pas cette colonne renseignée)
  faites ce nettoyage et vérifiez votre résultat

1. sauver le résultat dans un fichier excel

toujours pour fixer les idées, on doit trouver à la fin une dataframe qui a une forme de `(7386, 4)`

+++

### indices

je vous signale des fonctions utiles dans tout le TP:

```{code-cell} ipython3
# df.dropna?
# df.drop?

# pd.Series.unique?

# df.to_excel?
# !pip install openpyxl
```

---

+++

## colonnes vides

+++

la première étape donc, consiste à supprimer les colonnes vides

```{code-cell} ipython3
# on recharge pour être sûr
df = pd.read_csv("data/television.txt", sep="\t")
df.shape
```

### la méthode rapide

+++ {"tags": ["level_basic"]}

le mieux c'est d'utiliser `dropna`

```{code-cell} ipython3
# pour voir la doc
# df.dropna?
```

```{code-cell} ipython3
# à vous
...
```

```{code-cell} ipython3
# ceci doit afficher True
df.shape == (8403, 4)
```

```{code-cell} ipython3
df.head()
```

### la méthode pédestre

+++

dans ce cas précis, `dropna` est le mieux bien sûr

maintenant, dans certains cas le critère pour 'oublier' des colonnes peut être moins simple - imaginez par exemple qu'on veuille supprimer toutes les colonnes qui contiennent un certain pourcentage de valeurs parmi `GARBAGE` et `TRASH` et un vrai n/a...

donc voyons comment on peut faire le même nettoyage, mais de manière plus fine

```{code-cell} ipython3
# on recharge pour être sûr
df = pd.read_csv("data/television.txt", sep="\t")
```

+++ {"tags": ["level_basic"]}

en deux étapes:

d'abord comment feriez-vous, étant donné le nom d'une colonne, pour savoir si elle est pleine de vide ?

```{code-cell} ipython3
# à vous 
def is_empty_column(df, colname):
    ...
```

```{code-cell} ipython3
:cell_style: split

# ceci doit afficher True

# on teste
col1 = 'POIDLOG'
not is_empty_column(df, col1)
```

```{code-cell} ipython3
:cell_style: split

# ceci doit afficher True

col5 = 'Unnamed: 4'
is_empty_column(df, col5)
```

+++ {"hide_input": true, "tags": ["level_basic"]}

ensuite il ne reste qu'à calculer la liste des colonnes vides, pour la passer à `df.drop()`

```{code-cell} ipython3
# à vous

# calculez la liste des colonnes vides
empty_columns = ...

# puis utilisez df.drop
```

```{code-cell} ipython3
# ceci doit afficher True
df.shape == (8403, 4)
```

Bien sûr on a découpé le problème en deux mais en fait ça peut se récrire en une seule ligne

```{code-cell} ipython3
# en option

# à vous

# récrire tout ceci en une seule passe
```

```{code-cell} ipython3
# ceci doit afficher True
df.shape == (8403, 4)
```

## obtenir les valeurs distinctes

+++

comment obtenir les valeurs distinctes de la colonne `cLT2FREQ`

+++

le texte de l'exercice initial nous apprend qu'on ne devrait avoir que 3 valeurs; 
et une inspection visuelle rapide vous le confirme, plus la présence de pas mal de vide dans cette colonne

+++ {"tags": ["level_basic"]}

la méthode la plus simple consiste à utiliser [`Series.unique`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.unique.html) qui renvoie le résultat sous la forme d'un `numpy.ndarray`

```{code-cell} ipython3
# à vous
uniques = ...
```

```{code-cell} ipython3
uniques
```

```{code-cell} ipython3
:tags: [raises-exception]

# ceci doit afficher True
uniques.sort()
np.all(uniques[:-1] == np.arange(1, 4)) and np.isnan(uniques[-1])
```

```{code-cell} ipython3
:tags: [level_basic, raises-exception]

# point de réflexion : pourquoi ceci ne renvoie-t-il pas True ?
uniques.sort()
np.all(uniques == np.array([1., 2., 3., np.nan]))
```

## compter les lignes à nettoyer

+++ {"tags": ["level_basic"]}

on veut maintenant nettoyer les données en enlevant les lignes qui n'ont pas la colonne `cLT2FREQ` renseignée

dans un premier temps on vous demande de calculer le nombre de lignes concernées

```{code-cell} ipython3
# à vous
nb_lines_to_clean = ...
```

```{code-cell} ipython3
:tags: [raises-exception]

# ceci doit afficher True

nb_lines_to_clean == 1017
```

```{code-cell} ipython3
# ce qui signifie qu'à la fin on doit avoir ce nombre de lignes
8403-1017
```

```{code-cell} ipython3
:tags: [raises-exception]

# ou encore, plus proprement
expected_lines = len(df) - nb_lines_to_clean
expected_lines
```

## nettoyage des lignes

+++

### option 1: `df.drop()`

```{code-cell} ipython3
:hide_input: false

# on recharge à tout hasard
df = pd.read_csv("data/television.txt", sep="\t").dropna(axis='columns', how='all')
print(df.shape)
```

remarquez que `df.drop` prend un paramètre optionnel `inplace` qui peut être souvent utile

```{code-cell} ipython3
#df.drop?
```

+++ {"tags": ["level_basic"]}

option 1: on peut utiliser `df.drop()`, l'avantage étant qu'on peut faire l'opération en place

```{code-cell} ipython3
# à vous

# df.drop(...)
```

```{code-cell} ipython3
:tags: [raises-exception]

# ceci doit afficher True

# la forme après nettoyage
df.shape == (7386, 4)
```

### option 2: sélection avec un masque et `[]`

```{code-cell} ipython3
:hide_input: false

# on recharge à tout hasard
df = pd.read_csv("data/television.txt", sep="\t").dropna(axis='columns', how='all')
print(df.shape)
```

+++ {"tags": ["level_basic"]}

option 2: il y a plein d'autres façons de faire, on peut aussi utiliser tout simplement un masque

```{code-cell} ipython3
# à vous
# df = ...
```

```{code-cell} ipython3
:tags: [raises-exception]

# ceci doit afficher True

# la forme après nettoyage
df.shape == (7386, 4)
```

## sauver un fichier excel

+++ {"hide_input": true, "tags": ["level_basic"]}

je vous laisse conclure le TP, il s'agit d'enregistrer nos données nettoyées dans un fichier excel

```{code-cell} ipython3
# à vous

filename = "television.xlsx"

# df.to_excel?
```

je vous laisse éventuellement vérifier votre code en rechargeant sous excel le fichier produit

+++

```{image} media/television.png
:align: center
```

+++

***
