from typing import Dict

import sympy as sp

from src.formula_utils import _get_result, _get_output_sym


def solve_p_no_failures_in_n_periods(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "p_no_failures_in_n_periods": "",
        "p_works": "",
        "n": "",
    }

    p_no_failures_in_n_periods, p_works, n = sp.symbols(
        "p_no_failures_in_n_periods p_works n"
    )
    equation = (p_works**n) - p_no_failures_in_n_periods
    output_sym = _get_output_sym(inputs, [p_no_failures_in_n_periods, p_works, n])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_p_exactly_1_failure_among_n_drives_in_1_period(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "p_exactly_1_failure_among_n_drives_in_1_period": "",
        "n": "",
        "p_1_drive_fails_in_1_period": "",
        "p_1_drive_works_in_1_period": "",
    }

    (
        p_exactly_1_failure_among_n_drives_in_1_period,
        n,
        p_1_drive_fails_in_1_period,
        p_1_drive_works_in_1_period,
    ) = sp.symbols(
        "p_exactly_1_failure_among_n_drives_in_1_period n p_1_drive_fails_in_1_period p_1_drive_works_in_1_period"
    )
    equation = (
        n * p_1_drive_fails_in_1_period * (p_1_drive_works_in_1_period ** (n - 1))
    ) - p_exactly_1_failure_among_n_drives_in_1_period
    output_sym = _get_output_sym(
        inputs,
        [
            p_exactly_1_failure_among_n_drives_in_1_period,
            n,
            p_1_drive_fails_in_1_period,
            p_1_drive_works_in_1_period,
        ],
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_p_exactly_2_failure_among_n_drives_in_1_period(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "p_exactly_2_failure_among_n_drives_in_1_period": "",
        "n": "",
        "p_1_drive_fails_in_1_period": "",
        "p_1_drive_works_in_1_period": "",
    }

    (
        p_exactly_2_failure_among_n_drives_in_1_period,
        n,
        p_1_drive_fails_in_1_period,
        p_1_drive_works_in_1_period,
    ) = sp.symbols(
        "p_exactly_2_failure_among_n_drives_in_1_period n p_1_drive_fails_in_1_period p_1_drive_works_in_1_period"
    )
    equation = (
        ((n**2 - n) / 2)
        * (p_1_drive_fails_in_1_period**2)
        * (p_1_drive_works_in_1_period ** (n - 2))
    ) - p_exactly_2_failure_among_n_drives_in_1_period
    output_sym = _get_output_sym(
        inputs,
        [
            p_exactly_2_failure_among_n_drives_in_1_period,
            n,
            p_1_drive_fails_in_1_period,
            p_1_drive_works_in_1_period,
        ],
    )
    return _get_result(inputs, equation, output_sym, unit_map)
