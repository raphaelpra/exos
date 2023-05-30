---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  encoding: '# -*- coding: utf-8 -*-'
  main_language: python
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
  title: 'TP: Dr Watson'
---

# Dr Watson

Indice: voyez la fonction `input()` pour poser une question et lire la réponse dans le terminal

```{code-cell} ipython3
reponse = input("une question: ")
```

```{code-cell} ipython3
# et le retour de input() c'est la chaine qu'on a tapée - sans newline ni rien
reponse
```

## v1: un coup, les mots-clé en dur

on veut écrire un programme qui
* pose une question, du genre `bonjour, à vous: `
* attend la réponse tapée par l'utilisateur
* puis:
  * selon que la réponse contient le mot `bien` ou `mal`  
    on affiche un message positif ou négatif (par exemple `C'est super!` et `Ohhhh, c'est triste.`)
  * si la phrase est vide par contre, on affiche `Tu n'es pas bavard.`
  * enfin si rien de tout cela, on affiche `Je ne comprends pas`
* dans tous les cas après la première réponse le programme s'arrête


une session pourrait ressembler à ceci

```
>>> watson()
bonjour, à vous: j'ai mal dormi aujourd'hui
Ohhhh, c'est triste.
C'est fini, au revoir !
>>>
```

Pour travailler vous pouvez éditer ce code

```{code-cell} ipython3
def watson():
    ...

watson()
```

## v2 - les mots-clé dans une liste

on change un peu le code; on veut reconnaitre les phrases positives ou négatives sur la base de plusieurs mots; par exemple
```
NEGATIVE_WORDS = ["mal", "triste", "marre"]
POSITIVE_WORDS = ["bien", "super", "content", "contente"]
```

+++

*Indice*: faites descendre votre cellule de code pour qu'elle soit toujours près de la consigne; pour cela sélectionner la cellule, assurez-vous d'être en mode 'commande' (la bordure à gauche doit être bleue; tapez `Escape` si nécessaire) et tapez le caractère `'D'` pour *down* ou `'U'` pour *Up*

+++

## v3 - meilleure idée ?

est-ce que de mettre les mots-clés dans une liste c'est une bonne idée ?
est-ce qu'on peut améliorer la performance du code du coup ?

+++

## v4 - les mots-clé dans un fichier

on veut pouvoir définir les mots-clé dans un fichier; on choisit le format suivant

```
$ cat watson.txt
POSITIVE bien super content contente
NEGATIVE mal triste marre
```

ajoutez dans votre code une fonction
`init_watson(filename)` qui retourne - par exemple - un tuple de deux ensembles de mots

+++

## v5 - boucle sans fin

au lieu de faire le traitement une seule fois, on va le faire indéfiniment; pour que tout de même on puisse sortir de là, on rajoute une nouvelle catégorie de mots dans le fichier de config:

```
$ cat watson-config.txt
POSITIVE bien super content contente
NEGATIVE mal triste marre
EXIT bye quit exit
```

et si un des mots de la phrase est contenu dans la nouvelle catégorie on arrête le programme complètement; c'est-à-dire qu'une session ressemblerait à ceci

```
>>> watson()
bonjour, à vous: j'ai bien dormi
C'est super, mais encore...
j'i mal au dents
Ohhhh, c'est triste, mais encore...
c'est fini
je ne comprends pas...
je veux dire exit
C'est fini, au revoir !
>>>
```

+++

## v6 - on ajoute des *magics*

+++

maintenant si la réponse commence par des mots magiques (qui commencent tous par un `!`), on les traite:
* `!somme` considère que tous les mots de la réponse sont des nombres, on les ajoute et on affiche la sommme
* `!unique` on affiche tous les mots de la réponse mais une seule fois par mot

c'est-à-dire qu'une session pourrait être:
```
>>> watson()
bonjour
!somme skdjf skdjf skfjs kjsf kjkdfj skdjf
voici la somme : 0
Mais encore...
!somme 123 45 678
voici la somme : 846
Mais encore...
!unique abc def abc def ghi abc
voici les mots uniques : {'abc', 'ghi', 'def'}
Mais encore...
exit
C'est fini, au revoir !
>>>
```

+++

## v7 - rendre la fonction réglable

+++

* on veut pouvoir passer le fichier de config en paramètre à la fonction `watson()`
* on veut aussi pouvoir lui passer des paramètres
  * un paramètre config (qui par défaut vaut `"watson-config.txt"`)
  un paramètre `debug` (qui par défaut est `False`) et dans ce cas on affiche un message qui montre où on a trouvé le mot

+++

```
# on utilise un autre fichier de config, et en mode debug
>>> watson("watson-config.en", True)
sdfsdf
je ne comprends pas...
awesome this morning
DEBUG: *awesome* this morning
C'est super, mais encore...
had a nice dream
DEBUG: had a *NICE* dream
C'est super, mais encore...
exit
C'est fini, au revoir !
```

+++

## v9 - refactoring

+++

on décide de refactorer le code en créant des classes; par exemple
* une classe `Phrase` qui sera crée pour chaque réponse
* une classe `Feeling` correspondant à chacun des deux ensembles de mots
* ... 

en option on peut aussi en faire un vrai programme Python qui se lance depuis la ligne de commande (voir pour ça la librairie `argparse`)

+++

***
