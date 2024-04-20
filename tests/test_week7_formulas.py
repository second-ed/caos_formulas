import pytest

from src.week7_formulas import *


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "p_no_failures_in_n_periods": 0.9801,
                "p_works": 0.99,
                "n": 2,
            },
            0.9801,
        ),
        (
            {
                "p_no_failures_in_n_periods": 0.9801,
                # "p_works": 0.99,
                "n": 2,
            },
            0.99,
        ),
        (
            {
                "p_no_failures_in_n_periods": 0.9801,
                "p_works": 0.99,
                # "n": 2,
            },
            2,
        ),
    ],
)
def test_p_no_failures_in_n_periods(inputs, expected_result):
    assert abs(solve_p_no_failures_in_n_periods(inputs)) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "p_exactly_1_failure_among_n_drives_in_1_period": 0.003988011996,
                "n": 4,
                "p_1_drive_fails_in_1_period": 0.001,
                "p_1_drive_works_in_1_period": 0.999,
            },
            0.003988011996,
        ),
        (
            {
                "p_exactly_1_failure_among_n_drives_in_1_period": 0.003988011996,
                "n": 4,
                # "p_1_drive_fails_in_1_period": 0.001,
                "p_1_drive_works_in_1_period": 0.999,
            },
            0.001,
        ),
        (
            {
                "p_exactly_1_failure_among_n_drives_in_1_period": 0.003988011996,
                "n": 4,
                "p_1_drive_fails_in_1_period": 0.001,
                # "p_1_drive_works_in_1_period": .999,
            },
            0.999,
        ),
    ],
)
def test_p_exactly_1_failure_among_n_drives_in_1_period(inputs, expected_result):
    assert (
        solve_p_exactly_1_failure_among_n_drives_in_1_period(inputs) == expected_result
    )


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "p_exactly_2_failure_among_n_drives_in_1_period": 0.0135375,
                "n": 4,
                "p_1_drive_fails_in_1_period": 0.05,
                "p_1_drive_works_in_1_period": 0.95,
            },
            0.0135375,
        ),
        (
            {
                "p_exactly_2_failure_among_n_drives_in_1_period": 0.0135375,
                "n": 4,
                # "p_1_drive_fails_in_1_period": 0.05,
                "p_1_drive_works_in_1_period": 0.95,
            },
            0.05,
        ),
        (
            {
                "p_exactly_2_failure_among_n_drives_in_1_period": 0.0135375,
                "n": 4,
                "p_1_drive_fails_in_1_period": 0.05,
                # "p_1_drive_works_in_1_period": 0.95,
            },
            0.95,
        ),
    ],
)
def test_p_exactly_2_failure_among_n_drives_in_1_period(inputs, expected_result):
    assert (
        abs(solve_p_exactly_2_failure_among_n_drives_in_1_period(inputs))
        == expected_result
    )
