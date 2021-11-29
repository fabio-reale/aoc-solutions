from pathlib import Path
from collections import Counter


path = Path.cwd().parent / "inputs" / "01.txt"

with open(path) as f:
    directions = Counter(f.read())

print(directions["("] - directions[")"])
