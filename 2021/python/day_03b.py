from __future__ import annotations

from pathlib import Path
from collections import defaultdict


str_counter = list[defaultdict[str, int]]


class Report:
    def __init__(self, bin_strs: list[str]) -> None:
        self.bin_strs = bin_strs
        self.bins_o2: list[int] = []
        self.bins_co2: list[int] = []
        self.max_power = len(bin_strs[0])

    def build_bins(self) -> None:
        for bin_str in self.bin_strs:
            num = get_binary_int([c for c in bin_str])
            self.bins_o2.append(num)
            self.bins_co2.append(num)

    def filter_o2(self) -> None:
        current_power = self.max_power - 1
        current_split = 2 ** current_power

        while len(self.bins_o2) > 1:
            splitted: dict[bool, list[int]] = {True: [], False: []}
            for num in self.bins_o2:
                splitted[num >= current_split].append(num)

            current_power -= 1
            if len(splitted[True]) >= len(splitted[False]):
                self.bins_o2 = splitted[True]
                current_split += 2 ** current_power
            else:
                self.bins_o2 = splitted[False]
                current_split -= 2 ** current_power

    def filter_co2(self) -> None:
        current_power = self.max_power - 1
        current_split = 2 ** current_power

        while len(self.bins_co2) > 1:
            splitted: dict[bool, list[int]] = {True: [], False: []}
            for num in self.bins_co2:
                splitted[num >= current_split].append(num)

            current_power -= 1
            if len(splitted[True]) < len(splitted[False]):
                self.bins_co2 = splitted[True]
                current_split += 2 ** current_power
            else:
                self.bins_co2 = splitted[False]
                current_split -= 2 ** current_power


def parse_input(inp: str) -> list[str]:
    return inp.split()


def get_binary_int(bin_str: list[str]) -> int:
    return int("".join(bin_str), 2)


def solve(inp: str) -> int:
    report = Report(parse_input(inp))
    report.build_bins()
    report.filter_o2()
    report.filter_co2()

    return report.bins_o2[0] * report.bins_co2[0]


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

test_report = Report(parse_input(TEST_INPUT))
test_report.build_bins()
print("O2 filters:")
test_report.filter_o2()
print()

print("CO2 filters:")
test_report.filter_co2()
print()

assert solve(TEST_INPUT) == 230

if __name__ == "__main__":

    path = Path(__file__).parents[1] / "inputs" / "day_03.txt"

    with open(path) as f:
        inp = f.read()

    print(solve(inp))
