from pathlib import Path


path = Path.cwd().parent / "inputs" / "01.txt"

with open(path) as f:
    directions = f.read()

floor = 0

for i, c in enumerate(directions):
    floor = floor + 1 if c == "(" else floor - 1
    if floor == -1:
        print(i + 1)
        break
