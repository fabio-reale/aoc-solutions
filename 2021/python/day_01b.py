from pathlib import Path


def solve(inp: str, offset: int) -> int:
    depths = [int(num) for num in inp.split()]

    return sum((d_prev < d_next for d_prev, d_next in zip(depths, depths[offset:])))


if __name__ == "__main__":
    path = Path(__file__).parents[1] / "inputs" / "day_01.txt"

    with open(path) as f:
        inp = f.read()

    print(solve(inp, 3))
