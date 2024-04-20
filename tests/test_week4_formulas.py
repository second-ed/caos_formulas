import pytest

from src.formula_utils import HertzConverter, TimeConverter
from src.week4_formulas import *


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "performance_gain_from_hyperthreading": 64,
                "n_cores": 16,
                "k_ways_of_hyperthreading": 4,
            },
            64,
        ),
        (
            {
                "performance_gain_from_hyperthreading": 64,
                # "n_cores": 16,
                "k_ways_of_hyperthreading": 4,
            },
            16,
        ),
        (
            {
                "performance_gain_from_hyperthreading": 64,
                "n_cores": 16,
                # "k_ways_of_hyperthreading": 4,
            },
            4,
        ),
    ],
)
def test_performance_gain_from_hyperthreading(inputs, expected_result):
    assert solve_performance_gain_from_hyperthreading(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "cpu_time_pct_thread": 90,
                "total_time_slice_thread": TimeConverter().convert(90, "ms", "s"),
                "switch_time_thread": TimeConverter().convert(10, "ms", "s"),
            },
            90,
        ),
        (
            {
                "cpu_time_pct_thread": 90,
                # "total_time_slice_thread": TimeConverter().convert(90, "ms", "s"),
                "switch_time_thread": TimeConverter().convert(10, "ms", "s"),
            },
            TimeConverter().convert(90, "ms", "s"),
        ),
        (
            {
                "cpu_time_pct_thread": 90,
                "total_time_slice_thread": TimeConverter().convert(90, "ms", "s"),
                # "switch_time_thread": TimeConverter().convert(10, "ms", "s"),
            },
            TimeConverter().convert(10, "ms", "s"),
        ),
    ],
)
def test_cpu_time_pct_thread(inputs, expected_result):
    assert solve_cpu_time_pct_thread(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "time_interval_between_repetitions": TimeConverter().convert(0.3, "s", "s"),
                "total_time_slice_thread": TimeConverter().convert(90, "ms", "s"),
                "switch_time_thread": TimeConverter().convert(10, "ms", "s"),
                "n_tasks": 3,
            },
            TimeConverter().convert(0.3, "s", "s"),
        ),
        (
            {
                "time_interval_between_repetitions": TimeConverter().convert(
                    0.3, "s", "s"
                ),
                # "total_time_slice_thread": TimeConverter().convert(90, "ms", "s"),
                "switch_time_thread": TimeConverter().convert(10, "ms", "s"),
                "n_tasks": 3,
            },
            TimeConverter().convert(90, "ms", "s"),
        ),
        (
            {
                "time_interval_between_repetitions": TimeConverter().convert(
                    0.3, "s", "s"
                ),
                "total_time_slice_thread": TimeConverter().convert(90, "ms", "s"),
                # "switch_time_thread": TimeConverter().convert(10, "ms", "s"),
                "n_tasks": 3,
            },
            TimeConverter().convert(10, "ms", "s"),
        ),
        (
            {
                "time_interval_between_repetitions": TimeConverter().convert(
                    0.3, "s", "s"
                ),
                "total_time_slice_thread": TimeConverter().convert(90, "ms", "s"),
                "switch_time_thread": TimeConverter().convert(10, "ms", "s"),
                # "n_tasks": 3,
            },
            3,
        ),
    ],
)
def test_time_interval_between_repetitions(inputs, expected_result):
    assert solve_time_interval_between_repetitions(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "repetition_freq": HertzConverter().convert(100, "Hz", "Hz"),
                "time_interval_between_repetitions": TimeConverter().convert(
                    10, "ms", "s"
                ),
            },
            HertzConverter().convert(100, "Hz", "Hz"),
        ),
        (
            {
                "repetition_freq": HertzConverter().convert(100, "Hz", "Hz"),
                # "time_interval_between_repetitions": TimeConverter().convert(10, "ms", "s"),
            },
            TimeConverter().convert(10, "ms", "s"),
        ),
    ],
)
def test_repetition_freq(inputs, expected_result):
    assert solve_repetition_freq(inputs) == expected_result
