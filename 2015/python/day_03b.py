from pathlib import Path

path = Path.cwd().parent / "inputs" / "03.txt"

with open(path) as f:
    directions = f.read()

santa_x, santa_y = (0, 0)
robot_santa_x, robot_santa_y = (0, 0)
houses = {(santa_x, santa_y)}
headings = {"^": (1, 0), ">": (0, 1), "v": (-1, 0), "<": (0, -1)}

for i, direction in enumerate(directions):
    dx, dy = headings[direction]
    if i % 2 == 0:
        santa_x, santa_y = (santa_x + dx, santa_y + dy)
        houses.add((santa_x, santa_y))
    else:
        robot_santa_x, robot_santa_y = (robot_santa_x + dx, robot_santa_y + dy)
        houses.add((robot_santa_x, robot_santa_y))

print(len(houses))
