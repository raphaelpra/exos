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

+++ {"run_control": {"frozen": false, "read_only": false}}

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
</div>

+++ {"run_control": {"frozen": false, "read_only": false}}

# Exercice 'langage d'expressions'

+++ {"run_control": {"frozen": false, "read_only": false}}

## Objectif

On veut implémenter un langage d'expressions.

+++ {"run_control": {"frozen": false, "read_only": false}}

Considérant une expression comme 

$27 * (43 + 12)$

+++ {"run_control": {"frozen": false, "read_only": false}}

On construit un objet comme ceci

```
exp = Mult(Number(27), Plus(Number(43), Number(12)))
```

+++ {"run_control": {"frozen": false, "read_only": false}}

Sur lequel on veut disposer d'une méthode `eval`

+++ {"run_control": {"frozen": false, "read_only": false}}

```
>>> exp.eval()
1485
```

+++ {"run_control": {"frozen": false, "read_only": false}}

## Sujet 

* on vous demande d'écrire les classes `Mult`, `Plus`, `Power` et `Number`
* il ne s'agit **PAS** de parser un string comme `27 * (43 + 12)`

+++ {"run_control": {"frozen": false, "read_only": false}}

## Variante 'pretty'

* améliorer la présentation des expressions

```
>>> exp = Mult(Number(27), Plus(Number(43), Number(12)))
>>> print(exp)
Mult [[N 27] * Plus [[N 43] + [N 12]]]
```

+++ {"run_control": {"frozen": false, "read_only": false}}

## Variante 'variables'

Ajout de variables

+++ {"run_control": {"frozen": false, "read_only": false}}

Ajouter les classes `Variable`et `NameSpace` de façon à pouvoir faire ceci

+++ {"run_control": {"frozen": false, "read_only": false}}

```
expression = Mult(Variable('x'), Plus(Variable('y'), Number(34)))
environnement = NameSpace(x = 12, y = 45)
expression.eval(namespace)
```

+++ {"run_control": {"frozen": false, "read_only": false}}

En gardant la compatibilité, c'est-à dire qu'on veut toujours pouvoir faire
```
Mult(Number(27), Plus(Number(43))).eval()
```

+++ {"run_control": {"frozen": false, "read_only": false}}

Pour faire simple on peut admettre qu'une variable non définie s'évalue à 0
```
>>> Variable('x').eval()
0
```

+++ {"run_control": {"frozen": false, "read_only": false}}

## Variante 'number-not-required'

Supprimer l'étage `Nombre`

+++ {"run_control": {"frozen": false, "read_only": false}}

Étudiez vos options pour simplifier la vie de l'appelant pour lui permettre d'écrire simplement

```
expression = Mult('x', Plus('y', 34))
```
