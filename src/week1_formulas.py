from typing import Dict

import sympy as sp

from src.formula_utils import _get_result, _get_output_sym


def solve_compute_density(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "compute_density": "",
        "max_mips": "",
        "volume": "",
    }

    compute_density, max_mips, volume = sp.symbols("compute_density max_mips volume")
    equation = (max_mips / volume) - compute_density
    output_sym = _get_output_sym(inputs, [compute_density, max_mips, volume])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_power_density(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "power_density": "",
        "power": "",
        "volume": "",
    }

    power_density, power, volume = sp.symbols("power_density power volume")
    equation = (power / volume) - power_density
    output_sym = _get_output_sym(inputs, [power_density, power, volume])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_cost_efficiency(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "cost_efficiency": "",
        "price": "",
        "max_mips": "",
    }

    cost_efficiency, price, max_mips = sp.symbols("cost_efficiency price max_mips")
    equation = (price / max_mips) - cost_efficiency
    output_sym = _get_output_sym(inputs, [cost_efficiency, price, max_mips])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_cost_of_running_computer_for_n_secs(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "cost_of_running_computer_for_n_secs": "",
        "n_secs": "",
        "power_consumption_per_sec": "",
        "cost_per_sec": "",
        "base_cost": "",
    }

    (
        cost_of_running_computer_for_n_secs,
        n_secs,
        power_consumption_per_sec,
        cost_per_sec,
        base_cost,
    ) = sp.symbols(
        "cost_of_running_computer_for_n_secs n_secs power_consumption_per_sec cost_per_sec base_cost"
    )
    equation = (
        n_secs * power_consumption_per_sec * cost_per_sec + base_cost
    ) - cost_of_running_computer_for_n_secs
    output_sym = _get_output_sym(
        inputs,
        [
            cost_of_running_computer_for_n_secs,
            n_secs,
            power_consumption_per_sec,
            cost_per_sec,
            base_cost,
        ],
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_max_speedup(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "max_speedup": "",
        "P": "",
    }

    max_speedup, P = sp.symbols("max_speedup P")
    equation = (1 / (1 - P)) - max_speedup
    output_sym = _get_output_sym(inputs, [max_speedup, P])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_true_speedup(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "true_speedup": "",
        "P": "",
        "n": "",
    }

    true_speedup, P, n = sp.symbols("true_speedup P n")
    equation = (1 / ((1 - P) + (P / n))) - true_speedup
    output_sym = _get_output_sym(inputs, [true_speedup, P, n])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_gustafsons_law(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "gustafsons_law": "",
        "P": "",
        "n": "",
    }

    gustafsons_law, P, n = sp.symbols("gustafsons_law P n")
    equation = ((1 - P) + (P * n)) - gustafsons_law
    output_sym = _get_output_sym(inputs, [gustafsons_law, P, n])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_branch_prediction_saving_time(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "branch_prediction_saving_time": "",
        "hit_rate": "",
        "hit_time_avg": "",
        "miss_rate": "",
        "miss_time_avg": "",
    }

    (
        branch_prediction_saving_time,
        hit_rate,
        hit_time_avg,
        miss_rate,
        miss_time_avg,
    ) = sp.symbols(
        "branch_prediction_saving_time hit_rate hit_time_avg miss_rate miss_time_avg"
    )
    equation = (
        hit_rate * hit_time_avg - miss_rate * miss_time_avg
    ) - branch_prediction_saving_time
    output_sym = _get_output_sym(
        inputs,
        [
            branch_prediction_saving_time,
            hit_rate,
            hit_time_avg,
            miss_rate,
            miss_time_avg,
        ],
    )
    return _get_result(inputs, equation, output_sym, unit_map)
