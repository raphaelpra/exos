---
jupytext:
  cell_metadata_filter: all, -hidden, -heading_collapsed, -run_control, -trusted
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
  title: Taylor interactif
---

# Taylor (3/3) un dashboard

+++

On se propose d'approximer une fonction par la formule de Taylor

$$f_n(x) = \sum_{i=0}^{n}\frac{f^{(i)}(0).x^i}{i!}$$

```{code-cell} ipython3
# ! pip install autograd
import autograd.numpy as np

from math import factorial
```

## un dashboard

+++

en application de ce qu'on a vu sur les notebooks interactifs, on peut s'amuser à fabriquer un dashboard qui permet d'afficher l'approximation de Taylor pour une fonction f passée en paramètre

le dashboard permet de choisir le degré de l'approximation

avec par exemple les fonctions sinus, cosinus, et exponentielle

+++

cet exercice est tiré du MOOC Python, où on donne en option des indications supplémentaires
