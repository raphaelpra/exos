---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  cell_metadata_json: true
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
notebookname: indexation & slicing
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>UE 12</span>
<span><img src="media/ensmp-25-alpha.png" /></span>
</div>

+++

# TP simple avec des images

merci à Wikipedia et à stackoverflow

**vous n'allez pas faire ici de traitement d'image  
on se sert d'images pour égayer des exercices avec `numpy`  
(et parce que quand on se trompe: on le voit)**

+++

**Notions intervenant dans ce TP**

* création, indexation, slicing, modification  de `numpy.ndarray`
* affichage d'image (RBG, RGB-A, niveaux de gris)
* lecture de fichier `jpg`
* les autres notions utilisées sont rappelées (très succinctement)

**N'oubliez pas d'utiliser le help en cas de problème.**

+++

## import des librairies

+++

1. Importez la librairie `numpy`
1. Importez la librairie `matplotlib.pyplot`  
ou toute autre librairie d'affichage que vous aimez et/ou savez utiliser, e.g.`seaborn`...

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

import numpy as np
from matplotlib import pyplot as plt

import seaborn as sns
```

3. choisissez le mode d'affichage `notebook` de matplotlib

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

%matplotlib notebook
```

4. (optionnel): changez la taille par défaut des figures matplotlib; par exemple un carré de 4x4 (en théorie ce sont des inches)

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

plt.rc('figure', figsize=(4, 4))
```

## création d'une image de couleur

+++

**Rappels (rapides)**

* dans une image en couleur, les pixels sont représentés par leurs *dosages* dans les 3 couleurs primaires: `red`, `green`, `blue` (RGB)  
* si le pixel vaut `(r, g, b) = (255, 0, 0)`, il ne contient que de l'information rouge, il est affiché comme du rouge
* l'affichage à l'écran, d'une image couleur `rgb`, utilise les règles de la synthèse additive  
`(r, g, b) = (255, 255, 255)` donne la couleur blanche  
`(r, g, b) = (0, 0, 0)` donne la couleur noire  
`(r, g, b) = (255, 255, 0)` donne la couleur jaune ...
<img src='media/synthese-additive.png' width=200>
* pour afficher le tableau `im` comme une image, utilisez: `plt.imshow(im)`
* pour afficher plusieurs images dans une même cellule de notebook faire `plt.show()` après chaque `plt.imshow(...)`

+++

**Exercices**

1. Créez un tableau blanc, de 91 pixels de côté, d'entiers non-signés 8 bits et affichez-le  
   indices:  
   . le tableau n'est pas forcément initialisé à ce stade  
   . il vous faut pouvoir stocker 3 uint8 par pixel pour ranger les 3 couleurs

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

# 1.
img = np.empty(shape=(91, 91, 3), dtype=np.uint8)*255 # RGB

# important avec le mode %matplotlib notebook
plt.figure()
plt.imshow(img);

# optionnel avec le mode %matplotlib notebook
#plt.show()
```

2. Transformez le en tableau noir (en un seul slicing) et affichez-le

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

# 2.
img[:, :, :] = 0

plt.figure()
plt.imshow(img);
```

3. Transformez le en tableau jaune (en un seul slicing) et affichez-le

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

# 3.
img[:, :, 0:2] = 255
plt.figure()
plt.imshow(img);
```

4. Affichez les valeurs RGB du premier pixel de l'image, et du dernier

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

# 4.
print(img[0, 0, :])

# on peut omettre la dernière coordonnée
print(img[-1, -1])
```

5. faites un quadrillage dans une autre couleur - par exemple cyan c'est-à-dire 0, 255, 255 - de 1 ligne sur 10 et 1 colonne sur 10

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

# 5.
# pour illustrer plusieurs façons de faire
# les lignes: avec un slicing
img[::10, :, 0] = 0
img[::10, :, 1:] = 255

# ou tout le triplet d'un coup
img[:, ::10] = (0, 255, 255)

plt.figure()
plt.imshow(img);
```

6. utilisez le code de 4. pour vérifier les valeurs des pixels aux coins  
   pensez à copier-coller les cellules du notebook avec (en mode édition)  
   * 'c' pour copier
   * 'v' pour coller
   * 'D' et 'U' pour descendre/monter la·les cellules·s sélectionnée·s

+++

## lecture d'une image en couleur

+++

1. Avec la fonction `plt.imread` lisez le fichier `data/les-mines.jpg`  
ou toute autre image - *faites juste attention à la taille*

```{code-cell} ipython3
filename = 'data/les-mines.jpg'

# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

img = plt.imread(filename)
```

2. Vérifiez si l'objet est modifiable avec `im.flags.writeable`  
si il ne l'est pas copiez-le

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

