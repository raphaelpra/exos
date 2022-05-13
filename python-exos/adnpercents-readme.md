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

# pourcentages

+++ {"run_control": {"frozen": false, "read_only": false}}

En partant d'un string qui représente un brin d'ADN

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
dna = "GGCGCGCCATCGCCGGCTGGCGGAAATT"
```

+++ {"run_control": {"frozen": false, "read_only": false}}

Calculer les deux pourcentages de nucleotides 

 * les `C` ou `G`
 * les `A` ou `T`

+++ {"run_control": {"frozen": false, "read_only": false}}

Imprimez le résultat comme ceci

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
from adnpercents import nice_format
```

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
nice_format(dna)
```

+++ {"run_control": {"frozen": false, "read_only": false}}

* Indices
  * `"{:2f}"` pour écrire un flottant avec deux chiffres significatifs
  * il existe aussi un format `%` ou lieu de `f` qui peut être utile dans ce cas également

+++ {"run_control": {"frozen": false, "read_only": false}}

## variantes

+++ {"run_control": {"frozen": false, "read_only": false}}

Entraînez-vous à utiliser les f-strings lorsque c'est possible

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
f"le brin {dna}"
```

+++ {"run_control": {"frozen": false, "read_only": false}}

# plus compliqué

+++ {"run_control": {"frozen": false, "read_only": false}}

#### À faire peu plus tard (cf. aussi f-strings)

+++ {"run_control": {"frozen": false, "read_only": false}}

Écrire une fonction `format_dna` qui permet à son appelant de spécifier le format de présentation

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
from adnpercents import format_dna
```

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
format_dna(dna, "la chaine {dna} a\n {at} de (A ou T)")
```

+++ {"run_control": {"frozen": false, "read_only": false}}

# à noter aussi

+++ {"run_control": {"frozen": false, "read_only": false}}

Dans la solution, voir l'utilisation de `collections.Counter` pour faire les calculs

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
from adnpercents import percents_at_cg_bis

percents_at_cg_bis(dna)
```
