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
  title: exo titanic
---

# les passagers du titanic

```{code-cell} ipython3
import pandas as pd
```

## les données

```{code-cell} ipython3
df_raw = pd.read_csv('../data/titanic.csv', index_col='PassengerId')
```

```{code-cell} ipython3
df_raw.head()
```

## ce qu'il faut faire


+++

----

+++

## simplification

+++

**[consigne]** simplifier la table, ne gardez que les colonnes qui après renommage s'appellent `survived`, `class`, `sex`, et `age`

```{code-cell} ipython3
# à vous
df = ...
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell 

# v0 - not too nice but works

df = df_raw[['Survived', 'Pclass', 'Sex', 'Age']]
df.columns = ['survived', 'class', 'sex', 'age']
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell 

columns = {'Survived': 'survived', 'Pclass': 'class', 
           'Sex': 'sex', 'Age': 'age'}

df = df_raw[columns.keys()].rename(columns=columns)
```

```{code-cell} ipython3
df.head()
```

## taux de survie par sexe

+++

**[consigne]** calculez le taux de survie par sexe (2 valeurs)

```{code-cell} ipython3
# à vous
...
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-begin

# survival rate by sex
df.groupby('sex')['survived'].mean()
```

### décortiquons un peu

```{code-cell} ipython3
# let's decompose a bit 
# this object df.groupby('sex')
# has two parts, female -> dataframe, and male -> dataframe

for criteria, subdf in df.groupby('sex'):
    print(criteria, type(subdf), subdf.columns)
```

```{code-cell} ipython3
# if we now look at its sex attribute,
# it still has 2 parts,
# female -> Series
# male -> Series

for criteria, subseries in df.groupby('sex').survived:
    print(criteria, type(subseries))
```

```{code-cell} ipython3
# so when we apply mean() on that object
# it results a Series that maps
# female -> mean(...) and male -> mean()

M = df.groupby('sex').survived.mean()
type(M), M
```

```{code-cell} ipython3
# prune-end
```

## survie selon deux critères

+++

**[consigne]** calculez le taux de survie par sexe et classe (6 valeurs)
* faites ce dernier calcul de deux façons, à base de de `pivot_table()` et de `groupby()`
* dans les deux versions, envisagez aussi de calculer le **nombre** de survivants plutôt que le taux
* comment choisir dans quel ordre on présente les résultats (sexe en ligne ou en colonne)

+++

### moyenne avec groupby

```{code-cell} ipython3
# à vous - pour produire un tableau de 6 valeurs 
# 2 lignes (female / male) et 3 colonnes pour les classes
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

mean = df.groupby(['sex', 'class'])['survived'].mean()
mean
```

```{code-cell} ipython3
# prune-cell

# nicer when unstacked

mean.unstack()
```

### pareil dans l'autre sens (sexe en colonne)

```{code-cell} ipython3
# à vous - pour produire un tableau de 6 valeurs 
# 2 lignes (female / male) et 3 colonnes pour les classes
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

# I can either select the level to unstack

df.groupby(by=['sex', 'class'])['survived'].mean().unstack(0)
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

# or change the order of the initial multiindex

df.groupby(by=['class', 'sex'])['survived'].mean().unstack()
```

### moyenne avec pivot_table()

```{code-cell} ipython3
# à vous
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

# the 'aggfunc' parameter defaults to 'mean'
df.pivot_table('survived', index='sex', columns='class')
```

### idem mais dans l'autre sens

```{code-cell} ipython3
# à vous
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

df.pivot_table('survived', index='class', columns='sex')
```

### nombre de survivants avec pivot_table()

```{code-cell} ipython3
# à vous
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

# just define `aggfunc` 

S = df.pivot_table('survived', index='sex', columns='class', aggfunc='sum')
S
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

# check consistency

S.sum().sum() == df.survived.sum()
```
