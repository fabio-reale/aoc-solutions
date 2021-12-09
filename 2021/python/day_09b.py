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


def get_basin_size(surface_map: Map, basin: Point) -> int:
    stack = [basin]
    basin_points = set()

    while stack:
        curr_point = stack.pop()
        if curr_point not in basin_points:
            neighbor_points = [
                p for p in neighbors(curr_point) if surface_map.get(p, 9) < 9
            ]
            stack.extend(neighbor_points)
            basin_points.add(curr_point)

    return len(basin_points)


def solve(inp: str) -> int:
    surface_map = parse_input(inp)
    basins = get_basins(surface_map)

    basins_sizes = sorted(get_basin_size(surface_map, b) for b in basins)
    a, b, c = basins_sizes[-3:]
    return a * b * c


TEST = """2199943210
3987894921
9856789892
8767896789
9899965678"""

assert solve(TEST) == 1134

if __name__ == "__main__":
    path = Path(__file__).parents[1] / "inputs" / "day_09.txt"

    with open(path) as f:
        inp = f.read()

    print(solve(inp))
