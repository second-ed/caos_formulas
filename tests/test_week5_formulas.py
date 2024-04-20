import pytest

from src.formula_utils import ByteConverter
from src.week5_formulas import *


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "compression_ratio": 2,
                "original_size": ByteConverter().convert(200, "MB", "B"),
                "compressed_size": ByteConverter().convert(100, "MB", "B"),
            },
            2,
        ),
        (
            {
                "compression_ratio": 2,
                # "original_size": ByteConverter().convert(200, "MB", "B"),
                "compressed_size": ByteConverter().convert(100, "MB", "B"),
            },
            ByteConverter().convert(200, "MB", "B"),
        ),
        (
            {
                "compression_ratio": 2,
                "original_size": ByteConverter().convert(200, "MB", "B"),
                # "compressed_size": ByteConverter().convert(100, "MB", "B"),
            },
            ByteConverter().convert(100, "MB", "B"),
        ),
    ],
)
def test_compression_ratio(inputs, expected_result):
    assert solve_compression_ratio(inputs) == expected_result
