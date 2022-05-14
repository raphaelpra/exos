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
  title: 'trouver tous les fichiers *.truc'
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

# solutions

+++

## solution v1

```{code-cell} ipython3
# comme toujours c'est juste *une* façon de faire hein...
def scanv1(folder, extension):
    # on convertit la chaine en Path
    # pour pouvoir utiliser la librairie
    path = Path(folder)
    # on scanne
    for child in path.glob(f"*.{extension}"):
        # avec resolve() on obtient le chemin canonique
        print(f"File {child.resolve()}")
        # la taille et l'heure de modification sont accessibles au travers
        # de la méthode stat()
        print(f"  {child.stat().st_size} B last modified on {child.stat().st_mtime}")
        # pour lire seulement la première ligne
        # on pourrait faire un for + break
        # mais c'est plus élégant comme ceci
        with child.open() as feed:
            print("  first line:", next(feed), end="")
```

```{code-cell} ipython3
# scanv1("../slides", "md")
```

```{code-cell} ipython3
# si on veut trier, il suffit de rajouter un sorted()
# remarquez que ça signifie que path.glob()
# sait se faire trier
def scanv1_sorted(folder, extension):
    path = Path(folder)
    #            ↓↓↓↓↓↓↓
    for child in sorted(path.glob(f"*.{extension}")):
        print(f"File {child.resolve()}")
        print(f"  {child.stat().st_size} B last modified on {child.stat().st_mtime}")
        with child.open() as feed:
            print("  first line:", next(feed), end="")
```

```{code-cell} ipython3
# scanv1_sorted("../slides", "md")
```

## solution v2

```{code-cell} ipython3
# en fait la v1 accepte déjà les objets de type Path

def scanv2(folder, extensions=None, recursive=False):
    # optionnel mais si on veut éviter la création
    # d'objets inutiles
    if isinstance(folder, Path):
        # déjà un Path
        path = folder
    if isinstance(folder, str):
        # une chaine: on convertit
        path = Path(folder)
    else:
        raise TypeError(f"{folder} neither str nor Path")
    # pour faire un parcours récursif, il suffit d'utiliser
    # le pattern "**"
    pattern = "**/*" if recursive else "*"
    # la gestion des extensions est du coup sasez différente
    for child in path.glob(pattern):
        # à ce stade, child est .. un Path aussi
        ext = child.suffix[1:]
        # on regarde s'il y a lieu d'ignorer ce fichier
        if extensions is not None:
            if isinstance(extensions, str):
                if ext != extensions:
                    continue
            else:
                if ext not in extensions:
                    continue
        # le reste est comme dans la v1
        print(f"File {child.resolve()}")
        print(f"  {child.stat().st_size} B last modified on {child.stat().st_mtime}")
        with child.open() as feed:
            print("  first line:", next(feed), end="")
```

```{code-cell} ipython3
# scanv2("..", ('md', 'txt'), recursive=True)
```

je vous laisse à titre d'exercice corriger quelques défauts résiduels:

* les fichiers de taille nulle posent problème (pour le `next(feed)`)
* les fichiers binaires posent problème (pareil)

pour arranger ça il faut être un peu plus soigneux

+++

***
