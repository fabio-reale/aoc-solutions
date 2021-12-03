from pathlib import Path
from collections import defaultdict


str_counter = list[defaultdict[str, int]]


def parse_input(inp: str) -> list[str]:
    return inp.split()


def count_cols(bins: list[str]) -> str_counter:
    rows = len(bins)
    cols = len(bins[0])

    counters: str_counter = [defaultdict(int) for _ in range(cols)]
    for row in range(rows):
        for col in range(cols):
            char = bins[row][col]
            counters[col][char] += 1

    return counters


def get_gamma_epsilon(counters: str_counter) -> tuple[int, int]:
    gammas = []
    epsilons = []

    for count in counters:
        if count["1"] > count["0"]:
            gammas.append("1")
            epsilons.append("0")
        else:
            gammas.append("0")
            epsilons.append("1")

    gamma = int("".join(gammas), 2)
    epsilon = int("".join(epsilons), 2)

    return gamma, epsilon


def solve(inp: str) -> tuple[int, int]:
    bins = parse_input(inp)
    counts = count_cols(bins)
    gamma, epsilon = get_gamma_epsilon(counts)

    return gamma * epsilon


TEST_INPUT = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

assert solve(TEST_INPUT) == 198

if __name__ == "__main__":

    path = Path(__file__).parents[1] / "inputs" / "day_03.txt"

    with open(path) as f:
        inp = f.read()

    print(solve(inp))
