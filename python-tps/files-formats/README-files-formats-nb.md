---
jupyter:
  jupytext:
    cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted,-editable
    notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
      -jupytext.text_representation.format_version,-language_info.version, -language_info.codemirror_mode.version,
      -language_info.codemirror_mode,-language_info.file_extension, -language_info.mimetype,
      -toc, -rise, -version
    text_representation:
      extension: .md
      format_name: markdown
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
  language_info:
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
---

# fichiers et formats

{download}`Commencez par télécharger le zip<./ARTEFACTS-files-formats.zip>`


## on va faire quoi ?

- les fichiers et l'OS; comment ouvrir, pourquoi fermer ?
- différents formats de fichier *standard8
  - pickle (ouille ça pique, c'est du binaire)
  - json (on se sent un peu mieux)
  - csv (ah là on parle)
  - yaml (de plus en plus populaire)
- parser un format de fichier *custom*


### modalités du TP

- on ouvre vs-code
- on participe


## les fichiers et l'OS

c'est quoi l'OS ? 

```{image} operating_system_placement.png
:align: center
:width: 200px
```

- votre code ne cause jamais directement au harware
- mais au travers d'abstractions
- dont la notion de "fichier"


### questions préliminaires

- qu'est-ce qu'un fichier ?
- que contient un fichier ?
- quelles sont les étapes pour y accéder ?


## lire un fichier simple

(le fichier `hello.txt` fait partie du zip)

### ouverture d'un fichier

```
f = open("hello.txt")
```

- que se passe-t-il ?
- pensez à consulter la documentation
  (comment on la trouve ?)
- que peut-on faire de `f` ?

### ouverture d'un fichier (2)

- analyser les types des différents objets
- avancer étape par étape

### ouverture d'un fichier (3)

que se passe-t-il si on oublie de fermer le fichier ?

> on va écrire un code qui ouvre `n`  fichiers
> le faire tourner avec `n`= 10, 100, 1000, ...

pouvez-vous prédire ce qui va passer ?

<!-- #region -->
## les context managers

l'idiome à **toujours utiliser** pour lire un fichier texte

```python
# TOUJOURS lire ou écrire un fichier avec un with !

with open("hello.txt") as f:
    for line in f:
        print(line, end="")
```

quelles autres formules connaissiez-vous pour faire ça ?


````{admonition} pourquoi le end="" ?
:class: admonition-small

à chaque itération, vous allez trouver dans la variable `line`, eh bien la ligne suivante évidemment,  
sauf que ceci **contient un caractère de fin de ligne** - qu'on appelle aussi *newline*  
du coup si vous faites un `print(line)` (essayez..) vous allez avoir une ligne blanche sur deux !

une autre approche consisterait à utiliser `line.rstrip("\n")` qui enlève l'éventuel *newline*;  
je dis éventuel car la dernière ligne ne contient pas toujours ce fameux *newline*; le monde est compliqué parfois...
````
<!-- #endregion -->

## fichiers texte - contenu

### ASCII

- installez l'extension vscode *Hex Editor*
- regarder le contenu de `hello.txt` avec vscode
  - utilisez *clic droit* -> *Open With* -> *Hex Editor*
- comparez avec  
  <https://www.rapidtables.com/code/text/ascii-table.html>


### Unicode

- pareil avec `bonjour.txt`
- que constatez-vous ?
- voyez aussi <https://www.utf8-chartable.de/>  


## fichiers binaires

### pickle

- pareil avec `tiny.pickle`  
- ouvrez-le "normalement"
  (pour l'instant sans utiliser la librairie `pickle`)
- comment faut-il adapter le code ?
- que constatez-vous ? (indice: les types !)

````{admonition} à retenir
:class: important

- toujours ouvrir un fichier avec `with`
- un fichier peut
  - contenir du texte (qu'il faut alors décoder)
    pour obtenir un `str`
  - ou pas - on obtient alors des `bytes`
````


## les différents formats de fichier

Tout le monde ne crée pas sa propre structure de fichier !  
Il existe des formats ***standard*** qui permettent une interaction entre les programmes et même différents langages de programmation


## le format pickle

c'est le format *intégré* de Python  
il permet de lire/écrire non seulement   

- format binaire (s'ouvre avec `open(name, 'rb')`)
- pour sérialiser notamment les types de base,
  c-a-d non seulement des atomes (nombres, chaines...)  
  mais aussi des **structures plus complexes**, avec des containers etc...
- lisez la documentation du module `pickle`
- essayez de lire le fichier `tiny.pickle`
- inspectez les types des objets dans la donnée

````{admonition} b pour binaire
:class: note

dans `open(name, 'rb')` le `r` est pour *read* et le `b` pour *binary*
````


### écriture

- partez de ce que vous venez de lire
- modifiez certaines des données
- sauvegardez-les dans un nouveau fichier  
  `tiny-changed.pickle`
- et relisez-le pour vérifier que "ça marche"


## autre format: json

à vous de jouer

- on va refaire pareil à partir de `tiny.json`
- lisez-la doc et écrivez le code qui lit ce fichier
- modifiez la donnée lue, et sauvez-la
- est-ce qu'on peut y mettre un ensemble ? ou un tuple ?


## encore un: yaml

- trouvez la doc de PyYAML
- lisez le fichier `tiny.yaml`
- comment peut-on comparer avec JSON ?


## et aussi: les csv

on recommence:

- lisez la documentation du module csv  
  google `python module csv`
- essayez de lire le fichier `pokemon.csv`
- sauriez-vous créer une dataframe ?  
  (sans utiliser `pd.read_csv` évidemment)


## formats custom

* comment peut-on lire (on dit *parse*) des formats de fichiers inconnus ?
* pour cela, 2 armes
  * le type `str` fournit plein de méthodes  
    notamment `strip()` `split()` et `join()`
  * le module `re` (pour *regular expressions*)  
    peut également être utile


### exercice

* sans importer de module additionnel,
* lisez le fichier `notes.txt`
* créez et affichez un dictionnaire  
  *nom élève* → note

````{admonition} un mot sur print()

* l'opération la plus simple pour sauver un résultat
* mais pas très utile en réalité
* car le plus souvent limitée à un lecteur humain
* on peut écrire dans un fichier `f` (ouvert en écriture)  
  avec `print(des, trucs, file=f)`
````

````{admonition} les redirections de bash (pour info)

* quand il est lancé, votre programme a un `stdin` et un `stdout` (et un `stderr` mais c'est plus anecdotique)
* qui sont créés par bash (et sont branchés sur le terminal)
* vous pouvez les rediriger en faisant
  ```bash
  python myhack.py < the-input > the-output
  ```
````


## exercice: écrivez un programme

* qui lit sans fin le texte entré dans le terminal
* regarde si le texte commence par un `q`
* si oui c'est la fin du programme
* sinon affiche le nombre de mots dans la ligne  
  et recommence

````{admonition} consigne

ne pas utiliser `input()`, mais plutôt `sys.stdin`
````

````{admonition} indices
:class: tip

* de quel type est `sys.stdin` ?
* si vous voulez ajouter un *prompt*  
  (un peu comme les `>>>` de python)  
  lancez votre programme avec `python -u mycode.py`
````


## regexps, en deux mots

sans transition..

* l'idée est de décrire une *famille* de chaines
* à partir d'une autre chaine (la *regexp*)
* qui utilise des opérateurs
  * comme p.e. `*`
  * pour indiquer 'un nombre quelconque de fois' telle ou telle autre *regexp*


### regexp exemple

`ab((cd)|(ef))*` décrit un ensemble qui

* ne contient que des mots qui commencent par `ab`
* contient `abcd` et aussi `abef`
* ou encore `abcdcdefcd`
* mais pas `abce` ni `abcde`

````{admonition} avertissement

> Some people, when confronted with a problem, think
“I know, I'll use regular expressions.”   Now they have two problems.

<http://regex.info/blog/2006-09-15/247>
````
