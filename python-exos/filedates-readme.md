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

Exo fichier / format / datetime

+++

# un générateur de date

```{code-cell} ipython3
from filedates import generate_random_date
```

```{code-cell} ipython3
help(generate_random_date)
```

```{code-cell} ipython3
generate_random_date()
```

```{code-cell} ipython3
generate_random_date()
```

## Indices

+++

### ne même pas essayer 

* si vous générez les trois morceaux indépendamment
  * vous n'avez aucune chance d'être uniforme

+++

### le module `random`

```{code-cell} ipython3
# générer un entier dans un intervalle
import random
random.randint(1000, 2000)
```

### le module `datetime`

```{code-cell} ipython3
from datetime import datetime
day = datetime(2000, 3, 1)
day
```

```{code-cell} ipython3
# convertir en entiers (ici des jours, mais peu importe)
i = day.toordinal()
i
```

```{code-cell} ipython3
# et dans l'autre sens
day_after = datetime.fromordinal(i + 2)
day_after
```

### [les formats de date/time](https://docs.python.org/3.5/library/datetime.html#strftime-and-strptime-behavior)

```{code-cell} ipython3
# revenir d'une date à un string
f"{day_after:%d %m %Y}"
```

*****

+++

# écrire *n* échantillons dans un fichier

```{code-cell} ipython3
from filedates import write_random_dates_in_file
```

```{code-cell} ipython3
help(write_random_dates_in_file)
```

```{code-cell} ipython3
with open("dates.txt", 'w') as output:
    write_random_dates_in_file(output, 3)
```

```{code-cell} ipython3
!cat dates.txt
```

# relire le fichier et le trier

```{code-cell} ipython3
from filedates import sort_file_dates
```

```{code-cell} ipython3
help(sort_file_dates)
```

```{code-cell} ipython3
with open("dates.txt") as input:
    sort_file_dates(input)
```

```{code-cell} ipython3
!cat dates.txt.sort
```

## Indices

* on n'a pas d'autre choix que de lire l'entrée en entier avant de trier
  * et de reconstruire un objet `datetime` par ligne
  * pour pouvoir trier proprement et réimprimer 
* un objet fichier a un attribut `name` - [voir doc `io`](https://docs.python.org/3.5/library/io.html#module-io)

```{code-cell} ipython3
with open('dates.txt') as input:
    to_sort = []
    for line in input:
        tokens = line.split()
        day, month, year, *rest, comment = tokens
        date = datetime(int(year), int(month), int(day))
        to_sort.append( (date, rest[0], comment))
    to_sort.sort(key = lambda tuple: tuple[0])
    print(to_sort)
```

# Primer classes

```{code-cell} ipython3
# class définit une classe
# comme def définit une fonction
class Vector2D:

    # ici on définit une méthode spéciale
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # une méthode 
    def produit_scalaire(self, vector):
        return self.x * vector.x + \
               self.y * vector.y
        
v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)
v1, v2
```

```{code-cell} ipython3
v1.produit_scalaire(v2)
```

# Variantes

`filedates_cl.py`

* générez un commentaire random ou lieu de 'bla', fait de 1 a 4 mots choisis dans un dictionnaire

* si vous vous sentez confortable avec les classes, vous pouvez écrire une classe `Sample` pour chaque élément dans le fichier

* écrivez un `if __name__ == '__main__'` pour rendre votre script exécutable
  et utilisez `ArgumentParser` pour paramétrer le nombre de lignes générées

```{code-cell} ipython3
from filedates_cl import write_random_dates_in_file as write_file_dates_cl
```

```{code-cell} ipython3
with open("dates_cl.txt", 'w') as output:
    write_random_dates_in_file_cl(output, 3)
```

```{code-cell} ipython3
!cat dates_cl.txt
```

```{code-cell} ipython3
from filedates_cl import sort_file_dates as sort_file_dates_cl
```

```{code-cell} ipython3
with open("dates_cl.txt") as input:
    sort_file_dates(input)
```
