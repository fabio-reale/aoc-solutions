from pathlib import Path


def is_nice_sandwich(santa_str: str) -> bool:
    for fst_char, snd_char in zip(santa_str, santa_str[2:]):
        if fst_char == snd_char:
            return True

    return False


def is_nice_double_pair(santa_str: str) -> bool:
    doubles: dict[tuple, int] = {}

    for ind, tup in enumerate(zip(santa_str, santa_str[1:])):

        seen = doubles.get(tup)
        if seen is None:
            doubles[tup] = ind
        elif seen < ind - 1:
            return True

    return False


def is_nice_str(santa_str: str) -> bool:
    return is_nice_sandwich(santa_str) and is_nice_double_pair(santa_str)


def solve(inp: str) -> int:
    nice_list = [santa_str for santa_str in inp.split() if is_nice_str(santa_str)]
    return len(nice_list)


# unit tests
assert is_nice_str("qjhvhtzxzqqjkmpb")
assert is_nice_str("xxyxx")
assert is_nice_str("xxxx")
assert not is_nice_str("uurcxstgmygtbstg")
assert not is_nice_str("ieodomkazucvgmuy")
assert not is_nice_str("xxxyx")

path = Path.cwd().parent / "inputs" / "05.txt"

with open(path) as f:
    inp = f.read()

print(solve(inp))
