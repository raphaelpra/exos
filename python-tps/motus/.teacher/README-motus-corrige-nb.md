---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
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
  title: 'TP: le jeu de motus'
---

+++ {"tags": ["raises-exception"]}

# le jeu de motus

+++

inspiré d'un jeu télévisé; pour ceux qui ne connaissent pas les règles, on parle d'un jeu qui s'insipre un peu du mastermind, mais avec des mots; il s'agit de trouver un mot caché, on essaie un mot et en réponse on nous dit si chaque lettre est présente et/ou bien placée.

+++

pour plus de détails sur ce jeu, voyez <https://fr.wikipedia.org/wiki/Motus_(jeu_t%C3%A9l%C3%A9vis%C3%A9)>

+++

## les règles

voici un exemple de session, le mot à deviner était `CITRON`

![](motus-example.png)

ici on a 
* d'abord essayé `CASTOR`; la 'correction' nous a appris que
  * le mot commence par un `C`,
  * qu'il contient un `O` en 5-ème position,
  * qu'il ontient un `T` mais pas en 4-éme position,
  * et un `R` mais pas en dernière position,
  * et pas de `A` ni de `S`
* on a ensuite essayé `CINEMA` ou a appris que
  * la seconde lettre est `I`,
  * le mot contient un `N` mais pas en 3-ème position,
  * etc...

les codes de couleur sont donc
* rouge: lettre bien placée
* jaune: lettre mal placée
* bleu (ou blanc, selon les supports): lettre absente

<div class=note>

**note:** en fait au tout début on vous montre la première lettre, en rouge; mais bon ça ne change pas grand-chose à notre TP
    
</div>

+++

### petite subtilité

il faut préciser un peu ce qu'il se passe lorsque l'un des deux mots (le caché, ou la tentative) contient des lettres en double

la règle est que on commence par donner autant de rouges que possible, puis ces lettres-là sont enlevées du décompte; 
puis on donne ensuite autant de jaunes que possible, et à chaque fois les lettres sont enlevées du décompte; 

+++

c'est  ainsi que par exemple
![](motus-multiple-1.png)

vous remarquez que la réponse contient un `d` bleu, alors qu'il y a deux `d` dans le mot à deviner, mais comme ils ont déjà été 'consommés' pour les deux `d` rouges, le troisième `d` est considéré comme absent.

+++

autre exemple
![](motus-multiple-2.png)

vous remarquez que la réponse contient un `p` rouge en 3ème position, et un `p` jaune en première position qui correspond à la deuxième position du mot caché; si notre essai avait contenu un troisième `p`, il aurait été corrigé en bleu.

```{code-cell} ipython3
# prune-cell
from motus import show_example

show_example("addition", "addendum")
```

```{code-cell} ipython3
# prune-cell
from motus import show_example

show_example("apprise", "papyrus")
```

```{code-cell} ipython3

```

## une librarie utile `colorama`

+++

pour l'affichage j'ai utilisé ci-dessus la librairie `colorama`, voici quelques exemples, cherchez la documentation si vous avez besoin de plus de détails

```{code-cell} ipython3
from colorama import Back, Style
```

```{code-cell} ipython3
print(f"{Back.RED} C  I {Back.YELLOW} N {Back.BLUE} E M A {Style.RESET_ALL}")
```

```{code-cell} ipython3
from colorama import Back, Style
print(f"{Back.RED} C {Style.RESET_ALL} {Back.RED} I {Style.RESET_ALL} "
      f"{Back.YELLOW} N {Style.RESET_ALL} {Back.BLUE} E {Style.RESET_ALL} "
      f"{Back.YELLOW} M {Style.RESET_ALL} {Back.YELLOW} A {Style.RESET_ALL}")
```
