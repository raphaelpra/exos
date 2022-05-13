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

# filtrer une liste

+++ {"run_control": {"frozen": false, "read_only": false}}

Il s'agit d'écrire une fonction `all_integers` qui

* accepte en entrée un itérable
* retourne la liste de tous les entiers trouvés dans l'itérable (on ignore le reste)
* bien sûr on les conserve dans l'ordre où on les trouve

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
from filterlist import all_integers
```

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
inputs = [
    [1, 2, 3, 4, 'spam', 5, 'beans'],
    [(1, 2), 3, 4, 'spam', 5, 'beans'],
   ]
```

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
# remarquez bien que les objets 'input' ne sont pas modifiés
for input in inputs:
   print(10*'=')
   print(f"input(avant0) = {input}")
   print(f"integers = {all_integers(input)}")
   print(f"input(après) = {input}")
```

+++ {"run_control": {"frozen": false, "read_only": false}}

# filtrage par effet de bord

+++ {"run_control": {"frozen": false, "read_only": false}}

Cette fois on veut une fonction `keep_only_integers` qui

* accepte en entrée une liste
* modifie cette entrée pour ne garder que les éléments de type **`int`**

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
from filterlist import keep_only_integers
```

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
for input in inputs:
   print(10*'=')
   print(f"input(avant0) = {input}")
   print(f"integers = {all_integers(input)}")
   print(f"input(après) = {input}")
   keep_only_integers(input)
   print(f"input(modifié) = {input}")
```

```{code-cell} ipython3
---
run_control:
  frozen: false
  read_only: false
---
!head -18 filterlist.py
```

```{code-cell} ipython3

```
