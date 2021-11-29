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


def update_scheme(lights: list[list[bool]], comm: Command) -> list[list[bool]]:

    comm_sq = (
        Point(x, y)
        for x in range(comm.from_point.x, 1 + comm.upto_point.x)
        for y in range(comm.from_point.y, 1 + comm.upto_point.y)
    )

    for light in comm_sq:

        if comm.command == "toggle":  # XOR with True to invert
            lights[light.x][light.y] ^= True

        elif comm.command == "turn on":
            lights[light.x][light.y] = True

        elif comm.command == "turn off":
            lights[light.x][light.y] = False

        else:
            raise ValueError(f"unknown command: {comm.command}")

    return lights


def count_on_lights(lights: list[list[bool]]) -> int:
    on_count = 0

    for row in lights:
        for light in row:
            on_count += 1 if light else 0

    return on_count


def solve(inp_str: str) -> int:

    commands = parse_input(inp_str)
    lights: list[list[bool]] = [[False for _ in range(1000)] for _ in range(1000)]

    for command in commands:
        lights = update_scheme(lights, command)

    return count_on_lights(lights)


path = Path.cwd().parent / "inputs" / "06.txt"

with open(path) as f:
    inp = f.read()

print(solve(inp))
