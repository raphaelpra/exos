# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     cell_metadata_json: true
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   livereveal:
#     height: 1024
#     start_slideshow_at: selected
#     theme: simple
#     transition: cube
#     width: 1280
#   notebookname: Mandelbrot
#   version: '1.0'
# ---

# %% [markdown] {"run_control": {"frozen": false, "read_only": false}}
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% {"run_control": {"frozen": false, "read_only": false}, "slideshow": {"slide_type": "slide"}, "trusted": true}
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib notebook

# %% [markdown] {"run_control": {"frozen": false, "read_only": false}}
# ## exercice
#
# il s'agit de calculer l'image de la convergence de mandelbrot:
#
# <img src="../media/mandelbrot.png" width="2000px">

# %% [markdown] {"cell_style": "split", "run_control": {"frozen": false, "read_only": false}, "slideshow": {"slide_type": "slide"}}
# * dans l'espace complexe où
#    * $re \in [-2, 0.8]$
#    * $im \in [-1.4, 1.4]$
# * on définit pour chaque $c\in\mathbb{C}$ la suite
#    * $z_0 = c$
#    * $z_{n+1} = z_n^2 + c$
# * on démontre que 
#   * lorsque $|z_n|>2$, la suite diverge

# %% [markdown] {"cell_style": "split", "run_control": {"frozen": false, "read_only": false}, "slideshow": {"slide_type": "-"}}
# il s'agit pour nous de 
#
# * découper ce pavé 
#   * en un maillage de $w$ x $h$ points
# * pour chacun, calculer si la suite diverge
#   * avant un nombre d'itérations fixe
# * afficher l'image obtenue avec `plt.imshow`

# %% [markdown] {"run_control": {"frozen": false, "read_only": false}, "slideshow": {"slide_type": "slide"}}
# * une adaptation libre de l'[implementation proposée dans le tutorial scipy](https://docs.scipy.org/doc/numpy/user/quickstart.html#indexing-with-boolean-arrays)

# %% [markdown] {"run_control": {"frozen": false, "read_only": false}, "slideshow": {"slide_type": "slide"}}
# *indices*
#
# * pour fabriquer la grille des points de départ, 
#   on pourra regarder `np.linspace` et `np.meshgrid`

# %% {"trusted": true}
# à vous de jouer
