from __future__ import annotations

import sys
import ast
from dataclasses import dataclass
from collections import deque


@dataclass
class Snail:
    val: int
    depth: int


def magnitude_reduce(snails: deque[Snail], max_depth: int) -> None:
    i = 0
    while i < len(snails) - 1:
        snail_l = snails[i]
        if snail_l.depth == max_depth:
            snail_r = snails[i + 1]
            reduced_val = 3 * snail_l.val + 2 * snail_r.val
            snails[i] = Snail(reduced_val, max_depth - 1)
            snails.remove(snail_r)
        i += 1


def magnitude(snails: deque[Snail]) -> int:
    mags = snails.copy()
    for i in range(3, -1, -1):
        magnitude_reduce(mags, i)
    return mags[0].val


def explode(snails: deque[Snail]) -> bool:
    for i in range(len(snails) - 1):
        snail_l = snails[i]
        snail_r = snails[i + 1]
        if snail_l.depth == snail_r.depth == 4:
            if i + 2 < len(snails):
                snails[i + 2].val += snail_r.val
            if i:
                snails[i - 1].val += snail_l.val
            snails.remove(snail_r)
            snails[i] = Snail(0, 3)
            return True
    return False


def split(snails: deque[Snail]) -> bool:
    for i in range(len(snails)):
        snail = snails[i]
        if snail.val > 9:
            split_val = snail.val // 2
            snail_l = Snail(split_val, snail.depth + 1)
            snails[i] = Snail(split_val + (snail.val % 2), snail.depth + 1)
            snails.insert(i, snail_l)
            return True
    return False


def reduce_snail(snails: deque[Snail]) -> None:
    exploded = True
    splitted = False
    while exploded or splitted:
        exploded = explode(snails)
        if not exploded:
            splitted = split(snails)
        else:
            splitted = False


def join_snails(snails_l: deque[Snail], snails_r: deque[Snail]) -> deque[Snail]:
    joined = snails_l + snails_r
    for snail in joined:
        snail.depth += 1
    reduce_snail(joined)
    return joined


def print_snails(snails: deque[Snail]) -> None:
    for snail in snails:
        t = "--" * snail.depth
        print(f"{t}>{snail.val}")


def list_to_snails(lst: list, depth: int = 0) -> deque[Snail]:

    l, r = lst[0], lst[1]
    if isinstance(l, int):
        snails = deque([Snail(l, depth)])
    else:
        snails = list_to_snails(l, depth + 1)
    if isinstance(r, int):
        snails.append(Snail(r, depth))
    else:
        snails.extend(list_to_snails(r, depth + 1))

    return snails


def parse_input(inp: str) -> list[list]:
    return [ast.literal_eval(line) for line in inp.split("\n")]


def solve(inp: str) -> int:
    parsed = parse_input(inp)
    snails = [list_to_snails(v) for v in parsed]
    snail = snails[0]
    for next_snail in snails[1:]:
        snail = join_snails(snail, next_snail)

    print_snails(snail)
    return magnitude(snail)  # POP POP


if __name__ == "__main__":
    from time import perf_counter

    with open(sys.argv[1], "r") as f:
        inp = f.read().strip()

    st = perf_counter()

    print(solve(inp))

    end = perf_counter()
    print(f"\nTime elapsed: {end-st}s")
