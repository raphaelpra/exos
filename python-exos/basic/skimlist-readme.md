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
nbhosting:
  title: filtrer les éléments d'une liste
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
</div>

+++

# filtrer une liste

+++

## filtrage par copie

+++

Il s'agit d'écrire une fonction `all_integers` qui

* accepte en entrée un itérable
* retourne la liste de tous les entiers trouvés dans l'itérable (on ignore le reste)
* bien sûr on les conserve dans l'ordre où on les trouve

```{code-cell} ipython3
# on charge la correction pour afficher des exemples
from skimlist import all_integers
```

```{code-cell} ipython3
inputs = [
    [1, 2, 3, 4, 'spam', 5, [4, 5]],
    [(1, 2), 3, 4, 'spam', 5, 3.],
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

## filtrage par effet de bord

+++

Cette fois on veut une fonction `keep_only_integers` qui

* accepte en entrée une liste
* **modifie cet objet** en entrée pour ne garder que les éléments de type **`int`**

```{code-cell} ipython3
from skimlist import keep_only_integers
```

```{code-cell} ipython3
inputs = [
    [1, 2, 3, 4, 'spam', 5, 'beans'],
    [(1, 2), 3, 4, 'spam', 5, 'beans'],
]
```

```{code-cell} ipython3
for input in inputs:
   print(10*'=')
   print(f"input(avant) = {input}")
   print(f"all_integers = {all_integers(input)}")
   print(f"input(après - intact) = {input}")
   keep_only_integers(input)
   print(f"input(modifié par keep_only_integers) = {input}")
```
