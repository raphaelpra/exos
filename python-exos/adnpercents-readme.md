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

# pourcentages

+++

En partant d'un string qui représente un brin d'ADN

```{code-cell} ipython3
dna = "GGCGCGCCATCGCCGGCTGGCGGAAATT"
```

Calculer les deux pourcentages de nucleotides 

 * les `C` ou `G`
 * les `A` ou `T`

+++

Imprimez le résultat comme ceci

```{code-cell} ipython3
from adnpercents import nice_format
```

```{code-cell} ipython3
nice_format(dna)
```

* Indices
  * `"{:2f}"` pour écrire un flottant avec deux chiffres significatifs
  * il existe aussi un format `%` ou lieu de `f` qui peut être utile dans ce cas également

+++

## variantes

+++

Entraînez-vous à utiliser les f-strings lorsque c'est possible

```{code-cell} ipython3
f"le brin {dna}"
```

# plus compliqué

+++

#### À faire peu plus tard (cf. aussi f-strings)

+++

Écrire une fonction `format_dna` qui permet à son appelant de spécifier le format de présentation

```{code-cell} ipython3
from adnpercents import format_dna
```

```{code-cell} ipython3
format_dna(dna, "la chaine {dna} a\n {at} de (A ou T)")
```

# à noter aussi

+++

Dans la solution, voir l'utilisation de `collections.Counter` pour faire les calculs

```{code-cell} ipython3
from adnpercents import percents_at_cg_bis

percents_at_cg_bis(dna)
```
