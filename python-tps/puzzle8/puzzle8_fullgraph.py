from collections import defaultdict

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
    def __init__(self, array=None):
        if array is None:
            array = GOAL
        self.internal = tuple(array)
        self.h = hash(self.internal)

    def __str__(self):
        return str(self.internal)

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

def main():
    import time
    begin = time.time()
    solver = Solver()
    solver.compute_full_graph()
    print(f"computed graph in {time.time() - begin} seconds"
          f" with {len(solver.graph)} nodes")

if __name__ == '__main__':
    main()
