from typing import Optional
from pathlib import Path


class Seq:
    open_chars = set("<[{(")
    close_map = {">": "<", "]": "[", "}": "{", ")": "("}
    ilegal_points = {">": 25137, "]": 57, "}": 1197, ")": 3, None: 0}

    def __init__(self, seq: str) -> None:
        self.seq = seq

    def __repr__(self) -> str:
        return f"Seq( {self.seq} )"

    def find_ilegal_char(self) -> Optional[str]:
        stack = []

        for char in self.seq:
            if char in self.open_chars:
                stack.append(char)
            elif stack[-1] == self.close_map[char]:
                stack.pop()
            else:
                return char

        return None


def parse_input(inp: str) -> list[str]:
    return inp.split()


def solve(inp: str) -> int:
    parsed = parse_input(inp)
    seqs = list(map(Seq, parsed))
    ilegal_total = 0
    for seq in seqs:
        ilegal_total += seq.ilegal_points[seq.find_ilegal_char()]

    return ilegal_total


if __name__ == "__main__":
    path = Path(__file__).parents[1] / "inputs" / "day_10.txt"

    with open(path) as f:
        inp = f.read().strip()

    print(solve(inp))
