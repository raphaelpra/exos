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

# analyse de texte

+++

on veut calculer la fréquence d'apparition des mots dans un texte

pour cela on vous demande d'écrire une classe qui s'utilise comme ceci  
(le fichier texte contient le premier chapitre du *Hitch-Hiker's Guide to the Galaxy* - alias hhgg)

+++

```
from wordcounts import WordCounts

wc = WordCounts("wordcounts-data.txt")

print(wc)

for word in ['arthur', 'people']:
    print(f"word {word} was found {wc.counter[word]} times")
```

+++

et ce code produirait alors ceci

```
python wordcounts_test.py
wordcounts-data.txt: 1612 words 588 different words
    the : 65
     he : 56
      a : 52
     to : 52
     it : 40
word arthur was found 16 times
word people was found 9 times
```

+++

## Indices

+++

* il est raisonnable de tout mettre en minuscule une bonne fois au tout début du traitement
* voyez `string.punctuation` éventuellement
* voyez aussi la classe `collections.Counter` qui va vous rendre la vie bien plus facile

+++

## variantes

+++

* comment trouveriez-vous tous les mots qui apparaissent entre 30 et 40 fois dans le texte ?


* si vous vous sentez confortable (il faut faire de la surcharge d'opérateur),
  faites en sorte qu'on puisse aussi écrire:
  ```
  for word in ['arthur', 'people']:
      # here we can index the WordCount instance directly
      print(f"word {word} was found {wc[word]} times")

  ```
