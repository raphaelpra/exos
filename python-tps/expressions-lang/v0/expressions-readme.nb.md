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

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
</div>

+++

# Exercice 'langage d'expressions'

+++

## Objectif

On veut implémenter un langage d'expressions.

+++

Considérant une expression comme 

$27 * (43 + 12)$

+++

On construit un objet comme ceci

```
exp = Mult(Number(27), Plus(Number(43), Number(12)))
```

+++

Sur lequel on veut disposer d'une méthode `eval`

+++

```
>>> exp.eval()
1485
```

+++

## Sujet 

* on vous demande d'écrire les classes `Mult`, `Plus`, `Power` et `Number`
* il ne s'agit **PAS** de parser un string comme `27 * (43 + 12)`

+++

## Variante 'pretty'

* améliorer la présentation des expressions

```
>>> exp = Mult(Number(27), Plus(Number(43), Number(12)))
>>> print(exp)
Mult [[N 27] * Plus [[N 43] + [N 12]]]
```

+++

## Variante 'variables'

Ajout de variables

+++

Ajouter les classes `Variable`et `NameSpace` de façon à pouvoir faire ceci

+++

```
expression = Mult(Variable('x'), Plus(Variable('y'), Number(34)))
environnement = NameSpace(x = 12, y = 45)
expression.eval(namespace)
```

+++

En gardant la compatibilité, c'est-à dire qu'on veut toujours pouvoir faire
```
Mult(Number(27), Plus(Number(43))).eval()
```

+++

Pour faire simple on peut admettre qu'une variable non définie s'évalue à 0
```
>>> Variable('x').eval()
0
```

+++

## Variante 'number-not-required'

Supprimer l'étage `Nombre`

+++

Étudiez vos options pour simplifier la vie de l'appelant pour lui permettre d'écrire simplement

```
expression = Mult('x', Plus('y', 34))
```
