import sys
from collections import defaultdict


def parse_input(inp: str) -> dict[str, set[str]]:
    incidences = defaultdict(set)

    for line in inp.split():
        a, b = line.split("-")[:2]
        incidences[a].add(b)
        incidences[b].add(a)

    return incidences


def remove_starts(incidences: dict[str, set[str]]) -> None:
    for cave in incidences["start"]:
        incidences[cave].remove("start")


def count_paths(
    incidences: dict[str, set[str]], path: str, next_cave: str, repeat: int
) -> int:
    if next_cave == "end":
        return 1
    elif next_cave.islower() and next_cave in path:
        if repeat:
            return sum(
                count_paths(incidences, path + f"{next_cave}, ", cave, repeat - 1)
                for cave in incidences[next_cave]
            )
        else:
            return 0
    else:
        return sum(
            count_paths(incidences, path + f"{next_cave}, ", cave, repeat)
            for cave in incidences[next_cave]
        )


def solve(inp: str) -> int:
    incidences = parse_input(inp)
    remove_starts(incidences)
    return count_paths(incidences, "", "start", 1)


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        inp = f.read().strip()

    from time import perf_counter

    st = perf_counter()

    print(solve(inp))

    end = perf_counter()
    print(f"\nTime elapsed: {end-st}s")
