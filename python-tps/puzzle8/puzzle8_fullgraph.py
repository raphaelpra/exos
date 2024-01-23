"""
This module implements a solver for the puzzle8 game
"""

from typing import Iterator
from collections import defaultdict
from math import factorial

from queue import PriorityQueue
from dataclasses import dataclass, field

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

    @staticmethod
    def from_string(s):
        """
        convenience method to create a Board from a string
        of the form "1 2 3 4 5 6 7 8 0"
        """
        return Board(map(int, s.split()))

    def __repr__(self):
        return repr(self.internal)

    # make Board hashable
    def __eq__(self, other):
        return self.internal == other.internal

    def __hash__(self):
        return self.h

    def iter_moves(self) -> Iterator['Board']:
        zero_index = self.internal.index(0)
        neighbours_indices = NEIGHBOURS[zero_index]
        for neighbour_index in neighbours_indices:
            # use a list so we can alter it
            next = list(self.internal)
            next[zero_index], next[neighbour_index] = (
                next[neighbour_index], next[zero_index])
            yield Board(next)


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

    # for using in PriorityQueue
    @dataclass(order=True)
    class Item:
        priority: int
        board: Board = field(compare=False)

    def solve_details(self, from_board, goal) -> tuple[
                        dict[Board, Board],
                        dict[Board, int]]:
        """
        computes the details of scanning for the shortest path
        in the graph from from_board to goal

        it outputs 2 dictionaries:
        - came_from: a dictionary of the form {board: previous_board}
          that allows to rebuild the path
        - cost_so_far: a dictionary of the form {board: cost} which gives the
          shortest path from from_board for all nodes encountered during the
          search note that passing goal=None will scan the whole connected
          component reachable from from_board from from_board
        """

        frontier = PriorityQueue()
        frontier.put(self.Item(0, from_board))

        came_from = {from_board: None}
        cost_so_far = {from_board: 0}
        came_from[from_board] = None
        cost_so_far[from_board] = 0

        while not frontier.empty():
            current = frontier.get().board

            # passsing an unreachable goal (like e.g. None) will scan the whole
            # connected component reachable from from_board
            if current == goal:
                break

            for next in self.graph[current]:
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost
                    frontier.put(self.Item(priority, next))
                    came_from[next] = current
        return came_from, cost_so_far

    def solve(self, from_board, goal=None) -> tuple[float, list[Board]]:
        """
        computes the (one) shortest path in the graph from
        from_board to goal which defaults to
        (1, 2, 3, 4, 5, 6, 7, 8, 0)
        """
        if goal is None:
            goal = Board()

        came_from, cost_so_far = self.solve_details(from_board, goal)
        current = goal
        path = []
        if goal not in came_from:
            return float("inf"), path
        while current != from_board:
            path.append(current)
            current = came_from[current]
        path.append(from_board)
        path.reverse()
        return cost_so_far[goal], path


def main():
    import time
    begin = time.time()
    solver = Solver()
    solver.compute_full_graph()
    print(f"computed graph in {time.time() - begin} seconds"
          f" with {len(solver.graph)} nodes"
          f" and {solver.nb_edges()} edges")
    solver.double_check()
    begin = time.time()
    s1 = Board.from_string("1 2 3 4 5 6 0 7 8")  # d = 2
    s2 = Board.from_string("8 6 7 5 0 1 3 2 4")  # d = 30
    u1 = Board.from_string("6 1 7 4 5 2 3 8 0")  # d = infinity
    for s in (s1, s2, u1):
        print(f"computing path from {s} to {GOAL}")
        d, path = solver.solve(s)
        print(f"found {d=} {path=} in {time.time() - begin} seconds")

if __name__ == '__main__':
    main()
