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

```{code-cell} ipython3
%matplotlib notebook
from matplotlib import pyplot as plt
import numpy as np

def ellipse (cx, cy, rx, ry, n):
    return [cx + rx*np.cos(2*np.pi*i/n) for i in range(n)], \
           [cy + ry*np.sin(2*np.pi*i/n) for i in range(n)]

def rotate (points, alpha):
    x, y = points
    return ([ x*np.cos(alpha) - y*np.sin(alpha) for (x, y) in zip(x, y)],
            [ x*np.sin(alpha) + y*np.cos(alpha) for (x, y) in zip(x, y)])


e = ellipse(0, 0, 5, 2, 100)
alpha = np.pi/5
re = rotate(e, alpha)
plt.plot(*re, 'bx')
plt.axis('equal')
plt.show()
```

```{code-cell} ipython3
re_cov = np.cov(re)
print('matrice de co-variance:\n {} \n'.format(re_cov))
```

```{code-cell} ipython3
lambdas, A = np.linalg.eig(re_cov)
print("Valeurs propres {}\n".format(lambdas))
print("Matrice de rotation\n", A)
```

Là je prends les racines carrées des valeurs propres; en fait les valeurs propres ici sont homogènes à des variances, donc à des écart-types au carré..

```{code-cell} ipython3
r_lambdas = np.sqrt(lambdas)
```

Je prends comme vecteurs d'entrée $i$ et $j$ et je les multiplie par les racines carrées des valeurs propres:

```{code-cell} ipython3
v1 = r_lambdas[0] * np.array([1, 0])
v2 = r_lambdas[1] * np.array([0, 1])
```

Et maintenant j'applique la rotation, les points r1 et r2 sont les deux que je vais vouloir tracer:

```{code-cell} ipython3
r1 = A.dot(v1)
r2 = A.dot(v2)
```

Maintenant je retrace l'ellipse, avec les deux points en question

```{code-cell} ipython3
plt.plot(*re, 'bx')
plt.axis('equal')
plt.plot( (0, r1[0]), (0, r1[1]), 'r-')
plt.plot( (0, r2[0]), (0, r2[1]), 'g-')
plt.show()
```

```{code-cell} ipython3

```
