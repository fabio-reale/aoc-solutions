from pathlib import Path


def parse_input(inp: str) -> list[list[str]]:
    lines = inp.split("\n")
    return [line.split()[-4:] for line in lines]


def filter_1478(digs: list[str]) -> list[str]:
    return [dig for dig in digs if len(dig) in {2, 3, 4, 7}]


def solve(inp: str) -> int:
    digits = parse_input(inp)
    filtered_digits = list(map(filter_1478, digits))
    return sum(map(len, filtered_digits))


if __name__ == "__main__":
    path = Path(__file__).parents[1] / "inputs" / "day_08.txt"

    with open(path) as f:
        inp = f.read().strip()

    print(solve(inp))
