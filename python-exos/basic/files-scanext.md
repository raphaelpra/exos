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
---

# parcours de fichiers

+++

en 2022 tous les calculs/parcours sur le contenu du disque, dossiers, fichiers, et métadonnées telles que tailles, dates, etc... se font avec le couteau suisse `pathlib`

```{code-cell} ipython3
from pathlib import Path
```

(et non plus avec `os.path` et autres `glob` comme on aurait pu le faire dans le passé)

+++

## exercice v1

* écrire une fonction qui prend en paramètre un nom de dossier (une str)
* qui liste tous les fichiers avec **une** certaine extension dans le dossier
* afficher pour chacun d'eux
  * le nom complet, sa taille et la date/heure de dernière modification
  * la première ligne

* en option, on peut avoir envie de trier les fichiers par nom

+++

### indices

+++

certains traits qu'on peut avoir envie d'utiliser:

```{code-cell} ipython3
# le dossier courant
x = Path(".")

# un fichier dans un dossier
myself = x / "filescanner.nb.md"

# avec resolve() je peux calculer le chemin complet pour arriver
# à un objet Path
x.resolve()

# les méta données
#              taille
#                                   date de dernière modification
myself.stat().st_size, myself.stat().st_mtime
```

### à vous

```{code-cell} ipython3
# à vous de jouer
def scanv1():
    pass
```

```{code-cell} ipython3
# exemple d'appel
"""
scanv1("/Users/Jean Dupont/cours-python/", "py")
""";
```

```{code-cell} ipython3
# ou encore
"""
scanv1("../..", "md")
""";
```

## exercice v2

idem mais

* on peut passer le dossier sous la forme d'une str **ou** d'un objet Path
* on a plus de choix pour décrire la ou les extensions qui nous intéressent; le paramètre extension peut maintenant être
  * vide (tous les fichiers)
  * ou une chaine simple
  * ou une liste d'extensions (ou même plus généralement un *itérable* d'extensions)
* on peut passer un paramètre optionnel `recursive=False` qui indique
  * si la recherche se fait dans tout le contenu du dossier,
  * ou si au contraire seuls les fichiers placés directement sous le dossier sont concernés

```{code-cell} ipython3
# à vous de jouer
def scanv2():
    pass
```

```{code-cell} ipython3
# exemple d'appel
"""
scanv2(Path.home() / "flotpython-exos/", ("py", "md", recursive=True)
""";
```

## variantes

vous pouvez par exemple

* décider que le premier paramètre est optionnel, et dans ce cas on travaille sur le dossier courant
* ...

+++

---

+++

