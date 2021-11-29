from pathlib import Path


def is_naughty(st: str) -> bool:
    naughty_strs = ["ab", "cd", "pq", "xy"]
    return any([n in st for n in naughty_strs])


def is_nice_vowel(st: str) -> bool:
    vowels_needed: int = 3

    for c in st:
        if c in "aeiou":
            vowels_needed -= 1
        if vowels_needed <= 0:
            return True

    return False


def is_nice_double(st: str) -> bool:
    for c, d in zip(st, st[1:]):
        if c == d:
            return True

    return False


def is_nice_str(st: str) -> bool:
    return is_nice_vowel(st) and is_nice_double(st) and not is_naughty(st)


def solve(inp: str) -> int:
    nice_list = [st for st in inp.split() if is_nice_str(st)]
    return len(nice_list)


# unit tests
assert is_nice_str("ugknbfddgicrmopn") == True
assert is_nice_str("aaa") == True
assert is_nice_str("jchzalrnumimnmhp") == False
assert is_nice_str("haegwjzuvuyypxyu") == False
assert is_nice_str("dvszwmarrgswjxmb") == False

path = Path.cwd().parent / "inputs" / "05.txt"

with open(path) as f:
    inp = f.read()

print(solve(inp))
