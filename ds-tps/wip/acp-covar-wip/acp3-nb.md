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

# ACP in 3D

```{code-cell} ipython3
import numpy as np

from math import pi, cos, sin
```

### A rotation matrix in 3D

```{code-cell} ipython3
teta1 = pi / 3
A1 = np.array( [[cos(teta1), sin(teta1), 0],
                [-sin(teta1), cos(teta1), 0],
                [0 , 0, 1]])
```

```{code-cell} ipython3
teta2 = pi / 4
A2 = np.array( [[1, 0, 0],
                [0, cos(teta2), sin(teta2)],
                [0, -sin(teta2), cos(teta2)]])
```

```{code-cell} ipython3
rot = A1.dot(A2)
```

### An ellipsoid

+++

Generating a numpy-matrix of triples of an ellipsiod

```{code-cell} ipython3
def random_points(sdx, sdy, sdz, n):
    X = np.random.normal(0, sdx, n)
    Y = np.random.normal(0, sdy, n)
    Z = np.random.normal(0, sdz, n)
    return np.concatenate( (X, Y, Z)).reshape(3, n)
```

```{code-cell} ipython3
np_ellipsoid = random_points(10, 5, 2, 5000)
```

```{code-cell} ipython3
%matplotlib ipympl
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
```

```{code-cell} ipython3
def show_points(ax, np_3d):
    X, Y, Z = np_3d[0], np_3d[1], np_3d[2]
    ax.scatter(X, Y, Z)
    max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.0
    mid_x = (X.max()+X.min()) * 0.5
    mid_y = (Y.max()+Y.min()) * 0.5
    mid_z = (Z.max()+Z.min()) * 0.5
    # artificially enlarge
    max_range = max_range / 2.0
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)
```

```{code-cell} ipython3
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
show_points(ax, np_ellipsoid)
plt.show()
```

## applying a non-isometric linear transformation

+++

Now instead of taking this as-is, we will apply a non-isometric transformation first:

* i -> i + j
* j -> - i + j
* k -> -5i + -j + k

```{code-cell} ipython3
twist = np.array([1, -1, -5, 1, 1, -1, 0, 0, 1]).reshape(3, 3)
```

```{code-cell} ipython3
# checking
print(np.dot(twist, [1, 0, 0]))
print(np.dot(twist, [0, 1, 0]))
print(np.dot(twist, [0, 0, 1]))
```

**This actually does not work too well, let's use a real rotation**

```{code-cell} ipython3
np_twisted = rot.dot(np_ellipsoid)
```

```{code-cell} ipython3
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
show_points(ax, np_twisted)
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
v1 = roots[0] * np.array( [1, 0, 0])
v2 = roots[1] * np.array( [0, 1, 0])
v3 = roots[1] * np.array( [0, 0, 1])
r1 = A.dot(v1)
r2 = A.dot(v2)
r3 = A.dot(v3)
```

```{code-cell} ipython3
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
show_points(ax, np_twisted)
ax.plot( (0, r1[0]), (0, r1[1]), (0, r1[2]) , 'r-')
ax.plot( (0, r2[0]), (0, r2[1]), (0, r2[2]) , 'g-')
ax.plot( (0, r3[0]), (0, r3[1]), (0, r3[2]) , 'yellow')
plt.show()
```
