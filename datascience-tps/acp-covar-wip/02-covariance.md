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

<span style="float:left;">Licence CC BY-NC-ND</span><span style="float:right;">Thierry Parmentelat&nbsp;<img src="media/inria-25.png" style="display:inline"></span><br/>

```{code-cell} ipython3
from math import pi, cos, sin, atan, fabs, sqrt
import numpy as np
```

```{code-cell} ipython3
from collections import OrderedDict
```

```{code-cell} ipython3
from ipywidgets import interact, fixed
from ipywidgets import SelectionSlider, IntSlider
```

# Helpers

+++

### Translate a set of points

```{code-cell} ipython3
def translate(points, vector):
    X, Y = points
    x0, y0 = vector
    return X + x0, Y + y0
```

### Rotate a set of points

```{code-cell} ipython3
def rotate(points, alpha):
    x, y = points
    return x*cos(alpha) - y*sin(alpha), x*sin(alpha) + y*cos(alpha)
```

### Get the average (center of gravity)

```{code-cell} ipython3
# for a 1-dimension array
def average1(dim1):
    return sum(dim1)/len(dim1)

def average(points):
    x, y = points
    return average1(x), average1(y)
```

# Generating input : an ellipse

+++

### Centered and not rotated

```{code-cell} ipython3
# the 2 radiuses, plus n as the number of points 
def ellipse(rx, ry, n):
    return (rx * np.cos(2 * pi / n * np.arange(n)),
            ry * np.sin(2 * pi / n * np.arange(n)))
```

```{code-cell} ipython3
el3 = ellipse(3, 1, 100)
```

### How to display a set of points

+++

The optional `directions` argument gives you a way to specify additional lines to be displayed. Each element in the `directions` parameter should be tuple of the form `alpha, length`.

E.g.

    show_points( points, [ (pi/3, 10) ])
    
would cause a line of angle $\pi/3$ and length 10 to be drawn from the center of gravity of the points

```{code-cell} ipython3
%matplotlib notebook
import matplotlib.pyplot as plt

from math import pi, cos, sin

def show_points(points, directions=[]):
    x , y = points
    fig = plt.figure()
    plt.scatter(x, y)
    if directions:
        cx, cy = average(points)
        for alpha, length in directions:
            plt.plot( (cx, cx + length * cos(alpha)),
                      (cy, cy + length * sin(alpha)))
                 
    fig.show()
```

### A rotated and translated ellipse

```{code-cell} ipython3
el3t = translate(el3, (1,2))
```

```{code-cell} ipython3
elr = rotate(el3, pi/6)
show_points(elr, [ (pi/6, 4), [pi/2, 2]])
```

```{code-cell} ipython3
el = translate(rotate(el3, pi/6), (4, 2))
show_points(el)
```

# Generating input : random gaussian

```{code-cell} ipython3
def random_points(sdx, sdy, n):
    return (np.random.normal(0, sdx, n),
            np.random.normal(0, sdy, n))
```

### a sample random cloud

```{code-cell} ipython3
ra100 = random_points(10, 3, 100)
#show_points(ra100)
```

```{code-cell} ipython3
ra = translate(rotate(ra100, pi/6), (10, 20))
# 10 is the standard deviation, so let's be sure the line is long enough
show_points(ra, [ (pi/6, 30)])
```

# Computing covariance matrix

```{code-cell} ipython3
average(el)
```

### The covariance matrix

```{code-cell} ipython3
def covariance(points):
    # translate to the center of gravity
    mx, my = average(points)
    centered = translate(points, (-mx, -my))
    # convert into a np.array if needed
    m = np.array(centered)
    # compute tranposed
    t = np.transpose(m)
    # just multiply both
    return np.dot(m, t)
```

```{code-cell} ipython3
# try it out on our sample ellipse
co = covariance(el)
print(co)
```

### Eigen values

+++

Just use the numpy library to compute its eigen values

```{code-cell} ipython3
lambdas, A = np.linalg.eig(co)
print("Eigen values", lambdas)
print("Matrix", A)
```

# Various attempts

+++

A helper function to see if 2 value are almost equal...

```{code-cell} ipython3
def almost(x1, x2):
    if x1 == 0.:
        return fabs(x2) <= 0.0001
    return fabs((x1-x2)/x1) <= 0.0001
```

This helper function would display the set of points, and then compute the ACP output. If an expected angle is known in advance (like when the set of points has a known pattern), it is displayed as well.

```{code-cell} ipython3
def loopback(points, expected_alpha=None, directions=None):
    x, y = points
    n = len(x)
    co = covariance(points)
    lambdas, A = np.linalg.eig(co)
    # A is expected to be an isometric rotation
    (a11, a12), (a21, a22) = A
    radius = a11*a22 - a12*a21
    if not almost(a11, a22): print("ISOMETRY - WARNING 1")
    if not almost(fabs(a21), fabs(a12)): print("ISOMETRY - WARNING 2")
    if not almost(1., radius): print("ISOMETRY - WARNING 3")
    l1, l2 = lambdas
    print("valeurs propres {:.2f} - {:.2f}".format(l1, l2))
    #print("ACP ->", A)
    computed_alpha = pi/2 if a11 == 0 else atan(a12/a11)
    print("a11={:.3f}, a21={:.3f}".format(a11, a21))
    print("computed alpha = {:.3f}".format(computed_alpha))
    if expected_alpha:
        print("expected_alpha = {:.3f}".format(expected_alpha))
    # show lines as specified by the caller 
    directions = directions or []
    # add the computed one
    directions.append((-computed_alpha, sqrt(l1/n)))
    show_points(points, directions)

#        if not almost(computed_alpha, -expected_alpha):
#            print("MISMATCH")
#        α = expected_alpha
#        print("cos(α) = {}, sin(α) = {}".format(cos(α), sin(α)))
```

###  Synthesized ellipses

```{code-cell} ipython3
def loopback_el(rx, ry, cx, cy, alpha, n):
    e = ellipse(rx, ry, n)
    ert = translate(rotate(e, alpha), (cx, cy))
    # show only one direction
    loopback(ert, alpha, [ (alpha, max(rx, ry)) ])
```

```{code-cell} ipython3
loopback_el_datasets = OrderedDict()
loopback_el_datasets['pi_6'] = (3, 1, 5, 10, pi/6, 100)
loopback_el_datasets['pi_4'] = (5, 1, 20, 30, pi/4, 50)
loopback_el_datasets['pi_3'] = (10, 1, 100, 200, pi/3, 25)
loopback_el_datasets['pi_2'] = (1.2, 1, 100, 200, pi/2, 100)

def loopback_el_wrap(k):
    args = loopback_el_datasets[k]
    print("args = ", args)
    loopback_el(*args)

interact(loopback_el_wrap, 
         k = SelectionSlider(options = list(loopback_el_datasets.keys()),
                             continuous_update = False))
```

### Gaussian distribs

```{code-cell} ipython3
def loopback_ra(cx, cy, sdx, sdy, alpha, n):
    raw = random_points(sdx, sdy,n)
    points = translate(rotate(raw, alpha), (cx, cy))
    loopback(points, alpha, [ (alpha, 3*max(sdx, sdy)) ])
```

#### More and more points

```{code-cell} ipython3
interact(loopback_ra,
         cx = fixed(10), 
         cy = fixed(20),
         sdx = fixed(10),
         sdy = fixed(4),
         alpha = fixed(pi/6),
         n = IntSlider(min=10, max=1000, step=20, continuous_update = False)
        )
```
