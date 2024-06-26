from typing import Callable, List, Tuple

import pandas as pd
import pytest

from src.logic_gates import (
    and_gate,
    buffer_gate,
    full_adder,
    generate_inputs,
    get_logic_outputs,
    get_results_df,
    half_adder,
    inverter_gate,
    nand_gate,
    nor_gate,
    or_gate,
    xnor_gate,
    xor_gate,
)


def and_into_inverse(x, y) -> Tuple[int]:
    z = inverter_gate(and_gate(x, y))
    return (z,)


@pytest.mark.parametrize("x, expected", [(1, 1), (0, 0)])
def test_buffer_gate(x: int, expected: int) -> None:
    assert buffer_gate(x) == expected


@pytest.mark.parametrize("x, expected", [(1, 0), (0, 1)])
def test_inverter_gate(x: int, expected: int) -> None:
    assert inverter_gate(x) == expected


@pytest.mark.parametrize("x, y, expected", [(1, 1, 1), (1, 0, 0), (0, 1, 0), (0, 0, 0)])
def test_and_gate(x: int, y: int, expected: int) -> None:
    assert and_gate(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [(1, 1, 1), (1, 0, 1), (0, 1, 1), (0, 0, 0)])
def test_or_gate(x: int, y: int, expected: int) -> None:
    assert or_gate(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [(1, 1, 0), (1, 0, 1), (0, 1, 1), (0, 0, 1)])
def test_nand_gate(x: int, y: int, expected: int) -> None:
    assert nand_gate(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [(1, 1, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)])
def test_nor_gate(x: int, y: int, expected: int) -> None:
    assert nor_gate(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [(1, 1, 0), (1, 0, 1), (0, 1, 1), (0, 0, 0)])
def test_xor_gate(x: int, y: int, expected: int) -> None:
    assert xor_gate(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [(1, 1, 1), (1, 0, 0), (0, 1, 0), (0, 0, 1)])
def test_xnor_gate(x: int, y: int, expected: int) -> None:
    assert xnor_gate(x, y) == expected


@pytest.mark.parametrize(
    "x, y, expected_sum, expected_carry",
    [
        (0, 0, 0, 0),
        (0, 1, 1, 0),
        (1, 0, 1, 0),
        (1, 1, 0, 1),
    ],
)
def test_half_adder(x: int, y: int, expected_sum: int, expected_carry: int) -> None:
    assert half_adder(x, y) == (expected_sum, expected_carry)


@pytest.mark.parametrize(
    "x, y, c_in, expected_sum, expected_carry",
    [
        (0, 0, 0, 0, 0),
        (0, 0, 1, 1, 0),
        (0, 1, 0, 1, 0),
        (0, 1, 1, 0, 1),
        (1, 0, 0, 1, 0),
        (1, 0, 1, 0, 1),
        (1, 1, 0, 0, 1),
        (1, 1, 1, 1, 1),
    ],
)
def test_full_adder(
    x: int, y: int, c_in: int, expected_sum: int, expected_carry: int
) -> None:
    assert full_adder(x, y, c_in) == (expected_sum, expected_carry)


@pytest.mark.parametrize(
    "n, expected_output",
    [
        (2, [(0, 0), (0, 1), (1, 0), (1, 1)]),
        (
            3,
            [
                (0, 0, 0),
                (0, 0, 1),
                (0, 1, 0),
                (0, 1, 1),
                (1, 0, 0),
                (1, 0, 1),
                (1, 1, 0),
                (1, 1, 1),
            ],
        ),
        (
            4,
            [
                (0, 0, 0, 0),
                (0, 0, 0, 1),
                (0, 0, 1, 0),
                (0, 0, 1, 1),
                (0, 1, 0, 0),
                (0, 1, 0, 1),
                (0, 1, 1, 0),
                (0, 1, 1, 1),
                (1, 0, 0, 0),
                (1, 0, 0, 1),
                (1, 0, 1, 0),
                (1, 0, 1, 1),
                (1, 1, 0, 0),
                (1, 1, 0, 1),
                (1, 1, 1, 0),
                (1, 1, 1, 1),
            ],
        ),
    ],
)
def test_generate_inputs(n: int, expected_output: List[Tuple]) -> None:
    assert generate_inputs(n) == expected_output


@pytest.mark.parametrize(
    "inputs, func, expected_output",
    [
        (
            generate_inputs(2),
            and_into_inverse,
            [(0, 0, 1), (0, 1, 1), (1, 0, 1), (1, 1, 0)],
        )
    ],
)
def test_get_logic_outputs(
    inputs: List[Tuple], func: Callable, expected_output: List[Tuple]
) -> None:
    assert get_logic_outputs(inputs, func) == expected_output


@pytest.mark.parametrize(
    "func, col, expected_output",
    [
        (
            and_into_inverse,
            ["z"],
            pd.DataFrame().from_dict(
                {"x": [0, 0, 1, 1], "y": [0, 1, 0, 1], "z": [1, 1, 1, 0]}
            ),
        ),
    ],
)
def test_get_results_df(func: Callable, col: List[str], expected_output: pd.DataFrame):
    assert all(get_results_df(func, col).eq(expected_output))
