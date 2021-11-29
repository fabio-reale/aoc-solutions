from pathlib import Path

path = Path(__file__).parents[1] / "inputs" / "10.txt"

with open(path) as f:
    lst = [int(c) for c in f.read()]


def look_say(look: list[int]) -> list[int]:
    last: int = 0
    last_count: int = 0
    say: list[int] = []

    for i in look + [0]:
        if i == last:
            last_count += 1
        else:
            if last:
                say.extend([last_count, last])
            last = i
            last_count = 1

    return say


def stringify(lst: list[int]) -> str:
    return "".join([str(i) for i in lst])


def solve(n: int, look: list[int]) -> int:
    for i in range(n):
        look = look_say(look)

    return len(look)


print(solve(50, lst))
