from __future__ import annotations

import json
from pathlib import Path

from typing import Any, TypeVar, Callable

T = TypeVar("T")


def const_zero(arg: Any) -> int:
    return 0


def identity(arg: T) -> T:
    return arg


def accumulate_from_list(struct: list[Any]) -> int:
    acc_funcs: dict[type, Callable[..., int]] = {
        int: identity,
        list: accumulate_from_list,
        dict: accumulate_from_dict,
    }

    accum = 0
    for val in struct:
        accum += acc_funcs.get(type(val), const_zero)(val)

    return accum


def accumulate_from_dict(struct: dict[str, Any]) -> int:
    if "red" in struct.values():
        return 0

    return accumulate_from_list(list(struct.values()))


def solve(struct):
    return accumulate_from_list([struct])


if __name__ == "__main__":
    path = Path(__file__).parents[1] / "inputs" / "12.txt"

    with open(path) as f:
        vals = json.load(f)

    print(solve(vals))
