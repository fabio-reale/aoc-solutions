from pathlib import Path


class Submarine:
    def __init__(self, depth: int, hor: int, aim: int) -> None:
        self.depth = depth
        self.hor = hor
        self.aim = aim


def move(sub: Submarine, ammount: int, direction: str) -> Submarine:
    return Submarine(sub.depth + ammount, sub.hor + sub.aim * ammount, sub.aim)


def new_aim(sub: Submarine, ammount: int, direction: str) -> Submarine:
    dir_sign = 1 if direction == "down" else -1
    return Submarine(sub.depth, sub.hor, sub.aim + dir_sign * ammount)


def parse_command(comm: str) -> tuple[str, int]:
    direction, str_ammount = comm.split()
    return direction, int(str_ammount)


def parse_input(inp: str) -> list[tuple[str, int]]:
    commands = [parse_command(line) for line in inp.split("\n") if line]
    return commands


def execute_commands(comms: list[tuple[str, int]]) -> Submarine:
    accs = {"forward": move, "down": new_aim, "up": new_aim}
    sub = Submarine(0, 0, 0)
    for direction, ammount in comms:
        sub = accs[direction](sub, ammount, direction)
    return sub


def solve(inp: str) -> int:
    commands = parse_input(inp)
    sub = execute_commands(commands)
    return sub.depth * sub.hor


if __name__ == "__main__":
    path = Path(__file__).parents[1] / "inputs" / "day_02.txt"

    with open(path) as f:
        inp = f.read()

    print(solve(inp))
