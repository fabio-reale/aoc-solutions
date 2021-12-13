from __future__ import annotations
from typing import Any

from collections import defaultdict
import sys


class Paper:
    def __init__(self, dot_map: dict[tuple[Any, ...], bool]) -> None:
        self.dot_map = dot_map
        self.max_x = max(d[0] for d in dot_map)
        self.max_y = max(d[1] for d in dot_map)

    def count_dots(self) -> int:
        return sum(self.dot_map.values())

    def fold_x(self, x_val: int) -> None:
        self.max_x = x_val - 1

        new_dot_map = defaultdict(bool)
        for (x, y), b in self.dot_map.items():
            if x != x_val:
                folded_x = x_val - abs(x_val - x)
                new_dot_map[folded_x, y] |= self.dot_map[x, y]

        self.dot_map = new_dot_map

    def fold_y(self, y_val: int) -> None:
        self.max_y = y_val - 1

        new_dot_map = defaultdict(bool)
        for (x, y), b in self.dot_map.items():
            if y != y_val:
                folded_y = y_val - abs(y_val - y)
                new_dot_map[x, folded_y] |= self.dot_map[x, y]

        self.dot_map = new_dot_map

    def fold_paper(self, fold: tuple[str, int]) -> None:
        axis, val = fold
        if axis == "x":
            self.fold_x(val)
        elif axis == "y":
            self.fold_y(val)
        else:
            raise ValueError(f"no axis named {axis}")


def print_paper(paper: Paper) -> None:
    print_map = {True: "#", False: " "}

    for y in range(paper.max_y + 1):
        row = "".join([print_map[paper.dot_map[x, y]] for x in range(paper.max_x + 1)])
        print(row)


def parse_paper(pairs: str) -> Paper:
    paper_dict = defaultdict(bool)
    for pair in pairs.split():
        paper_dict[eval(pair)] = True

    paper = Paper(paper_dict)
    return paper


def parse_folds(fold_comms: str) -> list[tuple[str, int]]:
    folds = []
    for line in fold_comms.split("\n"):
        axis, val = line.split("=")
        folds.append((axis[-1], int(val)))

    return folds


def parse_input(inp: str) -> tuple[Paper, list[tuple[str, int]]]:
    pairs, fold_comms = inp.split("\n\n")

    paper = parse_paper(pairs)
    folds = parse_folds(fold_comms)

    return paper, folds


def solve(inp: str) -> int:
    paper, folds = parse_input(inp)
    count = -1
    for ind, fold in enumerate(folds):
        paper.fold_paper(fold)
        if not ind:
            count = paper.count_dots()
    print_paper(paper)
    return count


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        inp = f.read().strip()

    from time import perf_counter

    st = perf_counter()

    print(solve(inp))

    end = perf_counter()
    print(f"\nTime elapsed: {end-st}s")
