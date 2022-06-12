---
jupytext:
  cell_metadata_filter: all, -hidden, -heading_collapsed, -run_control, -trusted
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
---

```{code-cell} ipython3
import numpy as np
```

# indices

+++

la fonction `np.indices` est très pratique pour obtenir les rangs dans le tableau

```{code-cell} ipython3
# par exemple
I, J = np.indices((3, 4))
```

```{code-cell} ipython3
I, J
```

## échiquier

+++

### base

+++

On veut écrire une fonction qui produit un échiquier

ex. avec `checkers(3, 4)`

|  |  |  |  |
|--|--|--|--|
| 0| 1| 0| 1|
| 1| 0| 1| 0|
| 0| 1| 0| 1|

**[consigne]** assurez-vous de bien renvoyer un tableau de booléens

```{code-cell} ipython3
# à vous

def checkers():
    ...
```

```{code-cell} ipython3
# ceci doit afficher True

checkers(3, 4).dtype == bool
```

```{code-cell} ipython3
# ceci doit afficher True

np.all(checkers(3, 4) == np.array([[0,1,0,1],[1,0,1,0],[0,1,0,1]]))
```

### affichage

+++

comment feriez-vous pour afficher le tableau comme un damier ?

**[indice]** voyez `plt.imshow()`

```{code-cell} ipython3
# à vous
...
```

### paramètrer le coin

+++

Pour corser un peu, on ajoute un paramètre optionnel qui indique, lorsqu'il est True, qu'on veut que l'échiquer est inversé

ex. avec `checkers(3, 4, True)`

|  |  |  |  |
|--|--|--|--|
| 1| 0| 1| 0|
| 0| 1| 0| 1|
| 1| 0| 1| 0|

mais les appels avec seulement deux paramètres continuent à fonctionner comme avant

```{code-cell} ipython3
# à vous
```

```{code-cell} ipython3
# ceci doit afficher True

np.all(checkers(3, 4) == np.array([[0,1,0,1],[1,0,1,0],[0,1,0,1]]))
```

```{code-cell} ipython3
# ceci doit afficher True

np.all(checkers(3, 4, True) == ~(checkers(3, 4)))
```

```{code-cell} ipython3
# pour débugger
checkers(3, 4)
```

```{code-cell} ipython3
# pour débugger
checkers(3, 4, True)
```

### tester

+++

On veut maintenant tester que si on ajoute ces deux formes on n'obtient que des 1

```{code-cell} ipython3
# à vous
```

## escaliers

+++

écrivez une fonction qui retourne une espèce de pyramide escalier comme ceci

si le paramètre est 2, on retourne un tableau de taille $2*n+1$

`stairs(2)`

| | | | | |
|-|-|-|-|-|
|0|1|2|1|0|
|1|2|3|2|1|
|2|3|4|3|2|
|1|2|3|2|1|
|0|1|2|1|0|

```{code-cell} ipython3
xxxx
```

```{code-cell} ipython3
I, J = np.indices((5, 5))
```

```{code-cell} ipython3
# si on décale applique abs()
abs(2-I), abs(2-J)
```

```{code-cell} ipython3
# si on les ajoute
abs(2-I) + abs(2-J)
```

```{code-cell} ipython3
# on y est presque
4-(abs(2-I) + abs(2-J))
```

```{code-cell} ipython3
# hence

def stairs(taille):
    """
    la pyramide en escaliers telle que décrite dans l'énoncé
    """
    total = 2 * taille + 1
    I, J = np.indices((total, total))
    # on décale et déforme avec valeur absolue, pour obtenir
    # deux formes déjà plus propices
    I2, J2 = np.abs(I-taille), np.abs(J-taille)
    # si ajoute on obtient un négatif,
    # avec 0 au centre et taille aux 4 coins
    negatif = I2 + J2
    # ne reste plus qu'à renverser
    return 2 * taille - negatif    
```

```{code-cell} ipython3
S2 = stairs(2); S2
```

```{code-cell} ipython3
# ce qui donne avec imshow
plt.imshow(S2);
```
