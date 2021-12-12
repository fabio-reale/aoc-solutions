from __future__ import annotations

from typing import Iterator, NamedTuple, Any
from pathlib import Path
import itertools as it


class Point(NamedTuple):
    row: int
    col: int

    def __add__(self, other: Any) -> Point:
        if isinstance(other, Point):
            return Point(self.row + other.row, self.col + other.col)
        else:
            raise TypeError(f"argument must be instance of Point, was {type(other)}")


def print_octopi(points: dict[Point, int]) -> None:
    print()
    for row in range(10):
        print("".join([str(points[Point(row, col)]) for col in range(10)]))
    print()


def parse_line(line: str) -> list[int]:
    return list(map(int, line))


def parse_input(inp: str) -> dict[Point, int]:
    points = {}
    for row, line in enumerate(inp.split()):
        for col, char in enumerate(line):
            point = Point(row, col)
            points[point] = int(char)
    return points


def neighbors(point: Point) -> Iterator[Point]:
    for x in it.product(range(-1, 2), repeat=2):
        if x != (0, 0):
            yield point + Point(*x)


def increase(points: dict[Point, int]) -> tuple[dict[Point, int], set[Point]]:
    flash = set()
    new_points = {}

    for point, value in points.items():
        if value >= 9:
            flash.add(point)
            new_points[point] = 0
        else:
            new_points[point] = value + 1

    return new_points, flash


def step(points: dict[Point, int]) -> dict[Point, int]:
    increased, flash = increase(points)

    while flash:
        point = flash.pop()

        for neighbor in neighbors(point):
            neighbor_value = increased.get(neighbor, 0)
            if neighbor_value >= 9:
                flash.add(neighbor)
                increased[neighbor] = 0
            elif neighbor_value:
                increased[neighbor] += 1

    return increased


def count_flashes(points: dict[Point, int]) -> int:
    return len(list(it.filterfalse(lambda x: x, points.values())))


def solve(inp: str) -> int:
    octopi = parse_input(inp)

    for c in it.count(start=1):
        octopi = step(octopi)
        flashes = count_flashes(octopi)
        if flashes == 100:
            break

    return c


if __name__ == "__main__":
    path = Path(__file__).parents[1] / "inputs" / "day_11.txt"

    with open(path) as f:
        inp = f.read()

print(solve(inp))
