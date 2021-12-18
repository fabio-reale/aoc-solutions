import sys


def triangle(n: int) -> int:
    return n * (n + 1) // 2


# pass in min_y from target y axis as command line arg
y = int(sys.argv[1])

print(triangle(abs(y) - 1))
