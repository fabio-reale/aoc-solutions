from __future__ import annotations
from pathlib import Path


class Board:
    def __init__(self, cinquinas: list[set]) -> None:
        self.cinquinas = cinquinas

    def __repr__(self) -> str:
        return str(self.cinquinas)

    def is_full_match(self, seq: set[int]) -> bool:
        for cinquina in self.cinquinas:
            if cinquina == cinquina.intersection(seq):
                return True
        return False

    def score(self, seq: set[int], last_call: int) -> int:
        unmarked = 0
        for cinquina in self.cinquinas[:5]:
            unmarked += sum(cinquina - seq)
        return unmarked * last_call

    @staticmethod
    def from_list(lst: list[list[int]]) -> Board:
        cinquinas = [set(row) for row in lst]
        cinquinas.extend(list(map(set, zip(*lst))))

        return Board(cinquinas)


class Bingo:
    def __init__(self, numbers: list[int], boards: list[Board]) -> None:
        self.numbers = numbers
        self.boards = boards

    def __repr__(self) -> str:
        boards = "\n".join(map(str, self.boards))
        return f"numbers: {self.numbers}\n\nboards: {boards}"

    def find_winner(self) -> tuple[list[int], Board]:
        left = len(self.numbers) // 2
        right = len(self.numbers)
        seq = set(self.numbers[:left])
        losers = self.boards

        while right - left > 0:
            next_losers = [loser for loser in losers if not loser.is_full_match(seq)]
            if next_losers:
                left = 1 + (left + right) // 2
                losers = next_losers
            else:
                left, right = left // 2, left
            seq = set(self.numbers[:left])

        return self.numbers[:left], losers[0]


def get_input(test: bool = False) -> str:
    posfix = "_example" if test else ""
    path = Path(__file__).parents[1] / "inputs" / f"day_04{posfix}.txt"

    with open(path) as f:
        inp = f.read()

    return inp


def parse_numbers(nums_str: str) -> list[int]:
    return [int(num) for num in nums_str.split(",")]


def parse_board(b_str: str) -> list[list[int]]:
    return [
        [int(num) for num in line.strip().split(" ") if num]
        for line in b_str.split("\n")
        if line
    ]


def parse_input(inp: str) -> tuple[list[int], list[list[list[int]]]]:
    nums_str, *boards_str = inp.split("\n\n")
    numbers = parse_numbers(nums_str)
    boards = list(map(parse_board, boards_str))

    return numbers, boards


def solve(test: bool = False) -> int:
    inp = get_input(test=test)
    numbers, list_boards = parse_input(inp)
    boards = [Board.from_list(b) for b in list_boards]
    bingo = Bingo(numbers, boards)
    called, winning_board = bingo.find_winner()
    score = winning_board.score(set(called), called[-1])

    return score


assert solve(test=True) == 1924

if __name__ == "__main__":
    solutions = solve(test=False)
    print(solutions)
