from pathlib import Path
from collections import defaultdict, Counter


class Vector:
    def __init__(self, st: tuple[int, int], end: tuple[int, int]) -> None:
        self.st = st
        self.end = end

    def __repr__(self) -> str:
        return f"Vector({self.st}, {self.end})"

    def is_hor(self) -> bool:
        return self.st[1] == self.end[1]

    def is_ver(self) -> bool:
        return self.st[0] == self.end[0]

    def path_trough(self, space: dict[tuple[int, int], int]) -> None:

        if self.is_hor():
            step = 1 if self.st[0] < self.end[0] else -1
            for x in range(self.st[0], self.end[0] + step, step):
                space[x, self.st[1]] += 1
        elif self.is_ver():
            step = 1 if self.st[1] < self.end[1] else -1
            for y in range(self.st[1], self.end[1] + step, step):
                space[self.st[0], y] += 1


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


assert solve(True) == 5

if __name__ == "__main__":
    var = solve(False)
    print(var)
