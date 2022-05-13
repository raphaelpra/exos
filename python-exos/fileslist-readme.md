---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"run_control": {"frozen": false, "read_only": false}}

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
</div>

+++ {"run_control": {"frozen": false, "read_only": false}}

# La librairie `pathlib`

```{code-cell} ipython3
from pathlib import Path
```

## commodité

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
# à quoi ça sert ce truc ?

# eh bien si par hasard vous changez un module importé
# APRÉS l'avoir déjà chargé dans ce notebook
# avec cette formule magique le notebook sera capabale
# de RECHARGER la nouvelle version
# bref c'est plus pratique; mais ce n'est pas obligatoire du tout hein...

%load_ext autoreload
%autoreload 2
```

## initialisation

+++

on va partir d'un dossier avec un peu de contenu; c'est pour simuler par exemple un dossier avec des logs

```{code-cell} ipython3
# on nettoie bien tout pour être sûr
!rm -rf pathlib-foo
```

```{code-cell} ipython3
from fileslist import init
init()
```

## il faut faire quoi ?

+++ {"run_control": {"frozen": false, "read_only": false}}

Il s'agit d'écrire une fonction qui

* construit un chemin à partir d'une variable `root` de type `str`  (qui va désigner la racine de tout ceci)
  * et dedans on va isoler un dossier particulier (dont le nom est fourni par une variable `course`)
  * et dedans on se concentre sur le dossier `logs`

* dans ce dossier `logs`, on va chercher tous les fichiers qui sont présents; 2 modes
  * `deep=False` : les fichiers présents dans ce dossier exactement
  * `deep=True` ou à n'importe quel niveau de profondeur sous ce dossier

* puis tous les fichiers trouvés sont triés selon `criteria`
  1. `name` soit par le (dernier) nom du fichier
  1. `namelen` soit par longueur du (dernier) nom du fichier
  1. `size` soit sur la taille du fichier

```{code-cell} ipython3
from fileslist import sort_files
help(sort_files)
```

+++ {"run_control": {"frozen": false, "read_only": false}}

### Exemples

```{code-cell} ipython3
here = Path.cwd()
here
```

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
sort_files(here, "pathlib-foo", deep=True, criteria='name')
```

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
sort_files(here, "pathlib-foo", deep=True, criteria='namelen')
```

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
sort_files(here, "pathlib-foo", deep=True, criteria='size')
```

+++ {"run_control": {"frozen": false, "read_only": false}}

## Indices

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
from pathlib import Path

x = Path("pathlib-foo", "logs", "dir100", "filecxx")
x
```

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
list(x.parts)
```

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
# pour avoir la taille
x.stat().st_size
```

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
y = Path("pathlib-foo", "logs")
list(y.glob("*"))
```

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
list(y.glob("**/*"))
```

***
