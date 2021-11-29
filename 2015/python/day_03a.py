from pathlib import Path


path = Path.cwd().parent / "inputs" / "03.txt"

with open(path) as f:
    directions = f.read()

house_x, house_y = (0, 0)
houses = {(house_x, house_y)}
headings = {"^": (1, 0), ">": (0, 1), "v": (-1, 0), "<": (0, -1)}

for direction in directions:
    dx, dy = headings[direction]
    house_x, house_y = (house_x + dx, house_y + dy)
    houses.add((house_x, house_y))

print(len(houses))
