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

# filtrer une liste

+++

Il s'agit d'écrire une fonction `all_integers` qui

* accepte en entrée un itérable
* retourne la liste de tous les entiers trouvés dans l'itérable (on ignore le reste)
* bien sûr on les conserve dans l'ordre où on les trouve

```{code-cell} ipython3
from filterlist import all_integers
```

```{code-cell} ipython3
inputs = [
    [1, 2, 3, 4, 'spam', 5, 'beans'],
    [(1, 2), 3, 4, 'spam', 5, 'beans'],
   ]
```

```{code-cell} ipython3
# remarquez bien que les objets 'input' ne sont pas modifiés
for input in inputs:
   print(10*'=')
   print(f"input(avant0) = {input}")
   print(f"integers = {all_integers(input)}")
   print(f"input(après) = {input}")
```

# filtrage par effet de bord

+++

Cette fois on veut une fonction `keep_only_integers` qui

* accepte en entrée une liste
* modifie cette entrée pour ne garder que les éléments de type **`int`**

```{code-cell} ipython3
from filterlist import keep_only_integers
```

```{code-cell} ipython3
for input in inputs:
   print(10*'=')
   print(f"input(avant0) = {input}")
   print(f"integers = {all_integers(input)}")
   print(f"input(après) = {input}")
   keep_only_integers(input)
   print(f"input(modifié) = {input}")
```

```{code-cell} ipython3
!head -18 filterlist.py
```

```{code-cell} ipython3

```
