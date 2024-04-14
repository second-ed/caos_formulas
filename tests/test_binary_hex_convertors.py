import numpy as np
import pytest
from hypothesis import given
from hypothesis import strategies as st

from src.binary_hex_convertors import (
    binary_to_num,
    hexadecimal_to_num,
    num_to_binary,
    num_to_hexadecimal,
)


@given(st.integers())
def test_st_num_to_binary(num) -> None:
    assert num_to_binary(num, use_pad=False) == np.binary_repr(num)


@given(st.integers())
def test_st_binary(num) -> None:
    assert binary_to_num(num_to_binary(num)) == num


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (-100, "-01100100"),
        (-93, "-01011101"),
        (-86, "-01010110"),
        (-79, "-01001111"),
        (-72, "-01001000"),
        (-65, "-01000001"),
        (-58, "-00111010"),
        (-51, "-00110011"),
        (-44, "-00101100"),
        (-37, "-00100101"),
        (-30, "-00011110"),
        (-23, "-00010111"),
        (-16, "-00010000"),
        (-9, "-1001"),
        (-2, "-0010"),
        (5, "0101"),
        (12, "1100"),
        (19, "00010011"),
        (26, "00011010"),
        (33, "00100001"),
        (40, "00101000"),
        (47, "00101111"),
        (54, "00110110"),
        (61, "00111101"),
        (68, "01000100"),
        (75, "01001011"),
        (82, "01010010"),
        (89, "01011001"),
        (96, "01100000"),
    ],
)
def test_num_to_binary(input, expected_output) -> None:
    assert num_to_binary(input) == expected_output


@pytest.mark.parametrize(
    "input, expected_output",
    [
        ("-11001000", -200),
        ("-10111011", -187),
        ("-10101110", -174),
        ("-10100001", -161),
        ("-10010100", -148),
        ("-10000111", -135),
        ("-01111010", -122),
        ("-01101101", -109),
        ("-01100000", -96),
        ("-01010011", -83),
        ("-01000110", -70),
        ("-00111001", -57),
        ("-00101100", -44),
        ("-00011111", -31),
        ("-00010010", -18),
        ("-0101", -5),
        ("1000", 8),
        ("00010101", 21),
        ("00100010", 34),
        ("00101111", 47),
        ("00111100", 60),
        ("01001001", 73),
        ("01010110", 86),
        ("01100011", 99),
        ("01110000", 112),
        ("01111101", 125),
        ("10001010", 138),
        ("10010111", 151),
        ("10100100", 164),
        ("10110001", 177),
        ("10111110", 190),
    ],
)
def test_binary_to_num(input, expected_output) -> None:
    assert binary_to_num(input) == expected_output


@given(st.integers())
def test_st_hexadecimal(num) -> None:
    assert hexadecimal_to_num(num_to_hexadecimal(num)) == num


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (-100, "-0X64"),
        (-93, "-0X5D"),
        (-86, "-0X56"),
        (-79, "-0X4F"),
        (-72, "-0X48"),
        (-65, "-0X41"),
        (-58, "-0X3A"),
        (-51, "-0X33"),
        (-44, "-0X2C"),
        (-37, "-0X25"),
        (-30, "-0X1E"),
        (-23, "-0X17"),
        (-16, "-0X10"),
        (-9, "-0X9"),
        (-2, "-0X2"),
        (5, "0X5"),
        (12, "0XC"),
        (19, "0X13"),
        (26, "0X1A"),
        (33, "0X21"),
        (40, "0X28"),
        (47, "0X2F"),
        (54, "0X36"),
        (61, "0X3D"),
        (68, "0X44"),
        (75, "0X4B"),
        (82, "0X52"),
        (89, "0X59"),
        (96, "0X60"),
    ],
)
def test_num_to_hexadecimal(input, expected_output) -> None:
    assert num_to_hexadecimal(input) == expected_output


@pytest.mark.parametrize(
    "input, expected_output",
    [
        ("-0XC8", -200),
        ("-0XBB", -187),
        ("-0XAE", -174),
        ("-0XA1", -161),
        ("-0X94", -148),
        ("-0X87", -135),
        ("-0X7A", -122),
        ("-0X6D", -109),
        ("-0X60", -96),
        ("-0X53", -83),
        ("-0X46", -70),
        ("-0X39", -57),
        ("-0X2C", -44),
        ("-0X1F", -31),
        ("-0X12", -18),
        ("-0X5", -5),
        ("0X8", 8),
        ("0X15", 21),
        ("0X22", 34),
        ("0X2F", 47),
        ("0X3C", 60),
        ("0X49", 73),
        ("0X56", 86),
        ("0X63", 99),
        ("0X70", 112),
        ("0X7D", 125),
        ("0X8A", 138),
        ("0X97", 151),
        ("0XA4", 164),
        ("0XB1", 177),
        ("0XBE", 190),
    ],
)
def test_hexadecimal_to_num(input, expected_output) -> None:
    assert hexadecimal_to_num(input) == expected_output


@pytest.mark.parametrize(
    "input",
    [
        ("0XYEAH"),
        ("0X34!"),
    ],
)
def test_raises_hexadecimal_to_num(input):
    with pytest.raises(ValueError):
        hexadecimal_to_num(input)
