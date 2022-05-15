# Pile logicielle

pour les formations autour de Python

## avez-vous déjà ce qu'il faut ?

vous avez peut-être déjà installé Python sur votre ordinateur; mais comme il
existe 1001 façons d'installer Python, pour tester si votre installation est
correcte, voici une petite checklist

NB: si votre installation n'est pas bonne, le mieux est de
* bien tout nettoyer les installations précédentes
* repartir du début en suivant les indications des sections suivantes

### checklist

* créez un terminal - de préférence bash (voir ci-dessous);
  le terminal vous montre une invite (on dit aussi un *prompt*)
  + avec bash c'est un `$`, avec `cmd.exe` c'est un `%` - qui vous invite à taper du texte;
  dans les exemples qui suivent **je laisse le `$` ** pour qu'on comprenne
  que c'est du texte à taper dans le terminal, mais **il ne faut pas le taper** évidemment !
* tapez ceci dans le terminal

```
  $ python --version
  ```

  qui doit vous afficher quelque chose comme `Python 3.9.7`

  si vous voyez à la place un `command not found` ce n'est pas bon du tout

* maintenant on va essayer d'installer un module; tapez ceci (vous
  pouvez aussi le faire avec un autre module, comme par exemple
  `numpy` plutôt que `nbautoeval`)

```
  $ pip install nbautoeval
  ```

  qui va remplir un peu votre écran avec des détails sur cette
  installation; quoiqu'il en soit pour vérifer que l'installation de
  ce module `nbautoeval` a bien fonctionné, faites:

```
  $ python -c "import nbautoeval"
  ```

  qui, si ça fonctionne bien, ne va **rien vous dire** du tout

  si au contraire, vous avez une erreur qui contient
  `ModuleNotFoundError: No module named 'nbautoeval'` ce n'est pas bon
  du tout (mais essayez quand même le point suivant)

* dans ce dernier cas, vous pouvez essayer une méthode de secours,
  essayez d'installer le module avec cette fois

```
  $ python -m pip install nbautoeval
  ```

  et retentez ensuite

```
  $ python -c "import nbautoeval"
  ```

  qui doit toujours être silencieux

## terminal

nous utilisons le terminal `bash` (parfois on appelle ça un *shell*)

pour se le procurer

* MacOS et linux: rien à installer
* Windows: je vous recommande d'installer un outil qui s'appelle
`git for windows` , car il a la bonne propriété d'installer un terminal `bash`

  justement; et en plus, ça ne fait pas de mal de pouvoir utiliser `git` , mais
  on s'égare...

  vous trouverez plus de détails et quelques autres recommandations dans le lien suivant, mais c'est optionnel

  https://github.com/ue12-p21/python-primer/blob/next-year/notebooks/2-01-intro.md#installation-de--bash

## miniconda

pour l'installation de Python à proprement parler, je recommande d'installer
`miniconda` , pour plusieurs raisons
* d'abord cela permet ensuite de créer des environnements virtuels; on n'en a pas besoin
  au niveau débutant évidemment, mais comme ça la possibilité est là
* ensuite grâce à conda on peut se sortir de situations périlleuses; pour faire
  très court, les - rares - fois où vous n'arrivez pas à installer un module
  avec `pip install` , vous avez toujours le recours de tenter un `conda install`

pour cette installation, utilisez google pour trouver le support d'installation
de miniconda qui va bien pour votre machine

par rapport à une installation par défaut, voici les 2 ou 3 points qui sont
importants (pour tout le reste, choisissez les réponses qui sont proposées par
défaut)

* si votre dossier principal (votre dossier User) contient un accent ou une
  cédille ou un caractère abscons de ce genre, il est important de créer un dossier
  `c:\miniconda` - dans ce cas-là lisez bien attentivement le lien ci-dessous

* si on vous propose de choisir entre
  + installer pour **tous** les utilisateurs, ou
  + installer **seulement pour vous**
  alors choisissez **seulement pour vous** !

  de cette façon l'installation se fait dans **vos dossiers**, donc vous n'avez
  **pas du tout besoin de droits administrateur** pour faire ça - c'est de loin
  préférable

* aussi et surtout: si à un moment donné on vous demande si vous voulez
  **ajouter miniconda dans la variable PATH** alors c'est important de répondre
  oui à cette question (sinon vous allez avoir le `command not found` )

plus de détails si nécessaire ici:
https://github.com/ue12-p21/python-primer/blob/next-year/notebooks/2-02-outils.md#python
