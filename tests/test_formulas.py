import numpy as np
import pytest

from src.formulas import (
    ByteConverter,
    HertzConverter,
    solve_address_locations,
    solve_avg_memory_read_time,
    solve_branch_prediction,
    solve_cache_avg_read_time,
    solve_clock_freq,
    solve_max_speedup,
    solve_memory_data_rate,
    solve_storage_capacity,
    solve_true_speedup,
)


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({"f": 100}, 0.01),
        ({"t": 0.01}, 100),
    ],
)
def test_solve_clock_freq(inputs, expected_result) -> None:
    assert float(solve_clock_freq(inputs)[0]) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({"P": 0.5}, 2.0),
        ({"P": 0.2}, 1.25),
        ({"P": 0.99}, 100),
        ({"max_speedup": 2.0}, 0.5),
        ({"max_speedup": 4.0}, 0.75),
    ],
)
def test_solve_max_speedup(inputs, expected_result) -> None:
    assert float(solve_max_speedup(inputs)[0]) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({"P": 0.5, "n": 3}, 1.5000000),
        ({"P": 0.5, "true_speedup": 1.5}, 3),
        ({"true_speedup": 1.5, "n": 3}, 0.5),
    ],
)
def test_solve_true_speedup(inputs, expected_result) -> None:
    assert float(solve_true_speedup(inputs)[0]) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                "cycles_saved": 3,
                "cycles_cost": 2,
                "p_correct": 0.4,
                "p_incorrect": 0.6,
                # "total_savings": 0,
            },
            0,
        ),
        (
            {
                "cycles_saved": 3,
                "cycles_cost": 2,
                # "p_correct": 0.4,
                "p_incorrect": 0.6,
                "total_savings": 0,
            },
            0.4,
        ),
        (
            {
                # "cycles_saved": 3,
                "cycles_cost": 2,
                "p_correct": 0.4,
                "p_incorrect": 0.6,
                "total_savings": 0,
            },
            3,
        ),
        (
            {
                "cycles_saved": 3,
                # "cycles_cost": 2,
                "p_correct": 0.4,
                "p_incorrect": 0.6,
                "total_savings": 0,
            },
            2,
        ),
    ],
)
def test_solve_branch_prediction(inputs, expected_result) -> None:
    assert np.allclose(float(solve_branch_prediction(inputs)[0]), expected_result)


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({"address_locations": 65536}, 16.0),
        ({"address_lines": 16}, 65536),
    ],
)
def test_solve_address_locations(inputs, expected_result) -> None:
    assert float(solve_address_locations(inputs)[0]) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({"address_lines": 32, "data_lines": 64, "to_unit": "MB"}, 32768.00),
    ],
)
def test_solve_storage_capacity(inputs, expected_result) -> None:
    assert float(solve_storage_capacity(inputs)[0]) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                "access_time": 5,
                "recovery_cycles": 2,
                "ras_cycles": 1,
                "cas_cycles": 1,
            },
            9,
        ),
    ],
)
def test_solve_avg_memory_read_time(inputs, expected_result) -> None:
    assert float(solve_avg_memory_read_time(inputs)[0]) == expected_result


@pytest.mark.parametrize(
    "inputs, units, expected_result",
    [
        (
            {
                "memory_read_time": 5,
                "memory_width": ByteConverter().convert(32, "b", "B"),
                "clock_rate": HertzConverter().convert(1, "GHz", "Hz"),
            },
            "MB",
            762.939453125000,
        ),
    ],
)
def test_solve_memory_data_rate(inputs, units, expected_result) -> None:
    assert float(solve_memory_data_rate(inputs, units)[0]) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                "p_cache": 0.9,
                "sram": 1.0,
                "dram": 3.0,
                "ras": 1.0,
                "cas": 1.0,
            },
            3.300,
        ),
    ],
)
def test_solve_cache_avg_read_time(inputs, expected_result) -> None:
    assert float(solve_cache_avg_read_time(inputs)[0]) == expected_result
