from __future__ import annotations
from typing import Any, TypeVar
import sys
import itertools as it


class Packet:
    def __init__(self, ver: int, op: int, val: str | int | list[Packet]) -> None:
        self.ver = ver
        self.op = op
        self.val = val

    def __repr__(self) -> str:
        return f"Packet({self.ver}, {self.op}, {self.val})"

    @classmethod
    def from_string(cls, bin_str: str) -> Packet:
        return cls(int(bin_str[:3], 2), int(bin_str[3:6], 2), bin_str[6:])

    def get_versions_sum(self) -> int:
        if isinstance(self.val, list):
            return self.ver + sum([p.get_versions_sum() for p in self.val])
        elif isinstance(self.val, Packet):
            return self.ver + self.val.get_versions_sum()
        else:
            return self.ver


def process_4(pack: Packet) -> tuple[Packet, str]:
    assert isinstance(pack.val, str)

    bits = ""
    flag = "1"
    rest_str = pack.val
    while flag == "1":
        flag, nibble, rest_str = rest_str[0], rest_str[1:5], rest_str[5:]
        bits += nibble
    pack.val = int(bits, 2)

    return pack, rest_str


def process_indicator_0(pack: Packet) -> tuple[Packet, str]:
    assert isinstance(pack.val, str)

    length = int(pack.val[:15], 2)
    subpacks_str, rest_str = pack.val[15 : 15 + length], pack.val[15 + length :]
    subpacks_val, _ = process_bin_str(subpacks_str)

    return Packet(pack.ver, pack.op, subpacks_val), rest_str


def process_indicator_1(pack: Packet) -> tuple[Packet, str]:
    assert isinstance(pack.val, str)

    subpacks_num = int(pack.val[:11], 2)
    subpacks_val, rest_str = process_bin_str(pack.val[11:], max_packs=subpacks_num)

    return Packet(pack.ver, pack.op, subpacks_val), rest_str


def process_bin_str(bin_str: str, max_packs: int = -1) -> tuple[list[Packet], str]:
    packs: list[Packet] = []
    while len(bin_str) >= 11 and max_packs != len(packs):
        pack = Packet.from_string(bin_str)
        assert isinstance(pack.val, str)

        if pack.op == 4:
            new_pack, bin_str = process_4(pack)
        else:
            indicator = pack.val[0]
            pack.val = pack.val[1:]
            if indicator == "0":
                new_pack, bin_str = process_indicator_0(pack)
            else:
                new_pack, bin_str = process_indicator_1(pack)
        packs.append(new_pack)

    return packs, bin_str


def parse_input_dumb(inp: str) -> str:
    hex_map = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    return "".join([hex_map[c] for c in inp])


def solve(inp: str) -> int:
    bin_str = parse_input_dumb(inp)
    packs, padding = process_bin_str(bin_str, max_packs=1)

    return packs[0].get_versions_sum()


if __name__ == "__main__":
    from time import perf_counter

    with open(sys.argv[1], "r") as f:
        inp = f.read().strip()

    st = perf_counter()

    print(solve(inp))

    end = perf_counter()
    print(f"\nTime elapsed: {end-st}s")