print(img.flags.writeable)
img = img.copy()
print(img.flags.writeable)
```

3. Affichez l'image

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

plt.figure()
plt.imshow(img);
```

```{code-cell} ipython3
# votre code
```

4. Quel est le type de l'objet créé ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

print(type(img))
```

5. Quelle est la dimension de l'image ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

print(img.ndim)
```

6. Quelle est la taille de l'image en hauteur et largeur ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

print(img.shape[0], img.shape[1])
# ou encore
print(img.shape[:-1])
```

7. Quel est le nombre d'octets utilisé par pixel ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

print(img.itemsize)
```

8. Quel est le type des pixels ?  
(deux types pour les pixels: entiers non-signés 8 bits ou flottants sur 64 bits)

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

print(img.dtype)
```

9. Quelles sont ses valeurs maximale et minimale des canaux des pixels ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

print(img.min(), img.max())
```

10. Affichez le rectangle de 10 x 10 pixels en haut de l'image

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:scrolled: false
:tags: [level_basic]

# prune-cell

plt.figure()
plt.imshow(img[:10, :10, :]);
```

## accès à des parties d'image

+++

1. Relire l'image

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

img = plt.imread(filename)
```

2. Slicer et afficher l'image en ne gardant qu'une ligne et qu'une colonne sur 2, 5, 10 et 20  
(ne dupliquez pas le code)

**[indices]]**
* vous pouvez créer plusieurs figures depuis une seule cellule
* vous pouvez ensuite choisir de 'replier' ou non la zone *output* en hauteur;  
  c'est-à-dire d'afficher soit toute la hauteur, soit une zone de taille fixe avec une scrollbar pour naviguer  
  pour cela cliquez dans la marge gauche de la zone *output*

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:scrolled: true
:tags: [level_basic]

# prune-cell

for n in (2, 5, 10, 20):
    print(f"un pixel sur {n}")
    plt.figure()
    plt.imshow(img[::n, ::n, :]);


print("---")
# prune-cell
```

3. Isoler le rectangle de `lig` lignes et `col` colonnes en milieu d'image  
affichez-le pour `(lig, col) = (10, 20)` puis `(lig, col) = (100, 200)`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

for (lig, col) in ((10, 20), (100, 200)):
    print(f"centre de taille {lig} x {col}")
    ml = img.shape[0] // 2 - lig//2
    mc = img.shape[1] // 2 - col//2
    plt.figure()
    plt.imshow(img[ml:ml+lig, mc:mc+col, :])
```

4. Affichez le dernier pixel de l'image

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:scrolled: false
:tags: [level_basic]

# prune-cell

# avec ou sans le dernier slice
print(img[-1:, -1:])
plt.figure()
plt.imshow(img[-1:, -1:, :]);
```

## canaux rgb de l'image

+++

1. Relire l'image

```{code-cell} ipython3
filename = 'data/les-mines.jpg'

# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

img = plt.imread(filename)
```

2. Découpez l'image en ses trois canaux Red, Green et Blue

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]
```

3. Afficher chaque canal avec `plt.imshow`  
    La couleur est-elle la couleur attendue ?  
    Si oui très bien, si non que se passe-t-il ?
    
    **[indice]** table des couleurs
    * `RGB` représente directement l'encodage de la couleur du pixel  
    et non un indice dans une table
    * donc pour afficher des pixel avec les 3 valeurs RGB pas besoin de tables de couleurs  
    on a déjà la couleur
    * mais pour afficher une image unidimensionnelle contenant des nombres de `0` à `255`  
    il faut bien lui dire à quoi correspondent les valeurs  
    (lors de l'affichage, le `255` des rouges n'est pas le même `255` des verts)
    * donner le paramètre `cmap=` à `plt.imshow`, `'Reds'`,  `'Greens'` ou  `'Blues'`

Corrigez vos affichages si besoin

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

# version naïve

print('le canal R sans colormap')
plt.figure()
plt.imshow(R);
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

# on rectifie

print('le canal R avec colormap')
plt.figure()
plt.imshow(R, cmap='Reds')
```

```{code-cell} ipython3
:scrolled: false
:tags: [level_basic]

# prune-cell

# les 3 canaux
print('les 3 canaux avec colormap')
for (channel, cmap) in (R, 'Reds'), (G, 'Greens'), (B, 'Blues'):
    plt.figure()
    plt.imshow(channel, cmap)
```

4. Copiez l'image, remplacer dans la copie:
  * un carré de taille `(200, 200)` en bas à droite, par
  * A. un carré de couleur RGB avec R à 219, G à 112 et B à 147 (vous obtenez quelle couleur)  
  * B. puis par un carré blanc avec des rayures horizontales rouges de 1 pixel

```{code-cell} ipython3
# votre code A.
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

