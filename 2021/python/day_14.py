import sys
from collections import Counter
from dataclasses import dataclass


Rules = dict[str, str]


@dataclass
class Polymer:
    template: Counter[str]
    counts: Counter[str]

    def step(self, rules: Rules) -> None:
        new_template: Counter[str] = Counter()
        for pair, count in self.template.items():
            new_letter = rules[pair]
            self.counts[new_letter] += count

            left = pair[0] + new_letter
            new_template[left] += count

            right = new_letter + pair[1]
            new_template[right] += count

        self.template = new_template


def parse_template(template: str) -> Polymer:
    poly_template = Counter(template[i - 1 : i + 1] for i in range(1, len(template)))

    return Polymer(poly_template, Counter(template))


def parse_rules(insert_rules: str) -> Rules:
    rules: Rules = {}
    for line in insert_rules.split("\n"):
        inp, out = line.split(" -> ")
        rules[inp] = out

    return rules


def parse_input(inp: str) -> tuple[Polymer, Rules]:
    template, insert_rules = inp.split("\n\n")

    return parse_template(template), parse_rules(insert_rules)


def score(cnt: Counter[str]) -> int:
    most_common = cnt.most_common()
    _, top = most_common[0]
    _, bottom = most_common[-1]
    return top - bottom


def solve(inp: str, steps: int) -> int:
    polymer, rules = parse_input(inp)
    for i in range(steps):
        polymer.step(rules)
    return score(polymer.counts)


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        inp = f.read().strip()

    from time import perf_counter

    st = perf_counter()

    print(solve(inp, 10))
    print(solve(inp, 40))

    end = perf_counter()
    print(f"\nTime elapsed: {end-st}s")
