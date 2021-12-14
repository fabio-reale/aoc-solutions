import sys
from collections import Counter
from dataclasses import dataclass


Rules = dict[str, str]


@dataclass
class Polymer:
    template: Counter[str]
    last_pair: str

    def step(self, rules: Rules) -> None:
        new_template: Counter[str] = Counter()
        for pair, count in self.template.items():
            new_letter = rules[pair]

            left = pair[0] + new_letter
            new_template[left] += count

            right = new_letter + pair[1]
            new_template[right] += count

        self.template = new_template
        self.last_pair = rules[self.last_pair] + self.last_pair[1]

    def count_letters(self) -> Counter[str]:
        letters: Counter[str] = Counter()
        for pair, count in self.template.items():
            letters[pair[0]] += count

        letters[self.last_pair[1]] += 1
        return letters


def parse_template(template: str) -> Polymer:
    poly_template = Counter(template[i - 1 : i + 1] for i in range(1, len(template)))
    last = template[-2:]

    return Polymer(poly_template, last)


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
    cnt = polymer.count_letters()
    val = score(cnt)
    return val


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        inp = f.read().strip()

    from time import perf_counter

    st = perf_counter()

    print(solve(inp, 10))
    print(solve(inp, 40))

    end = perf_counter()
    print(f"\nTime elapsed: {end-st}s")
