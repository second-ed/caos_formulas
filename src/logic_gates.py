from typing import List, Tuple
import pandas as pd
from itertools import product
import inspect


def generate_inputs(n):
    return list(product([0, 1], repeat=n))


def get_logic_outputs(inputs: List[Tuple], func):
    outputs = []
    for input in inputs:
        outputs.append((*input, *func(*input)))
    return outputs


def get_results_df(func, output_cols: List[str]):
    params = inspect.signature(func).parameters.keys()
    n: int = len(params)
    input_cols = list(params)
    return pd.DataFrame(
        get_logic_outputs(generate_inputs(n), func), columns=input_cols + output_cols
    )


def buffer_gate(x) -> int:
    return int(bool(x))


def inverter_gate(x) -> int:
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
