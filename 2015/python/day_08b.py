import re

from pathlib import Path


def convert_escaped(str_lit: str) -> str:
    pattern = r'(\\|")'
    return re.sub(pattern, r"\\\1", str_lit)


def solve(inp_str: str) -> int:
    return sum(
        [
            len(convert_escaped(str_lit)) - len(str_lit) + 2
            for str_lit in inp_str.split()
        ]
    )


RAW = r'''""
"abc"
"aaa\"aaa"
"\x27"'''

assert solve(RAW) == 19  # (6-2) + (9-5) + (16-10) + (11-6)


path = Path.cwd().parent / "inputs" / "08.txt"

with open(path) as f:
    inp = f.read()

print(solve(inp))
