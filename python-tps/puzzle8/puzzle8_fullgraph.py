from collections import defaultdict

import numpy as np

GOAL = [1, 2, 3, 4, 5, 6, 7, 8, 0]
NEIGHBOURS = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7],
}

# an array containing 10**8, ... 100, 10, 1
DIGITS = np.logspace(8, 0, num=9, base=10, dtype=np.uint64)

class Board:
    def __init__(self, array=None):
        if array is None:
            array = GOAL
        self.array = np.array(array, dtype=np.uint8)
        # caching the hash value allows to speed up
        # the computation of the graph from 50 to 33 seconds
        # also, using to_int rather than hash(str(self.array))
        # allosw to speed it up from 33 to 9 seconds
        self.h = hash(self.to_int())

    def to_int(self):
        """
        useful to speed up hashing
        """
        return np.sum(self.array * DIGITS)

    def __str__(self):
        return str(self.array)

    def __eq__(self, other):
        return np.array_equal(self.array, other.array)

    def __hash__(self):
        return self.h

    def iter_moves(self):
        zero_index = np.where(self.array == 0)[0][0]
        # print(zero_index)
        neighbours_indices = NEIGHBOURS[zero_index]
        for neighbour_index in neighbours_indices:
            board = self.array.copy()
            board[zero_index], board[neighbour_index] = (
                board[neighbour_index], board[zero_index])
            yield Board(board)


class Solver:
    def __init__(self):
        self.graph = defaultdict(list)

    def compute_full_graph(self, starting_board=None):
        if starting_board is None:
            starting_board = Board()

        # FIFO: just use append/pop
        queue = []
        queue.append(starting_board)

        # just to be clean
        self.graph = defaultdict(list)

        while queue:
            next = queue.pop()
            for move in next.iter_moves():
                if move not in self.graph:
                    self.graph[move].append(next)
                    queue.append(move)
