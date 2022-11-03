---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
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
  title: lister les fichiers *.truc
---

# lister les fichiers *.truc

+++

en 2022 tous les calculs/parcours sur le contenu du disque, dossiers, fichiers, et métadonnées telles que tailles, dates, etc... se font avec le couteau suisse `pathlib`

```{code-cell} ipython3
from pathlib import Path
```

(et non plus avec `os.path` et autres `glob` comme on aurait pu le faire dans le passé)

+++

## exercice v1

* écrire une fonction qui prend en paramètre un nom de dossier (une str)
* et une extension (une str aussi), par exemple `truc`
* parcourt tous les fichiers dans ce dossier (ou ses sous-dossiers) avec cette extension (i.e. de la forme `*.truc`)
* et qui affiche (avec print) pour chacun d'eux
  * le nom complet (à partir de la racine du disque dur), sa taille et la date/heure de dernière modification
  * la première ligne

* **en option**, on peut avoir envie de trier les fichiers par nom

+++

### exemples

+++

```bash
# exemple d'appel
In [11]: scanv1("/Users/Jean Dupont/cours-python/", "py")
File /Users/Jean Dupont/cours-python/notebooks/bidule.py
  2663 B last modified on 2022-05-15 15:06:22
  first line: def bidule(arg1, arg2):
File /Users/Jean Dupont/cours-python/notebooks/machin.py
  2663 B last modified on 2022-08-21 21:09:12
  first line: # la fonction machin doit faire un tri
<etc...>
```

+++

```bash
# un autre exemple: on cherche dans le dossier courant
# qui ici se trouve être le même; on affiche quand même
# les chemins complets
In [12]: scanv1(".", "py")
File /Users/Jean Dupont/cours-python/notebooks/bidule.py
  2663 B last modified on 2022-05-15 15:06:22
  first line: def bidule(arg1, arg2):
File /Users/Jean Dupont/cours-python/notebooks/machin.py
  2663 B last modified on 2022-08-21 21:09:12
  first line: # la fonction machin doit faire un tri
<etc...>
```

+++

### indices

+++

certains traits qu'on peut avoir envie d'utiliser:

```{code-cell} ipython3
# créer une instance de Path
# qui correspond au dossier courant
p = Path(".")
```

```{code-cell} ipython3
# avec resolve() je peux calculer le chemin complet pour arriver
# à un objet Path (en partant de la racine des fichiers)
p.resolve()
```

```{code-cell} ipython3
# les méta données
#        taille
#                      date de dernière modification
p.stat().st_size,   p.stat().st_mtime
```

```{code-cell} ipython3
# st_mtime retourne un 'epoch' 
# c'est-à-dire un nombre de secondes 
# depuis le 1er janvier 1970

# pour traduire ça en date 'lisible'
from datetime import datetime as DateTime

dt = DateTime.fromtimestamp(p.stat().st_mtime)
f"la date est {dt}"
```

vous aurez aussi besoin de voir la documentation du module `pathlib` pour la méthode `Path.glob()`

```{code-cell} ipython3
# à vous de jouer
def scanv1():
    pass
```

## exercice v2

vous insérez le code de la v1 dans un programme python `scan.py` qu'on peut lancer depuis le terminal, par exemple comme ceci

```bash
$ python scan.py /Users/Jean Dupont/cours-python py
File /Users/Jean Dupont/cours-python/notebooks/bidule.py
  2663 B last modified on 2022-05-15 15:06:22
  first line: def bidule(arg1, arg2):
File /Users/Jean Dupont/cours-python/notebooks/machin.py
  2663 B last modified on 2022-08-21 21:09:12
  first line: # la fonction machin doit faire un tri
<etc...>
```

+++

## exercice v3

idem mais on a plus de choix pour décrire la ou les extensions qui nous intéressent; le paramètre extension peut maintenant être
  * vide (tous les fichiers)
  * ou une chaine simple
  * ou une liste d'extensions (ou même plus généralement un *itérable* d'extensions)

```{code-cell} ipython3
# à vous de jouer
def scanv3():
    pass
```

```python
# exemple d'appel
scanv3(Path.home() / "flotpython-exos/", 
       ("py", "md"), recursive=True)
```
