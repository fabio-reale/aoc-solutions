import re
from pathlib import Path

path = Path(__file__).parents[1] / "inputs" / "12.txt"

with open(path) as f:
    inp = f.read()

print(sum(map(int, re.findall(r'-?\d+', inp))))