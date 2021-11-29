from pathlib import Path

path = Path.cwd().parent / "inputs" / "02.txt"

with open(path) as f:
    inp = [[int(i) for i in line.strip().split("x")] for line in f.readlines()]

acc = 0
for l, w, h in inp:
    sides_areas = [l * w, w * h, h * l]
    acc += min(sides_areas)
    for a in sides_areas:
        acc += 2 * a

print(acc)