img1 = img.copy()

lig, col = 200, 200

# v1 - un peu pédestre
img1[-lig:, -col:, 0] = 230
img1[-lig:, -col:, 1] = 112
img1[-lig:, -col:, 2] = 147
plt.figure()
plt.imshow(img1);
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

img1 = img.copy()

# v2 - plus pythonique
img1[-lig:, -col:] = (230, 112, 147)
plt.figure()
plt.imshow(img1);
```

```{code-cell} ipython3
# votre code B.
# pensez à zoomer si nécessaire pour bien voir la différence
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

img1 = img.copy()

img1[-lig::2, -col:] = 255         # par broadcasting <=> (255, 255, 255)
img1[-lig+1::2, -col:] = 255, 0, 0
plt.figure()
plt.imshow(img1);
```

5. enfin affichez les 20 dernières lignes et colonnes du carré à rayures

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:scrolled: false
:tags: [level_basic]

# prune-cell

plt.figure()
plt.imshow(img1[-20:, -20:]);
```

## transparence des images

+++

**rappel** RGB-A

* on peut indiquer, dans une quatrième valeur des pixels, leur transparence
* ce 4-ème canal s'appelle le canal alpha
* les valeurs vont de `0` pour transparent à `255` pour opaque

+++

1. Relire l'image initiale (sans la copier)

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

img = plt.imread(filename)
```

2. Créez un tableau vide de la même hauteur et largeur que l'image, du type de l'image initiale, avec un quatrième canal

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

imga = np.empty(shape=(img.shape[0], img.shape[1], 4), dtype=img.dtype)
# ou encore pour les geeks
# imga = np.empty(shape=(*img.shape[:2], 4), dtype=img.dtype)
```

3. Copiez-y l'image initiale, mettez le quatrième canal à `128` et affichez l'image

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

imga[:, :, 0:3] = img
imga[:, :, 3] = 128
plt.figure()
plt.imshow(imga);
```

## image en niveaux de gris en `float`

+++

1. Relire l'image `les-mines.jpg`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

img = plt.imread(filename)

# prune-cell
```

2. Passez ses valeurs en flottants entre 0 et 1 et affichez-la  

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

plt.title('q2: flottant entre 0 et 1')
imgf = img/255
plt.figure()
plt.imshow(imgf);
```

3. Transformer l'image en deux images en niveaux de gris :   
A. en mettant pour chaque pixel la moyenne de ses valeurs R, G, B  
B. en utilisant la correction 'Y' (qui corrige le constrate) basée sur la formule  
   G = $0.299\,R + 0.587\,V + 0.114\,B\,$

```{code-cell} ipython3
# votre code A.
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

plt.figure()
plt.title("q3.1: niveaux de gris (moyenne)")
gr = (imgf[:, :, 0] + imgf[:, :, 1] + imgf[:, :, 2])/3


# pour les geeks; par contre il semble que c'est plus lent...
gr = (imgf[:, :, :].sum(axis=2))/3
plt.imshow(gr, cmap='gray');
```

```{code-cell} ipython3
# votre code B.
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

plt.figure()
plt.title('q3.2: niveaux de gris (correction Y)')
grY = 0.299*imgf[:, :, 0] + 0.587*imgf[:, :, 1] + 0.114*imgf[:, :, 2]
plt.imshow(grY, cmap='gray');
```

4. Passez au carré les pixels (de la question A. ci-dessus) et affichez l'image

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

plt.figure()
plt.imshow(np.power(gr, 2), cmap='gray')
plt.title('q4: au carré');
```

5. Appliquez la racine carrée - toujours à la sortie de l'exercice A. - affichez-la

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

plt.figure()
plt.title('q5: racine carrée')
plt.imshow(np.sqrt(gr), cmap='gray');
```

6. Convertissez l'image de niveaux de gris en type entier non-signé 8 bits et affichez la en niveaux de gris

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:scrolled: false

# prune-cell

plt.figure()
plt.title('q6: en uint8')
gr8 = (gr*255).astype(np.uint8)
plt.imshow(gr8, cmap='gray');
```

```{code-cell} ipython3
:tags: [raises-exception, level_intermediate]

%%timeit 
# prune-cell

gr = (imgf[:, :, 0] + imgf[:, :, 1] + imgf[:, :, 2])/3
```

```{code-cell} ipython3
:tags: [raises-exception, level_intermediate]

%%timeit
# prune-cell

# pour les geeks
gr = (imgf[:, :, :].sum(axis=2))/3
```

