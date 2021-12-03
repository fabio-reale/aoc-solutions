from __future__ import annotations

from pathlib import Path
from collections import defaultdict


str_counter = list[defaultdict[str, int]]


class Report:
    def __init__(self, bin_strs: list[str]) -> None:
        self.bin_strs = bin_strs
        self.bins: list[int] = []
        self.max_power = len(bin_strs[0])

    def build_bins(self) -> None:
        for bin_str in self.bin_strs:
            num = get_binary_int([c for c in bin_str])
            self.bins.append(num)

    def calculate_rates(self) -> tuple[int, int]:
        gammas: list[str] = []
        epsilons: list[str] = []
        current_power = self.max_power

        while current_power > 0:
            current_power -= 1
            current_split = 2 ** current_power
            splitted: dict[str, list[int]] = {"1": [], "0": []}
            for num in self.bins:
                if num >= current_split:
                    splitted["1"].append(num - current_split)
                else:
                    splitted["0"].append(num)

            if len(splitted["1"]) >= len(splitted["0"]):
                gammas.append("1")
                epsilons.append("0")
            else:
                gammas.append("0")
                epsilons.append("1")

            self.bins = splitted["1"] + splitted["0"]

        gamma = get_binary_int(gammas)
        epsilon = get_binary_int(epsilons)

        return gamma, epsilon


def parse_input(inp: str) -> list[str]:
    return inp.split()


def get_binary_int(bin_str: list[str]) -> int:
    return int("".join(bin_str), 2)


def solve(inp: str) -> int:
    report = Report(parse_input(inp))
    report.build_bins()
    gamma, epsilon = report.calculate_rates()

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
