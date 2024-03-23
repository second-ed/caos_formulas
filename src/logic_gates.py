from typing import Tuple


def buffer(x) -> int:
    return int(bool(x))


def inverter(x) -> int:
    return int(bool(not x))


def and_gate(x, y) -> int:
    return int(x and y)


def or_gate(x, y) -> int:
    return int(x or y)


def nand_gate(x, y) -> int:
    return int(not (x and y))


def nor_gate(x, y) -> int:
    return int(not (x or y))


def xor_gate(x, y) -> int:
    return int((x and not y) or (not x and y))


def xnor_gate(x, y) -> int:
    return int((not x and not y) or (x and y))


def half_adder(x, y) -> Tuple[int, int]:
    return xor_gate(x, y), and_gate(x, y)


def full_adder(x, y, c_in) -> Tuple[int, int]:
    sum1, carry1 = half_adder(x, y)
    sum2, carry2 = half_adder(sum1, c_in)
    carry_out = or_gate(carry1, carry2)
    return sum2, carry_out
