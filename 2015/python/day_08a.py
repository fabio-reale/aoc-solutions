import re

from pathlib import Path


def convert_escaped(str_lit: str) -> str:
    pattern = r'(\\\\|\\"|\\x[0-9abcdef]{2})'
    return re.sub(pattern, "?", str_lit)


def solve(inp_str: str) -> int:
    return sum(
        [
            len(str_lit) - len(convert_escaped(str_lit[1:-1]))
            for str_lit in inp_str.split()
        ]
    )


RAW = r'''""
"abc"
"aaa\"aaa"
"\x27"'''

assert solve(RAW) == 12  # (2-0) + (5-3) + (10-7) + (6-1)


path = Path.cwd().parent / "inputs" / "08.txt"

with open(path) as f:
    inp = f.read()

print(solve(inp))
