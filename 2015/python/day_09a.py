from typing import NamedTuple
from pathlib import Path


class Rout(NamedTuple):
    rout: list[str]
    length: int


class TravelingSanta(NamedTuple):
    locs: set[str]
    dists: dict[frozenset[str], int]


def santa_from_text(text: str) -> TravelingSanta:
    dists: dict[frozenset[str], int] = {}
    locs: set[str] = set()

    for line in text.splitlines():
        dest_a, _, dest_b, _, dist = line.split()
        line_locs = {dest_a, dest_b}
        locs.update(line_locs)
        dists[frozenset(line_locs)] = int(dist)

    return TravelingSanta(locs, dists)


def recursive_all_paths(santa: TravelingSanta, curr: Rout) -> list[Rout]:
    assert curr.rout != [], "recursive_all_paths needs a starting point"

    # base of recursion: return singleton list of current Rout
    if len(santa.locs) == len(curr.rout):
        return [curr]

    # get list of possible next pair
    #    dists whose keys contain last elem of x and an elem not in x
    latest_city = curr.rout[-1]
    visited_cities = set(curr.rout)
    routs_from_curr = []
    for pair, dist in santa.dists.items():
        if visited_cities.intersection(set(pair)) == {latest_city}:
            (new_city,) = pair - {latest_city}
            new_rout = Rout(curr.rout + [new_city], curr.length + dist)
            routs_from_curr.extend(recursive_all_paths(santa, new_rout))

    return routs_from_curr


def recursive_paths(santa: TravelingSanta) -> list[Rout]:
    routs: list[Rout] = []

    for city in santa.locs:
        routs.extend(recursive_all_paths(santa, Rout([city], 0)))

    return routs


def solve(text: str) -> int:
    santa = santa_from_text(text)
    routs = recursive_paths(santa)

    min_rout = min(routs, key=lambda r: r.length)
    return min_rout.length


test_inp = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""

assert solve(test_inp) == 605

path = Path.cwd().parent / "inputs" / "09.txt"

with open(path) as f:
    inp = f.read()

print(solve(inp))
