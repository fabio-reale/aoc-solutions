from pathlib import Path


path = Path.cwd().parent / "inputs" / "02.txt"
with open(path) as f:
    inp = [[int(i) for i in line.strip().split("x")] for line in f.readlines()]

acc = 0
for l, w, h in inp:
    acc += l * w * h + min([2 * l + 2 * w, 2 * w + 2 * h, 2 * h + 2 * l])

print(acc)
