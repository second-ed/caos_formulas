import pytest
from src.logic_gates import (
    and_gate,
    generate_inputs,
    get_logic_outputs,
    inverter_gate,
    or_gate,
    nand_gate,
    nor_gate,
    xor_gate,
    xnor_gate,
    half_adder,
    full_adder,
)


def and_into_inverse(x, y):
    z = inverter_gate(and_gate(x, y))
    return (z,)


@pytest.mark.parametrize("x, y, expected", [(1, 1, 1), (1, 0, 0), (0, 1, 0), (0, 0, 0)])
def test_and_gate(x, y, expected):
    assert and_gate(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [(1, 1, 1), (1, 0, 1), (0, 1, 1), (0, 0, 0)])
def test_or_gate(x, y, expected):
    assert or_gate(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [(1, 1, 0), (1, 0, 1), (0, 1, 1), (0, 0, 1)])
def test_nand_gate(x, y, expected):
    assert nand_gate(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [(1, 1, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)])
def test_nor_gate(x, y, expected):
    assert nor_gate(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [(1, 1, 0), (1, 0, 1), (0, 1, 1), (0, 0, 0)])
def test_xor_gate(x, y, expected):
    assert xor_gate(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [(1, 1, 1), (1, 0, 0), (0, 1, 0), (0, 0, 1)])
def test_xnor_gate(x, y, expected):
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
def test_half_adder(x, y, expected_sum, expected_carry):
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
def test_full_adder(x, y, c_in, expected_sum, expected_carry):
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
def test_generate_inputs(n, expected_output):
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
def test_get_logic_outputs(inputs, func, expected_output):
    assert get_logic_outputs(inputs, func) == expected_output
