from pathlib import Path

path = Path(__file__).parents[1] / "inputs" / "day_05.txt"


def parse_input(inp: str) -> dict[int, int]:
    fishes = {i: 0 for i in range(9)}
    for fish in map(int, inp.strip().split(",")):
        fishes[fish] += 1
    return fishes


def day(yesterday: dict[int, int]) -> dict[int, int]:
    tomorrow = {i: yesterday[(i + 1) % 9] for i in yesterday}
    tomorrow[6] += yesterday[0]
    return tomorrow


def days(fishes: dict[int, int], num_days: int) -> dict[int, int]:
    for i in range(num_days):
        fishes = day(fishes)

    return fishes


def fish_count(fishes: dict[int, int]) -> int:
    return sum(fishes.values())


def solve(inp: str, num_days: int) -> int:
    fishes = parse_input(inp)
    fishes = days(fishes, num_days)

    return fish_count(fishes)


TEST = "3,4,3,1,2"

assert solve(TEST, 18) == 26
assert solve(TEST, 80) == 5934

with open(path) as f:
    inp = f.read()

print(solve(inp, 256))
