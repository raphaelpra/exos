from collections import defaultdict
from math import factorial

from typing import Iterator

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

GRAPH_FILENAME = 'puzzle8.pickle'

class Board:
    """
    represents a board of the puzzle8 game
    encoded as a tuple of the 9 integers 0..8
    """
    def __init__(self, array=None):
        if array is None:
            array = GOAL
        self.internal = tuple(array)
        self.h = hash(self.internal)

    def __repr__(self):
        return repr(self.internal)

    def __eq__(self, other):
        return self.internal == other.internal

    def __hash__(self):
        return self.h

    def iter_moves(self):
        zero_index = self.internal.index(0)
        neighbours_indices = NEIGHBOURS[zero_index]
        for neighbour_index in neighbours_indices:
            # use a list so we can alter it
            next = list(self.internal)
            next[zero_index], next[neighbour_index] = (
                next[neighbour_index], next[zero_index])
            yield Board(next)

    @staticmethod
    def from_string(s):
        """
        convenience method to create a Board from a string
        of the form "1 2 3 4 5 6 7 8 0"
        """
        return Board(map(int, s.split()))


class Solver:
    """
    computes the full graph with boards as nodes
    and uses a shortest-path algorithm to find the
    optimal path from a given board to the goal
    """
    def __init__(self):
        self.graph = None

    def nb_nodes(self):
        return len(self.graph)
    def nb_edges(self):
        return sum(len(v) for v in self.graph.values())

    def double_check(self):
        """
        compare graph with calculated number of nodes and edges
        """
        N, E = factorial(9)/2, factorial(8)*12
        assert self.nb_nodes() == N
        assert self.nb_edges() == E

    def compute_full_graph(self, starting_board=None):
        if starting_board is None:
            starting_board = Board()

        queue = list()
        queue.append(starting_board)

        # just to be clean
        self.graph = defaultdict(list)

        while queue:
            scan = queue.pop()
            # an unexplored node may be added twice or more
            if scan in self.graph:
                continue
            for next in scan.iter_moves():
                self.graph[scan].append(next)
                if next not in self.graph:
                    queue.append(next)


def main():
    import time
    begin = time.time()
    solver = Solver()
    solver.compute_full_graph()
    print(f"computed graph in {time.time() - begin} seconds"
          f" with {len(solver.graph)} nodes"
          f" and {solver.nb_edges()} edges")
    solver.double_check()

if __name__ == '__main__':
    main()
