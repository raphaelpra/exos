---
marp: true
markdown.marp.enableHtml: true
theme: default
class: invert
# backgroundImage: url('https://marp.app/assets/hero-background.svg')
# color: #44f
header: un TP sur les fichiers
#footer: 'cours Python ![height:40px](media/logo-python.svg)'
footer: 'cours Python
# tmp
paginate: true
---

<style>
@import url('https://fonts.googleapis.com/css?family=Patrick+Hand|Patrick+Hand+SC');

section {
    font-family: "Patrick Hand", Verdana;
    font-size: xxx-large;
}

section::after {
  content: 'Slide ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
}

.small {
  font-size: 70%;
}

</style>

# <!-- fit -->les fichiers

<!-- _backgroundImage: url("pexels-mike-1181772.jpg") -->
<!-- _color: #229 -->

---
## on va faire quoi ?
<!-- fontSize: smaller -->

- les fichiers et l'OS; comment ouvrir, pourquoi fermer ?
- différents formats de fichier
  - pickle (ouille ça pique, c'est du binaire)
  - json (on se sent un peu mieux)
  - csv (ah là on parle)
  - yaml (de plus en plus populaire)
- parser un nouveau format de fichier

---
# modalités du cours

- on ouvre vs-code
- on participe

---
# <!--fit --> les fichiers et l'OS

<!-- _backgroundImage: url("pexels-pixabay-270572.jpg") -->
<!-- # _color: #eee -->

---
# c'est quoi l'OS ? ![height:150px](operating_system_placement.png)


- votre code ne cause jamais directement au harware
- mais au travers d'abstractions
- dont la notion de "fichier"

---
# questions préliminaires

- qu'est-ce qu'un fichier ?
- que contient un fichier ?
- quelles sont les étapes pour y accéder ?

---
# <!-- fit--> Lire un fichier simple

---
# ouverture d'un fichier

```
f = open("hello.txt")
```

- que se passe-t-il ?
- pensez à consulter la documentation
  (comment on la trouve ?)
- que peut-on faire de `f` ?

---
# ouverture d'un fichier (2)

- analyser les types des différents objets
- avancer étape par étape

---
# ouverture d'un fichier (3)

que se passe-t-il si on oublie de fermer le fichier ?

> on va écrire un code qui ouvre `n`  fichiers
> le faire tourner avec `n`= 10, 100, 1000, ...

pouvez-vous prédire ce qui va passer ?

---
# les context managers

l'idiome à **toujours utiliser** pour lire un fichier texte

```python
with open("hello.txt") as f:
    for line in f:
        print(line.strip())
```

ou encore `print(line, end="")`

quelles autres formules connaissiez-vous pour faire ça ?

---
# fichiers texte - contenu

- installez l'extension vscode *Hex Editor*
- regarder le contenu de `hello.txt` avec vscode
  - utilisez *clic droit* -> *Open With* -> *Hex Editor*
- comparez avec  
  <https://www.rapidtables.com/code/text/ascii-table.html>

---
# fichiers texte - contenu (2)

- pareil avec `bonjour.txt`
- que constatez-vous ?
- voyez aussi  
  <https://www.utf8-chartable.de/>

---
# fichiers binaires

- pareil avec `tiny.pickle`  
- ouvrez-le "normalement"
  (pour l'instant sans utiliser la librairie `pickle`)
- comment faut-il adapter le code ?
- que constatez-vous ? (indice: les types !)

---
# à retenir

- toujours ouvrir un fichier avec `with`
- un fichier peut
  - contenir du texte (qu'il faut alors décoder)
    pour obtenir un `str`
  - ou pas - on obtient alors des `bytes`

---
# <!-- fit --> les différents <br>formats de fichier

<!-- _backgroundImage: url("pexels-pixabay-162553.jpg") -->
<!-- #_color: yellow -->

---
Tout le monde ne crée pas sa propre structure de fichier !
Il existe des formats ***standard*** qui permettent une interaction entre les programmes et même différents langages de programmation

---
# <!-- fit --> le format pickle

<!-- _backgroundImage: url("pexels-eva-bronzini-5503189.jpg") -->
<!-- #_color: yellow -->

---
c'est le format *intégré* de Python

- format binaire (s'ouvre avec `open(name, 'rb')`)
- pour sérialiser notamment les *types de base*
- lisez la documentation du module `pickle`
- essayez de lire le fichier `tiny.pickle`
- inspectez les types des objets dans la donnée

---
# écriture

- partez de ce que vous venez de lire
- modifiez certaines des données
- sauvegardez-les dans un nouveau fichier  
  `tiny-changed.pickle`
- et relisez-le pour vérifier que "ça marche"

---
# <!-- fit --> autre format: json

---
## à vous de jouer

- on va refaire pareil à partir de `tiny.json`
- lisez-la doc et écrivez le code qui lit ce fichier
- modifiez la donnée lue, et sauvez-la
- est-ce qu'on peut y mettre un ensemble ?

---
# <!-- fit --> encore un: yaml

---
## yet again

- trouvez la doc de PyYAML
- lisez le fichier `tiny.yaml`
- comment peut-on comparer avec JSON ?

---
# <!-- fit --> et aussi: les csv

(les mêmes que ceux qu'on a vus dans le cours pandas)

---
# on recommence

- lisez la documentation du module csv  
  google `python module csv`
- essayez de lire le fichier `pokemon.csv`
- sauriez-vous créer une dataframe ?  
  (sans utiliser `pd.read_csv` évidemment)

---
# <!-- fit --> formats custom

---
* comment peut-on lire (on dit *parse*) des formats de fichiers inconnus ?
* pour cela, 2 armes
  * le type `str` fournit plein de méthodes  
    notamment `strip()` `split()` et `join()`
  * le module `re` (pour *regular expressions*)  
    peut également être utile

---
# exercice

* sans importer de module additionnel,
* lisez le fichier `notes.txt`
* créez et affichez un dictionnaire  
  *nom élève* → note

---
# un mot sur `print()`

* l'opération la plus simple pour sauver un résultat
* mais pas très utile en réalité
* car le plus souvent limitée à un lecteur humain
* on peut écrire dans un fichier `f` (ouvert en écriture)  
  avec `print(des, trucs, file=f)`

---
# les redirections de `bash` (pour info)

* quand il est lancé, votre programme a un `stdin` et un `stdout` (et un `stderr` mais c'est plus anecdotique)
* qui sont créés par bash (et sont branchés sur le terminal)
* vous pouvez les rediriger en faisant
  ```bash
  python myhack.py < the-input > the-output
  ```

---
# exercice: écrivez un programme

* qui lit sans fin le texte entré dans le terminal
* regarde si le texte commence par un `q`
* si oui c'est la fin du programme
* sinon affiche le nombre de mots dans la ligne  
  et recommence

voir consigne et indices slide suivant

---
## consigne

ne pas utiliser `input()`, mais plutôt `sys.stdin`

## indices

* de quel type est `sys.stdin` ?
* si vous voulez ajouter un *prompt*  
  (un peu comme les `>>>` de python)  
  lancez votre programme avec `python -u mycode.py`

---
# regexps, en deux mots

* l'idée est de décrire une *famille* de chaines
* à partir d'une autre chaine (la *regexp*)
* qui utilise des opérateurs
  * comme p.e. `*`
  * pour indiquer 'un nombre quelconque de fois' telle ou telle autre *regexp*

---
# regexp exemple

`ab((cd)|(ef))*` décrit un ensemble qui

* ne contient que des mots qui commencent par `ab`
* contient `abcd` et aussi `abef`
* ou encore `abcdcdefcd`
* mais pas `abce` ni `abcde`

---
# avertissement

> Some people, when confronted with a problem, think
“I know, I'll use regular expressions.”   Now they have two problems.


<http://regex.info/blog/2006-09-15/247>
