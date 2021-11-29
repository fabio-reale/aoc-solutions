import re
from typing import NamedTuple

from pathlib import Path


class Point(NamedTuple):
    x: int
    y: int


class Command(NamedTuple):
    command: str
    from_point: Point
    upto_point: Point


def parse_input(inp_str: str) -> list[Command]:

    pattern = re.compile(r"(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)")

    commands = []
    for a, b, c, d, e in pattern.findall(inp_str):
        p1 = Point(int(b), int(c))
        p2 = Point(int(d), int(e))
        commands.append(Command(a, p1, p2))

    return commands


def update_scheme(on_lights: dict[Point, int], comm: Command) -> dict[Point, int]:

    update_const: dict[str, int] = {"turn on": 1, "turn off": -1, "toggle": 2}

    comm_sq = (
        Point(x, y)
        for x in range(comm.from_point.x, 1 + comm.upto_point.x)
        for y in range(comm.from_point.y, 1 + comm.upto_point.y)
    )

    for light in comm_sq:
        brightness = on_lights.get(light, 0) + update_const[comm.command]
        on_lights[light] = brightness if brightness > 0 else 0

    return on_lights


def solve(inp_str: str) -> int:

    commands = parse_input(inp_str)
    on_lights: dict[Point, int] = {}

    for command in commands:
        on_lights = update_scheme(on_lights, command)

    return sum([v for v in on_lights.values()])


path = Path.cwd().parent / "inputs" / "06.txt"

with open(path) as f:
    inp = f.read()

print(solve(inp))
