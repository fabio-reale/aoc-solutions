from pathlib import Path
from collections import defaultdict, Counter
from math import copysign


class Vector:
    def __init__(self, st: tuple[int, int], end: tuple[int, int]) -> None:
        self.st = st
        self.end = end
        self.delta = (sign(end[0] - st[0]), sign(end[1] - st[1]))

    def __repr__(self) -> str:
        return f"Vector({self.st}, {self.end})"

    def path_trough(self, space: dict[tuple[int, int], int]) -> None:
        dot = self.st
        while dot != self.end:
            space[dot] += 1
            dot = (dot[0] + self.delta[0], dot[1] + self.delta[1])
        space[dot] += 1


def sign(num: int) -> int:
    if num:
        return int(copysign(1, num))
    return 0


def get_input(teste: bool = False) -> list[str]:
    posfix = "_example" if teste else ""
    path = Path(__file__).parents[1] / "inputs" / f"day_05{posfix}.txt"

    with open(path) as f:
        inp = f.readlines()

    return inp


def parse_input(inp: list[str]) -> list[Vector]:
    vecs = []
    for line in inp:
        st_str, end_str = line.strip().split(" -> ")
        vecs.append(Vector(eval(st_str), eval(end_str)))

    return vecs


def count_overlaps(grid):
    count = Counter(grid.values())
    return sum(count.values()) - count[1]


def solve(test: bool = False):
    inp = get_input(test)
    vecs = parse_input(inp)
    grid = defaultdict(int)
    for vec in vecs:
        vec.path_trough(grid)
    return count_overlaps(grid)


assert solve(True) == 12

if __name__ == "__main__":
    var = solve(False)
    print(var)
