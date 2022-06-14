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
df.head()
```

## taux de survie par sexe

+++

**[consigne]** calculez le taux de survie par sexe (2 valeurs)

```{code-cell} ipython3
# à vous
...
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

### pareil dans l'autre sens (sexe en colonne)

```{code-cell} ipython3
# à vous - pour produire un tableau de 6 valeurs 
# 2 lignes (female / male) et 3 colonnes pour les classes
```

### moyenne avec pivot_table()

```{code-cell} ipython3
# à vous
```

### idem mais dans l'autre sens

```{code-cell} ipython3
# à vous
```

### nombre de survivants avec pivot_table()

```{code-cell} ipython3
# à vous
```
