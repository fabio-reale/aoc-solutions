from pathlib import Path


def parse_command(comm: str) -> tuple[str, int]:
    direction, str_ammount = comm.split()
    return direction, int(str_ammount)


def parse_input(inp: str) -> list[tuple[str, int]]:
    commands = [parse_command(line) for line in inp.split("\n") if line]
    return commands


def accumulate_commands(comms: list[tuple[str, int]]) -> dict[str, int]:
    accs = {"forward": 0, "down": 0, "up": 0}
    for direction, ammount in comms:
        accs[direction] += ammount
    return accs


def solve(inp: str) -> int:
    commands = parse_input(inp)
    accs = accumulate_commands(commands)
    depth = accs["down"] - accs["up"]
    return depth * accs["forward"]


if __name__ == "__main__":
    path = Path(__file__).parents[1] / "inputs" / "day_02.txt"

    with open(path) as f:
        inp = f.read()

    print(solve(inp))
