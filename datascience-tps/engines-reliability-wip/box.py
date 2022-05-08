import numpy as np
from itertools import product
from k3d.platonic import PlatonicSolid

# contrary to k3d's Cube class, we decide to build with 
# origin begin ONE CORNER and not the center rof the box
# so this means that
# Cube(origin=[1, 1, 1], size=1)
# is equivalent to
# Box(corner=[0, 0, 0], sizes=[2, 2, 2])
# or
# Box(corner=[2, 2, 2], sizes=[-2, -2, -2])

class Box(PlatonicSolid):
    def __init__(self, corner=[0, 0, 0], sizes=[1, 1, 1]):
        corner = np.array(corner, dtype=np.float32)

        if corner.shape == (3,):
            cube_vertices = np.array(list(product([0, 1], [0, 1], [0, 1])), np.float32)
            cube_vertices = np.float32(sizes * cube_vertices + corner)

            self.vertices = cube_vertices
            self.indices = [0, 1, 2, 1, 2, 3, 0, 1, 4, 1, 4, 5, 1, 3, 5, 3, 5, 7, 0, 2, 4, 2, 4, 6, 2, 3, 7, 2, 6, 7, 4,
                            5, 6, 5, 6, 7]

        else:
            raise TypeError('Origin attribute should have 3 coordinates.')
