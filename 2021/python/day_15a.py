from __future__ import annotations
from typing import Any, Iterator
import sys
from math import inf

Coord = tuple[int, int]


class Node:
    def __init__(self, risk: int, coord: Coord, dist: int | float = inf) -> None:
        self.risk = risk
        self.coord = coord
        self.dist = dist


class Map:
    def __init__(self, nodes: dict[Coord, Node], shape: tuple[int, int]) -> None:
        self.nodes = nodes
        self.shape = shape

    @classmethod
    def from_string(cls, inp: str) -> Map:
        nodes = {}
        for row, line in enumerate(inp.splitlines()):
            for col, risk_char in enumerate(line):
                nodes[row, col] = Node(int(risk_char), (row, col))

        return cls(nodes, (row, col))


def neighbors(p: Coord, d: dict[Coord, Node]) -> Iterator[Node]:
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    x, y = p
    for a, b in dirs:
        n = (x + a, y + b)
        if n in d:
            yield d[n]


def get_min_dist_node(coords: set[Coord], cave: Map) -> Node:
    return min((cave.nodes[coord] for coord in coords), key=lambda x: x.dist)


def find_min_path(cave: Map) -> int | float:
    cave.nodes[0, 0].dist = 0
    end_node = cave.nodes[cave.shape]
    visited_coords = set()
    to_visit_coords = {(0, 0)}

    while end_node.dist is inf:
        curr_node = get_min_dist_node(to_visit_coords, cave)
        visited_coords.add(curr_node.coord)
        to_visit_coords.remove(curr_node.coord)
        for node in neighbors(curr_node.coord, cave.nodes):
            new_dist = curr_node.dist + node.risk
            if new_dist < node.dist and node.coord not in visited_coords:
                node.dist = new_dist
                to_visit_coords.add(node.coord)

    return end_node.dist


def solve(inp: str) -> int | float:
    cave_map = Map.from_string(inp)
    min_path = find_min_path(cave_map)
    return min_path


if __name__ == "__main__":
    from time import perf_counter

    with open(sys.argv[1], "r") as f:
        inp = f.read().strip()

    st = perf_counter()

    print(solve(inp))

    end = perf_counter()
    print(f"\nTime elapsed: {end-st}s")
