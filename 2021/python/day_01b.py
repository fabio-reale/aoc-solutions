from pathlib import Path

path = Path(__file__).parents[1] / "inputs" / "day_01.txt"

with open(path) as f:
    inp = f.read()

depths = [int(num) for num in inp.split()]

increments = 0
for d_prev, d_next in zip(depths, depths[3:]):
    if d_prev < d_next:
        increments += 1

print(increments)
