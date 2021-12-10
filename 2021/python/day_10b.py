from typing import Optional
from pathlib import Path


class Seq:
    open_chars = set("<[{(")
    close_map = {">": "<", "]": "[", "}": "{", ")": "("}
    open_map = {"<": ">", "[": "]", "{": "}", "(": ")"}
    char_points = {">": 4, "]": 2, "}": 3, ")": 1}

    def __init__(self, seq: str) -> None:
        self.seq = seq

    def __repr__(self) -> str:
        return f"Seq( {self.seq} )"

    def is_legal(self) -> tuple[bool, list[str]]:
        stack = []

        for char in self.seq:
            if char in self.open_chars:
                stack.append(char)
            elif stack[-1] == self.close_map[char]:
                stack.pop()
            else:
                return False, []

        return True, stack

    def complete_seq(self, opens: list[str]) -> str:
        completion = [self.open_map[char] for char in reversed(opens)]
        return "".join(completion)

    def score_seq(self) -> Optional[int]:
        check, opens = self.is_legal()
        if check:
            complement = self.complete_seq(opens)
            score = 0
            for char in complement:
                score = 5 * score + self.char_points[char]
            return score
        else:
            return None


def find_median(lst: list[int]) -> int:
    index = len(lst) // 2
    return sorted(lst)[index]


def parse_input(inp: str) -> list[str]:
    return inp.split()


def solve(inp: str) -> int:
    parsed = parse_input(inp)
    seqs = list(map(Seq, parsed))
    incomplete_scores = []
    for seq in seqs:
        score = seq.score_seq()
        if score is not None:
            incomplete_scores.append(score)

    return find_median(incomplete_scores)


if __name__ == "__main__":
    path = Path(__file__).parents[1] / "inputs" / "day_10.txt"

    with open(path) as f:
        inp = f.read().strip()

    print(solve(inp))
