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

# random-generated but not orthogonal

```{code-cell} ipython3
import numpy as np
```

Generating a numpy-matrix of couples of an ellipse

```{code-cell} ipython3
def random_points(sdx, sdy, n):
    X, Y = np.random.normal(0, sdx, n), np.random.normal(0, sdy, n)
    return np.concatenate( (X, Y)).reshape(2, n)
```

```{code-cell} ipython3
np_ellipse = random_points(10, 5, 5000)
print(np_ellipse)
```

```{code-cell} ipython3
%matplotlib inline
from matplotlib import pyplot as plt
```

```{code-cell} ipython3
plt.plot(np_ellipse[0], np_ellipse[1], 'bx')
plt.axis('equal')
plt.show()
```

## applying a non-isometric linear transformation

+++

Now instead of taking this as-is, we will apply a non-isometric transformation first:

* (1, 0) -> (1, 0)
* (0, 1) -> (1, 1)

```{code-cell} ipython3
twist = np.array([1, 1, 0, 1]).reshape(2, 2)
```

```{code-cell} ipython3
# checking
print(np.dot(twist, [1, 0]))
print(np.dot(twist, [0, 1]))
```

```{code-cell} ipython3
np_twisted = twist.dot(np_ellipse)
```

```{code-cell} ipython3
plt.plot(np_twisted[0], np_twisted[1], 'bx')
plt.axis('equal')
plt.show()
```

## Running the ACP on that

```{code-cell} ipython3
e = np_twisted
```

```{code-cell} ipython3
C = np.cov(e)
print(C)
```

```{code-cell} ipython3
eigen, A = np.linalg.eig(C)
print(eigen)
print(A)
```

```{code-cell} ipython3
roots = np.sqrt(eigen)
v1 = roots[0] * np.array( [1, 0])
v2 = roots[1] * np.array( [0, 1])
r1 = A.dot(v1)
r2 = A.dot(v2)
```

```{code-cell} ipython3
plt.plot(np_twisted[0], np_twisted[1], 'bx')
plt.axis('equal')
plt.plot( (0, r1[0]), (0, r1[1]), 'r-')
plt.plot( (0, r2[0]), (0, r2[1]), 'g-')
plt.show()
```
