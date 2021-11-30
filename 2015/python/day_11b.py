from __future__ import annotations
from typing import Optional

from pathlib import Path


def get_next_char_map() -> dict[str, str]:
    next_char: dict[str, str] = {}
    for i in range(ord("a"), ord("z")):
        curr_char = chr(i)
        next_char[curr_char] = chr(i + 1)
    return next_char


def next_candidate(next_char: dict[str, str], pwd: str) -> str:
    if not pwd:
        return "a"
    elif pwd[-1] == "z":
        pwd = pwd[:-1]
        pwd = next_candidate(next_char, pwd)
        pwd += "a"
        return pwd
    else:
        return pwd[:-1] + next_char[pwd[-1]]


def all_valid_chars(pwd: str) -> bool:
    return not ("i" in pwd or "l" in pwd or "o" in pwd)


def any_valid_straight(next_char: dict[str, str], pwd: str) -> bool:
    for fst, snd, trd in zip(pwd, pwd[1:], pwd[2:]):
        if snd == next_char.get(fst) and trd == next_char.get(snd):
            return True
    return False


def non_overlapping_pairs(pwd: str) -> bool:
    found = False
    i = len(pwd)
    while i >= 2:
        fst, snd = pwd[i - 2], pwd[i - 1]
        i -= 1
        if fst == snd:
            if not found:
                found = True
                i -= 1
            else:
                return True

    return False


def valid_pwd(next_char: dict[str, str], pwd: str) -> bool:
    return (
        all_valid_chars(pwd)
        and any_valid_straight(next_char, pwd)
        and non_overlapping_pairs(pwd)
    )


def solve(pwd: str, iterations: int) -> str:
    next_char = get_next_char_map()

    while iterations:
        pwd = next_candidate(next_char, pwd)
        if valid_pwd(next_char, pwd):
            iterations -= 1

    return pwd


assert solve("abcdefgh", 1) == "abcdffaa"
assert solve("ghijklmn", 1) == "ghjaabcc"

if __name__ == "__main__":
    inp_dir = Path(__file__).parents[1] / "inputs"
    path = inp_dir / "11.txt"

    with open(path) as f:
        inp = f.read().strip()

    next_pwd = solve(inp, 2)
    print(next_pwd)
