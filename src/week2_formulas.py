from typing import Dict

import sympy as sp

from src.formula_utils import _get_result, _get_output_sym


def solve_n_addressable_locations(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "n_addressable_locations": "",
        "total_address_lines": "",
    }

    n_addressable_locations, total_address_lines = sp.symbols(
        "n_addressable_locations total_address_lines"
    )
    equation = (2**total_address_lines) - n_addressable_locations
    output_sym = _get_output_sym(inputs, [n_addressable_locations, total_address_lines])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_storage_capacity(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "storage_capacity": "",
        "n_addressable_locations": "",
        "n_data_lines": "",
    }

    storage_capacity, n_addressable_locations, n_data_lines = sp.symbols(
        "storage_capacity n_addressable_locations n_data_lines"
    )
    equation = (n_addressable_locations * n_data_lines) - storage_capacity
    output_sym = _get_output_sym(
        inputs, [storage_capacity, n_addressable_locations, n_data_lines]
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_avg_memory_bandwidth(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "cycle_clocks": "clocks",
        "data_width": "bytes",
        "freq": "Hz",
        "avg_memory_bandwidth": "bytes / sec",
    }

    cycle_clocks, data_width, freq, avg_memory_bandwidth = sp.symbols(
        "cycle_clocks data_width freq avg_memory_bandwidth"
    )
    equation = (freq * data_width / cycle_clocks) - avg_memory_bandwidth
    output_sym = _get_output_sym(
        inputs, [cycle_clocks, data_width, freq, avg_memory_bandwidth]
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_cycle_time_normal_mode(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "cycle_time_normal_mode": "",
        "ras": "",
        "cas": "",
        "access_time": "",
        "recovery_cycles": "",
    }

    cycle_time_normal_mode, ras, cas, access_time, recovery_cycles = sp.symbols(
        "cycle_time_normal_mode ras cas access_time recovery_cycles"
    )
    equation = (ras + cas + access_time + recovery_cycles) - cycle_time_normal_mode
    output_sym = _get_output_sym(
        inputs, [cycle_time_normal_mode, ras, cas, access_time, recovery_cycles]
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_cycle_time_n_reads_burst_mode(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "cycle_time_n_reads_burst_mode": "",
        "ras": "",
        "cas": "",
        "wait_time": "",
        "n": "",
        "read_time": "",
        "recovery_cycles": "",
    }

    (
        cycle_time_n_reads_burst_mode,
        ras,
        cas,
        wait_time,
        n,
        read_time,
        recovery_cycles,
    ) = sp.symbols(
        "cycle_time_n_reads_burst_mode ras cas wait_time n read_time recovery_cycles"
    )
    equation = (
        ras + cas + wait_time + (n * read_time) + recovery_cycles
    ) - cycle_time_n_reads_burst_mode
    output_sym = _get_output_sym(
        inputs,
        [
            cycle_time_n_reads_burst_mode,
            ras,
            cas,
            wait_time,
            n,
            read_time,
            recovery_cycles,
        ],
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_cycle_time_fast_page_mode(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "cycle_time_fast_page_mode": "",
        "ras": "",
        "cas": "",
        "wait_time": "",
        "n": "",
        "read_time": "",
        "recovery_cycles": "",
    }

    (
        cycle_time_fast_page_mode,
        ras,
        cas,
        wait_time,
        n,
        read_time,
        recovery_cycles,
    ) = sp.symbols(
        "cycle_time_fast_page_mode ras cas wait_time n read_time recovery_cycles"
    )
    equation = (
        ras + (n * cas) + wait_time + (n * read_time) + recovery_cycles
    ) - cycle_time_fast_page_mode
    output_sym = _get_output_sym(
        inputs,
        [cycle_time_fast_page_mode, ras, cas, wait_time, n, read_time, recovery_cycles],
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_cycle_time_mode_mixtures(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "cycle_time_mode_mixtures": "",
        "cycle_time_mode1": "",
        "ratio_mode1": "",
        "cycle_time_mode2": "",
        "ratio_mode2": "",
    }

    (
        cycle_time_mode_mixtures,
        cycle_time_mode1,
        ratio_mode1,
        cycle_time_mode2,
        ratio_mode2,
    ) = sp.symbols(
        "cycle_time_mode_mixtures cycle_time_mode1 ratio_mode1 cycle_time_mode2 ratio_mode2"
    )
    equation = (
        cycle_time_mode1 * ratio_mode1 + cycle_time_mode2 * ratio_mode2
    ) - cycle_time_mode_mixtures
    output_sym = _get_output_sym(
        inputs,
        [
            cycle_time_mode_mixtures,
            cycle_time_mode1,
            ratio_mode1,
            cycle_time_mode2,
            ratio_mode2,
        ],
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_data_transfer_rate(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "data_transfer_rate": "",
        "bus_width": "",
        "cycle_time_total": "",
    }

    data_transfer_rate, bus_width, cycle_time_total = sp.symbols(
        "data_transfer_rate bus_width cycle_time_total"
    )
    equation = (bus_width / cycle_time_total) - data_transfer_rate
    output_sym = _get_output_sym(
        inputs, [data_transfer_rate, bus_width, cycle_time_total]
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_cache_read_time_avg(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "cache_read_time_avg": "",
        "cache_hit_rate": "",
        "cache_hit_time_avg": "",
        "cache_miss_rate": "",
        "cache_miss_time_avg": "",
    }

    (
        cache_read_time_avg,
        cache_hit_rate,
        cache_hit_time_avg,
        cache_miss_rate,
        cache_miss_time_avg,
    ) = sp.symbols(
        "cache_read_time_avg cache_hit_rate cache_hit_time_avg cache_miss_rate cache_miss_time_avg"
    )
    equation = (
        cache_hit_rate * cache_hit_time_avg + cache_miss_rate * cache_miss_time_avg
    ) - cache_read_time_avg
    output_sym = _get_output_sym(
        inputs,
        [
            cache_read_time_avg,
            cache_hit_rate,
            cache_hit_time_avg,
            cache_miss_rate,
            cache_miss_time_avg,
        ],
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_cache_miss_time_avg(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "cache_miss_time_avg": "",
        "cache_hit_time_avg": "",
        "main_memory_read_time": "",
    }

    cache_miss_time_avg, cache_hit_time_avg, main_memory_read_time = sp.symbols(
        "cache_miss_time_avg cache_hit_time_avg main_memory_read_time"
    )
    equation = (cache_hit_time_avg + main_memory_read_time) - cache_miss_time_avg
    output_sym = _get_output_sym(
        inputs, [cache_miss_time_avg, cache_hit_time_avg, main_memory_read_time]
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_cycle_time_sec(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "cycle_time_sec": "",
        "n_clock_cycles": "",
        "clock_freq": "",
    }

    cycle_time_sec, n_clock_cycles, clock_freq = sp.symbols(
        "cycle_time_sec n_clock_cycles clock_freq"
    )
    equation = (n_clock_cycles / clock_freq) - cycle_time_sec
    output_sym = _get_output_sym(inputs, [cycle_time_sec, n_clock_cycles, clock_freq])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_time_speedup(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "time_speedup": "",
        "time_original": "",
        "time_new": "",
    }

    time_speedup, time_original, time_new = sp.symbols(
        "time_speedup time_original time_new"
    )
    equation = (time_original / time_new) - time_speedup
    output_sym = _get_output_sym(inputs, [time_speedup, time_original, time_new])
    return _get_result(inputs, equation, output_sym, unit_map)
