import pytest

from src.week1_formulas import *


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "compute_density": 2,
                "max_mips": 10,
                "volume": 5,
            },
            2,
        ),
        (
            {
                "compute_density": 2,
                # "max_mips": 10,
                "volume": 5,
            },
            10,
        ),
        (
            {
                "compute_density": 2,
                "max_mips": 10,
                # "volume": 5,
            },
            5,
        ),
    ],
)
def test_compute_density(inputs, expected_result):
    assert solve_compute_density(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "power_density": 0.1,
                "power": 2,
                "volume": 20,
            },
            0.1,
        ),
        (
            {
                "power_density": 0.1,
                # "power": 2,
                "volume": 20,
            },
            2,
        ),
        (
            {
                "power_density": 0.1,
                "power": 2,
                # "volume": 20,
            },
            20,
        ),
    ],
)
def test_power_density(inputs, expected_result):
    assert float(solve_power_density(inputs)) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                #'cost_efficiency': 2,
                "price": 10,
                "max_mips": 5,
            },
            2,
        ),
        (
            {
                "cost_efficiency": 2,
                #'price': 10,
                "max_mips": 5,
            },
            10,
        ),
        (
            {
                "cost_efficiency": 2,
                "price": 10,
                #'max_mips': 5
            },
            5,
        ),
    ],
)
def test_cost_efficiency(inputs, expected_result):
    assert solve_cost_efficiency(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "cost_of_running_computer_for_n_secs": 20.005,
                "n_secs": 5,
                "power_consumption_per_sec": 0.1,
                "cost_per_sec": 0.01,
                "base_cost": 20,
            },
            20.005,
        ),
        (
            {
                "cost_of_running_computer_for_n_secs": 20.005,
                # "n_secs": 5,
                "power_consumption_per_sec": 0.1,
                "cost_per_sec": 0.01,
                "base_cost": 20,
            },
            5,
        ),
        (
            {
                "cost_of_running_computer_for_n_secs": 20.005,
                "n_secs": 5,
                # "power_consumption_per_sec": 0.1,
                "cost_per_sec": 0.01,
                "base_cost": 20,
            },
            0.1,
        ),
        (
            {
                "cost_of_running_computer_for_n_secs": 20.005,
                "n_secs": 5,
                "power_consumption_per_sec": 0.1,
                # "cost_per_sec": 0.01,
                "base_cost": 20,
            },
            0.01,
        ),
        (
            {
                "cost_of_running_computer_for_n_secs": 20.005,
                "n_secs": 5,
                "power_consumption_per_sec": 0.1,
                "cost_per_sec": 0.01,
                # "base_cost": 20,
            },
            20,
        ),
    ],
)
def test_cost_of_running_computer_for_n_secs(inputs, expected_result):
    assert solve_cost_of_running_computer_for_n_secs(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                #'max_speedup': 2,
                "P": 0.5
            },
            2,
        ),
        (
            {
                "max_speedup": 2,
                #'P': 0
            },
            0.5,
        ),
    ],
)
def test_max_speedup(inputs, expected_result):
    assert solve_max_speedup(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "true_speedup": 1.6,
                "P": 0.5,
                "n": 4,
            },
            1.6,
        ),
        (
            {
                "true_speedup": 1.6,
                # "P": 0.5,
                "n": 4,
            },
            0.50,
        ),
        (
            {
                "true_speedup": 1.6,
                "P": 0.5,
                # "n": 4,
            },
            4,
        ),
    ],
)
def test_true_speedup(inputs, expected_result):
    assert solve_true_speedup(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "gustafsons_law": 2.5,
                "P": 0.5,
                "n": 4,
            },
            2.5,
        ),
        (
            {
                "gustafsons_law": 2.5,
                # "P": 0.5,
                "n": 4,
            },
            0.5,
        ),
        (
            {
                "gustafsons_law": 2.5,
                "P": 0.5,
                # "n": 4,
            },
            4,
        ),
    ],
)
def test_gustafsons_law(inputs, expected_result):
    assert solve_gustafsons_law(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "branch_prediction_saving_time": 1,
                "hit_rate": 0.6,
                "hit_time_avg": 3,
                "miss_rate": 0.4,
                "miss_time_avg": 2,
            },
            1,
        ),
        (
            {
                "branch_prediction_saving_time": 1,
                # "hit_rate": 0.6,
                "hit_time_avg": 3,
                "miss_rate": 0.4,
                "miss_time_avg": 2,
            },
            0.6,
        ),
        (
            {
                "branch_prediction_saving_time": 1,
                "hit_rate": 0.6,
                # "hit_time_avg": 3,
                "miss_rate": 0.4,
                "miss_time_avg": 2,
            },
            3,
        ),
        (
            {
                "branch_prediction_saving_time": 1,
                "hit_rate": 0.6,
                "hit_time_avg": 3,
                # "miss_rate": 0.4,
                "miss_time_avg": 2,
            },
            0.4,
        ),
        (
            {
                "branch_prediction_saving_time": 1,
                "hit_rate": 0.6,
                "hit_time_avg": 3,
                "miss_rate": 0.4,
                # "miss_time_avg": 2,
            },
            2,
        ),
    ],
)
def test_branch_prediction_saving_time(inputs, expected_result):
    assert solve_branch_prediction_saving_time(inputs) == expected_result
