from pathlib import Path
from typing import Optional

from collections import deque


class Circuit:

    operation = {
        "VAL": lambda v1, v2: v1,
        "NOT": lambda v1, v2: 65535 - v1,
        "AND": lambda v1, v2: v1 & v2,
        "OR": lambda v1, v2: v1 | v2,
        "RSHIFT": lambda v1, v2: v1 >> v2,
        "LSHIFT": lambda v1, v2: v1 << v2,
    }

    def __init__(self, rules: deque[list[str]]) -> None:
        self.wire: dict[str, int] = {"->": 0}
        self.rules: deque[list[str]] = deque(rules)

    def get_value(self, ref: str) -> Optional[int]:
        if ref.isnumeric():
            return int(ref)
        else:
            return self.wire.get(ref)

    def add_rule(self, rule: list[str]) -> None:

        op, label, ref1, ref2 = rule

        val1 = self.get_value(ref1)
        val2 = self.get_value(ref2)

        if val1 is not None and val2 is not None:
            self.wire[label] = self.operation[op](val1, val2) % 65536
        else:
            self.rules.append(rule)

    def process(self) -> None:
        while self.rules:
            rule = self.rules.popleft()
            label = rule[1]

            if label not in self.wire:
                self.add_rule(rule)


def parse_input(text: str) -> list[list[str]]:
    return sorted([line.split() for line in text.splitlines()], key=len)


def clean_input(parsed: list[list[str]]) -> deque[list[str]]:
    clean: deque[list[str]] = deque()

    for rule in parsed:

        l = len(rule)
        if l == 3:
            ref1, ref2, label = rule
            op = "VAL"
        elif l == 4:
            op, ref1, ref2, label = rule
        elif l == 5:
            ref1, op, ref2, _, label = rule

        clean.append([op, label, ref1, ref2])

    return clean


def solve(text: str) -> int:
    rules = clean_input(parse_input(text))
    circuit = Circuit(rules)
    circuit.process()

    new_b = circuit.wire["a"]
    rules.appendleft(["VAL", "b", str(new_b), "->"])
    circuit = Circuit(rules)
    circuit.process()

    return circuit.wire["a"]


RAW = """123 -> b
456 -> y
b AND y -> d
b OR y -> e
b LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT b -> a
NOT y -> i"""

assert solve(RAW) == 123


path = Path.cwd().parent / "inputs" / "07.txt"

with open(path) as f:
    inp = f.read()

print(solve(inp))  # 14134
