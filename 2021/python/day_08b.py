from pathlib import Path

Sig = frozenset[str]
Digits = set[Sig]


def parse_input(inp: str) -> list[list[str]]:
    lines = inp.split("\n")
    return [line.split(" | ") for line in lines]


def parse_line(line: list[str]) -> tuple[Digits, list[str]]:
    all_digits = {frozenset(sig) for sig in line[0].split()}
    digits = line[1].split()
    return all_digits, digits


def find_147(
    all_digits: Digits, decoder: dict[Sig, str], encoder: dict[str, Sig]
) -> None:
    by_len = {"2": "1", "3": "7", "4": "4"}

    for dig in all_digits:
        len_dig = str(len(dig))
        if len_dig in by_len:
            decoder[dig] = by_len[len_dig]
            encoder[by_len[len_dig]] = dig

    all_digits.difference_update(decoder.keys())


def find_9(
    all_digits: Digits, decoder: dict[Sig, str], encoder: dict[str, Sig]
) -> None:
    for dig in all_digits:
        if encoder["4"].issubset(dig):
            decoder[dig] = "9"
            encoder["9"] = dig

    all_digits.remove(encoder["9"])


def find_3(
    all_digits: Digits, decoder: dict[Sig, str], encoder: dict[str, Sig]
) -> None:
    for dig in all_digits:
        if len(dig) == 5 and encoder["1"].issubset(dig):
            decoder[dig] = "3"
            encoder["3"] = dig

    all_digits.remove(encoder["3"])


def find_0(
    all_digits: Digits, decoder: dict[Sig, str], encoder: dict[str, Sig]
) -> None:
    for dig in all_digits:
        if encoder["7"].issubset(dig):
            decoder[dig] = "0"
            encoder["0"] = dig

    all_digits.remove(encoder["0"])


def find_6(
    all_digits: Digits, decoder: dict[Sig, str], encoder: dict[str, Sig]
) -> None:
    for dig in all_digits:
        if len(dig) == 6:
            decoder[dig] = "6"
            encoder["6"] = dig

    all_digits.remove(encoder["6"])


def find_52(
    all_digits: Digits, decoder: dict[Sig, str], encoder: dict[str, Sig]
) -> None:
    for dig in all_digits:
        if dig.issubset(encoder["6"]):
            decoder[dig] = "5"
            encoder["5"] = dig
        else:
            decoder[dig] = "2"
            encoder["2"] = dig

    all_digits = set()


def decode(all_digits: Digits) -> dict[Sig, str]:
    eight = frozenset("abcdefg")
    decoder = {eight: "8"}
    encoder = {"8": eight}
    all_digits.remove(eight)
    for find in [find_147, find_9, find_3, find_0, find_6, find_52]:
        find(all_digits, decoder, encoder)

    return decoder


def solve(inp: str) -> int:
    lines = parse_input(inp)
    total = 0
    for line in lines:
        all_digits, digits = parse_line(line)
        decoder = decode(all_digits)
        string_digits = "".join([decoder[frozenset(digit)] for digit in digits])
        while string_digits[0] == "0":
            string_digits = string_digits[1:]
        total += eval(string_digits)
    return total


if __name__ == "__main__":
    path = Path(__file__).parents[1] / "inputs" / "day_08.txt"

    with open(path) as f:
        inp = f.read().strip()

    print(solve(inp))