# affichage grille de figures

+++

Affichage en `matplotlib.pyplot` de plusieurs figures sur une grille

**1) on créé une figure globale et des sous-figures**

les sous-figures sont appelées `axes` par convention `matplotlib`

on construit notre grille ici de 2 lignes et 3 colonnes

```python
fig, axes = plt.subplots(2, 3)
print(type(axes))
print(axes.shape)
```

les cases pour les sous-figures sont ici dans la variable `axes`  
qui est un `numpy.ndarray` de taille 2 lignes et 3 colonnes

**2) on affiche des sous-figure dans des cases de la grille**

```python
x = np.linspace(0, 2*np.pi, 50)
axes[0, 0].plot(x, np.sin(x), 'b')
axes[0, 1].plot(x, np.sin(x), 'r')
axes[0, 2].plot(x, np.sin(x), 'y')
axes[1, 0].plot(x, np.sin(x), 'k')
axes[1, 1].plot(x, np.sin(x), 'g')
axes[1, 2].plot(x, np.sin(x), 'm')
```

**3) on peut faire un peu de cosmétique mais**  
quand on commence on ne s'arrête plus et on perd beaucoup de temps  
préférez au début des affichages minimalistes à peu près lisibles
```python
fig.suptitle("sinus en couleur", fontsize=20) # titre général
axes[0, 0].set_title('sinus bleu')            # titre d'une sous-figure
axes[0, 2].set_xlabel('de 0 à 2 pi')          # label des abscisses
axes[1, 1].set_ylabel('de -1 à 1')            # label d'ordonnées
axes[1, 2].set_title('sinus magenta')
plt.tight_layout()                            # ajustement automatique des paddings
```
</div>

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

# le code
fig, axes = plt.subplots(2, 3, figsize=(8, 4))
print(type(axes))
print(axes.shape)

x = np.linspace(0, 2*np.pi, 50)

axes[0, 0].plot(x, np.sin(x), 'b')
# axes[0, 1].plot(x, np.sin(x), 'r')
axes[0, 2].plot(x, np.sin(x), 'y')
axes[1, 0].plot(x, np.sin(x), 'k')
axes[1, 1].plot(x, np.sin(x), 'g')
axes[1, 2].plot(x, np.sin(x), 'm')

fig.suptitle("sinus en couleur", fontsize=20)
axes[0, 0].set_title('sinus bleu')
axes[0, 2].set_xlabel('de 0 à 2 pi')
axes[1, 1].set_ylabel('de -1 à 1')
axes[1, 2].set_title('sinus magenta')
plt.tight_layout()
```

# reprenons le TP

+++

Reprenez les trois images en niveau de gris que vous aviez produites ci-dessus:  
  A: celle obtenue avec la moyenne des rgb  
  B: celle obtenue avec la correction Y  
  C: celle obtenue avec la racine carrée

1. Affichez les trois images côte à côte
   A B C

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

# gr, grY et grS

grA, grB, grC = gr, grY, np.sqrt(gr)

# pas besoin de plt.figure() car subplots crée une figure
fig, axes = plt.subplots(1, 3, figsize=(10, 3))
fig.suptitle('côte à côte')

axes[0].imshow(grA, cmap='gray')
axes[0].set_title('moyenne')
axes[1].imshow(grB, cmap='gray')
axes[1].set_title('corr. Y')
axes[2].imshow(grC, cmap='gray')
axes[2].set_title('racine');
```

```{code-cell} ipython3
:tags: [level_basic]

# prune-cell

# une version alternative avec un unpacking à la place

# pas besoin de plt.figure() car subplots crée une figure
fig, (ax_lef, ax_mid, ax_rig) = plt.subplots(1, 3, figsize=(10, 3))
fig.suptitle('côte à côte')

ax_lef.imshow(grA, cmap='gray')
ax_lef.set_title('moyenne')
ax_mid.imshow(grB, cmap='gray')
ax_mid.set_title('corr. Y')
ax_rig.imshow(grC, cmap='gray')
ax_rig.set_title('racine');
```

+++ {"tags": ["level_intermediate"]}

2. Affichez-les en damier:  
   A B C  
   C A B  
   B C A  

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:tags: [level_intermediate]

# prune-cell

images = [grA, grB, grC]
titles = ['moyenne', 'corr. Y', 'racine']

fig, axes = plt.subplots(3, 3, figsize=(9, 9))
fig.suptitle('en damier')
fig.tight_layout()

for i in range(3):
    for j in range(3):
        index = (i-j)%3
        image = images[index]
        title = titles[index]
        axes[i, j].imshow(image, cmap='gray')
        axes[i, j].set_title(title)
plt.show()
```

***
