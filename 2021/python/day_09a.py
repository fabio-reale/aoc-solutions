from pathlib import Path

Point = tuple[int, int]
Map = dict[Point, int]


def parse_input(inp: str) -> Map:
    surface_map = {}
    for row, line in enumerate(inp.split()):
        for col, hight in enumerate(line):
            surface_map[row, col] = int(hight)
    return surface_map


def neighbors(point: Point) -> list[Point]:
    r, c = point
    return [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]


def get_basins(surface_map: Map) -> list[Point]:
    basins = []

    for point, hight in surface_map.items():
        neighbor_higher = [
            hight < surface_map.get(point, 10) for point in neighbors(point)
        ]
        if all(neighbor_higher):
            basins.append(point)

    return basins


def get_risk_level(surface_map: Map, basin: Point) -> int:
    return 1 + surface_map[basin]


def solve(inp: str) -> int:
    surface_map = parse_input(inp)
    basins = get_basins(surface_map)

    risk_levels = [get_risk_level(surface_map, b) for b in basins]
    return sum(risk_levels)


TEST = """2199943210
3987894921
9856789892
8767896789
9899965678"""

assert solve(TEST) == 15

if __name__ == "__main__":
    path = Path(__file__).parents[1] / "inputs" / "day_09.txt"

    with open(path) as f:
        inp = f.read()

    print(solve(inp))
