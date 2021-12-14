import sys
from collections import Counter
from dataclasses import dataclass
from typing import Iterator


Seed = str
Rules = dict[str, str]


def parse_template(template: str) -> Iterator[Seed]:
    return (template[i - 1 : i + 1] for i in range(1, len(template)))


def parse_rules(insert_rules: str) -> Rules:
    rules: Rules = {}
    for line in insert_rules.split("\n"):
        inp, out = line.split(" -> ")
        rules[inp] = out

    return rules


def parse_input(inp: str) -> tuple[Iterator[Seed], Rules]:
    template, insert_rules = inp.split("\n\n")
    seeds = parse_template(template)
    rules = parse_rules(insert_rules)

    return seeds, rules


def get_count(seed: Seed, iterations: int, rules: Rules) -> Counter[str]:
    new_letter = rules[seed]
    if not iterations:
        return Counter(seed[0] + new_letter)

    left = get_count(seed[0] + new_letter, iterations - 1, rules)
    right = get_count(new_letter + seed[1], iterations - 1, rules)

    return left + right


def get_last(seed: Seed, iterations: int, rules: Rules) -> Counter[str]:
    if not iterations:
        return Counter(seed[1])

    return get_last(rules[seed] + seed[1], iterations - 1, rules)


def score(cnt: Counter[str]) -> int:
    most_common = cnt.most_common()
    _, top = most_common[0]
    _, bottom = most_common[-1]
    return top - bottom


def solve(inp: str, steps: int) -> int:
    polymer, rules = parse_input(inp)
    cnt: Counter[str] = Counter()
    for p in polymer:
        cnt += get_count(p, steps - 1, rules)

    val = score(cnt + get_last(p, steps - 1, rules))
    return val


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        inp = f.read().strip()

    from time import perf_counter

    st = perf_counter()

    print(solve(inp, 10))

    end = perf_counter()
    print(f"\nTime elapsed: {end-st}s")
