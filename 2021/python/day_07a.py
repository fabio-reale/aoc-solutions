from pathlib import Path


def parse_input(inp: str) -> list[int]:
    return eval(f"[{inp}]")


def calculate_fuel(crabs: list[int], pos: int) -> int:
    return sum([abs(crab - pos) for crab in crabs])


def search_min_fuel(crabs: list[int], min_pos: int, max_pos: int) -> int:
    avg_pos = (min_pos + max_pos) // 2

    min_fuel = calculate_fuel(crabs, min_pos)
    avg_fuel = calculate_fuel(crabs, avg_pos)
    max_fuel = calculate_fuel(crabs, max_pos)

    if min_pos + 1 == max_pos:
        return min(min_fuel, max_fuel)
    elif min_fuel < avg_fuel < max_fuel:
        return search_min_fuel(crabs, min_pos, avg_pos)
    elif min_fuel > avg_fuel > max_fuel:
        return search_min_fuel(crabs, avg_pos, max_pos)
    else:
        return min(
            search_min_fuel(crabs, min_pos, avg_pos),
            search_min_fuel(crabs, avg_pos, max_pos),
        )


def solve(inp: str) -> int:
    crabs = parse_input(inp)
    return search_min_fuel(crabs, min(crabs), max(crabs))


TEST = "16,1,2,0,4,2,7,1,2,14"
assert solve(TEST) == 37

path = Path(__file__).parents[1] / "inputs" / "day_07.txt"

with open(path) as f:
    inp = f.read().strip()

print(solve(inp))
