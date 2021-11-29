from pathlib import Path

path = Path(__file__).parents[1] / "inputs" / "xpto.txt"

with open(path) as f:
    inp = f.read()
