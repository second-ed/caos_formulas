from typing import Dict

import sympy as sp

from src.formula_utils import _get_result, _get_output_sym


def solve_performance_gain_from_hyperthreading(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "performance_gain_from_hyperthreading": "",
        "n_cores": "",
        "k_ways_of_hyperthreading": "",
    }

    (
        performance_gain_from_hyperthreading,
        n_cores,
        k_ways_of_hyperthreading,
    ) = sp.symbols(
        "performance_gain_from_hyperthreading n_cores k_ways_of_hyperthreading"
    )
    equation = (
        n_cores * k_ways_of_hyperthreading
    ) - performance_gain_from_hyperthreading
    output_sym = _get_output_sym(
        inputs,
        [performance_gain_from_hyperthreading, n_cores, k_ways_of_hyperthreading],
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_cpu_time_pct_thread(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "cpu_time_pct_thread": "",
        "total_time_slice_thread": "",
        "switch_time_thread": "",
    }

    cpu_time_pct_thread, total_time_slice_thread, switch_time_thread = sp.symbols(
        "cpu_time_pct_thread total_time_slice_thread switch_time_thread"
    )
    equation = (
        (total_time_slice_thread / (total_time_slice_thread + switch_time_thread)) * 100
    ) - cpu_time_pct_thread
    output_sym = _get_output_sym(
        inputs, [cpu_time_pct_thread, total_time_slice_thread, switch_time_thread]
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_time_interval_between_repetitions(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "time_interval_between_repetitions": "",
        "total_time_slice_thread": "",
        "switch_time_thread": "",
        "n_tasks": "",
    }

    (
        time_interval_between_repetitions,
        total_time_slice_thread,
        switch_time_thread,
        n_tasks,
    ) = sp.symbols(
        "time_interval_between_repetitions total_time_slice_thread switch_time_thread n_tasks"
    )
    equation = (
        (total_time_slice_thread + switch_time_thread) * n_tasks
    ) - time_interval_between_repetitions
    output_sym = _get_output_sym(
        inputs,
        [
            time_interval_between_repetitions,
            total_time_slice_thread,
            switch_time_thread,
            n_tasks,
        ],
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_repetition_freq(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "repetition_freq": "",
        "time_interval_between_repetitions": "",
    }

    repetition_freq, time_interval_between_repetitions = sp.symbols(
        "repetition_freq time_interval_between_repetitions"
    )
    equation = (1 / time_interval_between_repetitions) - repetition_freq
    output_sym = _get_output_sym(
        inputs, [repetition_freq, time_interval_between_repetitions]
    )
    return _get_result(inputs, equation, output_sym, unit_map)
