from typing import Dict

import sympy as sp

from src.formula_utils import (
    _get_output_sym,
    _get_result,
    ByteConverter,
)


def solve_clock_freq(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {"t": "s", "f": "Hz"}

    t, f = sp.symbols("t f")
    equation = 1 / t - f

    output_sym = _get_output_sym(inputs, [t, f])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_max_speedup(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {"max_speedup": "", "P": ""}

    max_speedup, P = sp.symbols("max_speedup P")
    equation = 1 / (1 - P) - max_speedup

    output_sym = _get_output_sym(inputs, [max_speedup, P])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_true_speedup(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {"true_speedup": "", "P": "", "n": ""}

    true_speedup, P, n = sp.symbols("true_speedup P n")
    equation = 1 / ((1 - P) + (P / n)) - true_speedup

    output_sym = _get_output_sym(inputs, [true_speedup, P, n])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_gustafsons_law(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "speedup": " speed up of n processors",
        "P": " proportion that can be parallelized",
        "n": " processors",
    }

    speedup, P, n = sp.symbols("speedup P n")
    equation = (n + (P * (1 - n))) - speedup

    output_sym = _get_output_sym(inputs, [speedup, P, n])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_branch_prediction(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "cycles_saved": "cycles",
        "cycles_cost": "cycles",
        "p_correct": "",
        "p_incorrect": "",
        "total_savings": "cycles",
    }

    cycles_saved, cycles_cost, p_correct, p_incorrect, total_savings = sp.symbols(
        "cycles_saved cycles_cost p_correct p_incorrect total_savings"
    )
    equation = (p_correct * cycles_saved) - (p_incorrect * cycles_cost) - total_savings

    output_sym = _get_output_sym(
        inputs, [cycles_saved, cycles_cost, p_correct, p_incorrect, total_savings]
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_reads_per_sec(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "freq": "Hz",
        "clocks_per_read": "clocks",
        "reads_per_sec": "reads per sec",
    }

    freq, clocks_per_read, reads_per_sec = sp.symbols(
        "freq clocks_per_read reads_per_sec"
    )
    equation = (freq / clocks_per_read) - reads_per_sec

    output_sym = _get_output_sym(inputs, [reads_per_sec, freq, clocks_per_read])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_memory_bandwidth(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "reads_per_sec": "reads per sec",
        "bytes": "B",
        "memory_bandwidth": "bytes per second",
    }

    reads_per_sec, bytes, memory_bandwidth = sp.symbols(
        "reads_per_sec, bytes, memory_bandwidth"
    )
    equation = (reads_per_sec * bytes) - memory_bandwidth

    output_sym = _get_output_sym(inputs, [reads_per_sec, bytes, memory_bandwidth])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_address_locations(inputs) -> float:
    unit_map = {
        "address_lines": "bits",
        "address_locations": "locations",
    }

    address_lines, address_locations = sp.symbols("address_lines address_locations")
    equation = (2**address_lines) - address_locations

    output_sym = _get_output_sym(inputs, [address_lines, address_locations])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_storage_capacity(inputs) -> float:
    n_data_lines_bytes = ByteConverter().convert(inputs["data_lines"], "b", "B")
    n_memory_locs = solve_address_locations({"address_lines": inputs["address_lines"]})
    result = n_data_lines_bytes * n_memory_locs
    print(f"{result :.5f}")
    return result


def solve_avg_memory_read_time(inputs) -> float:
    unit_map: Dict[str, str] = {
        "access_time": "",
        "recovery_cycles": "",
        "ras_cycles": "",
        "cas_cycles": "",
        "avg_memory_read_time": "",
    }

    (
        access_time,
        recovery_cycles,
        ras_cycles,
        cas_cycles,
        avg_memory_read_time,
    ) = sp.symbols(
        "access_time recovery_cycles ras_cycles cas_cycles avg_memory_read_time"
    )
    equation = (
        access_time + recovery_cycles + ras_cycles + cas_cycles - avg_memory_read_time
    )

    output_sym = _get_output_sym(
        inputs,
        [
            access_time,
            recovery_cycles,
            ras_cycles,
            cas_cycles,
            avg_memory_read_time,
        ],
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_memory_data_rate(inputs) -> float:
    unit_map: Dict[str, str] = {
        "memory_read_time": "clock read time",
        "memory_width": "bits",
        "clock_rate": "Hz",
        "memory_data_rate": "bytes per second",
    }

    memory_read_time, memory_width, clock_rate, memory_data_rate = sp.symbols(
        "memory_read_time memory_width clock_rate memory_data_rate"
    )
    equation = ((clock_rate / memory_read_time) * memory_width) - memory_data_rate

    output_sym = _get_output_sym(
        inputs, [memory_read_time, memory_width, clock_rate, memory_data_rate]
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_sustainable_data_rate(inputs) -> float:
    unit_map: Dict[str, str] = {
        "n_sectors": "sectors",
        "sector_size": "B",
        "rotational_latency": "RPM",
        "sustainable_data_rate": "",
    }

    n_sectors, sector_size, rotational_latency, sustainable_data_rate = sp.symbols(
        "n_sectors sector_size rotational_latency sustainable_data_rate"
    )
    equation = (
        1 / (((60 / rotational_latency) / n_sectors) / sector_size)
    ) - sustainable_data_rate
    output_sym = _get_output_sym(
        inputs, [n_sectors, sector_size, rotational_latency, sustainable_data_rate]
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_cache_avg_read_time(inputs) -> float:
    unit_map: Dict[str, str] = {
        "p_cache": "",
        "sram": "clocks",
        "dram": "clocks",
        "ras": "clocks",
        "cas": "clocks",
        "cache_avg_read_time": "clocks",
    }

    p_cache, sram, dram, ras, cas, cache_avg_read_time = sp.symbols(
        "p_cache sram dram ras cas cache_avg_read_time"
    )
    equation = (
        (p_cache * (sram + ras + cas))
        + ((1 - p_cache) * (sram + dram + ras + cas))
        - cache_avg_read_time
    )

    output_sym = _get_output_sym(
        inputs, [p_cache, sram, dram, ras, cas, cache_avg_read_time]
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_data_transfer_rate(inputs) -> float:
    unit_map: Dict[str, str] = {
        "protocol_overhead": "cycles",
        "bus_width": "bytes",
        "bus_frequency": "Hz",
        "data_transfer_rate": "bytes/sec",
    }

    protocol_overhead, bus_width, bus_frequency, data_transfer_rate = sp.symbols(
        "protocol_overhead bus_width bus_frequency data_transfer_rate"
    )
    equation = (
        bus_frequency * bus_width / (protocol_overhead + 1)
    ) - data_transfer_rate

    output_sym = _get_output_sym(
        inputs, [protocol_overhead, bus_width, bus_frequency, data_transfer_rate]
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_data_transfer_efficiency(inputs) -> float:
    unit_map: Dict[str, str] = {
        "protocol_overhead": "cycles",
        "bus_width": "bytes",
        "block_size": "bytes",
        "data_transfer_efficiency": "",
    }

    protocol_overhead, bus_width, block_size, data_transfer_efficiency = sp.symbols(
        "protocol_overhead bus_width block_size data_transfer_efficiency"
    )
    equation = (
        (block_size / bus_width) / ((block_size / bus_width) + protocol_overhead)
    ) - data_transfer_efficiency

    output_sym = _get_output_sym(
        inputs, [protocol_overhead, bus_width, block_size, data_transfer_efficiency]
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_synchronous_bus_max_bandwidth(inputs) -> float:
    unit_map: Dict[str, str] = {
        "bus_width": "bytes",
        "clock_cycle_time": "sec",
        "ras": "clocks",
        "cas": "clocks",
        "send_clocks": "clocks",
        "memory_access_time": "sec",
        "maximum_bandwidth": "bytes/sec",
    }

    (
        bus_width,
        clock_cycle_time,
        ras,
        cas,
        send_clocks,
        memory_access_time,
        maximum_bandwidth,
    ) = sp.symbols(
        "bus_width clock_cycle_time ras cas send_clocks memory_access_time maximum_bandwidth"
    )
    equation = (
        bus_width
        / (
            ((ras + cas) * clock_cycle_time)
            + memory_access_time
            + (send_clocks * clock_cycle_time)
        )
    ) - maximum_bandwidth

    output_sym = _get_output_sym(
        inputs,
        [
            bus_width,
            clock_cycle_time,
            ras,
            cas,
            send_clocks,
            memory_access_time,
            maximum_bandwidth,
        ],
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_asynchronous_bus_max_bandwidth(inputs) -> float:
    unit_map: Dict[str, str] = {
        "bus_width": "bytes",
        "handshake_time": "sec",
        "memory_access_time": "sec",
        "maximum_bandwidth": "bytes/sec",
    }

    (
        bus_width,
        handshake_time,
        memory_access_time,
        maximum_bandwidth,
    ) = sp.symbols("bus_width handshake_time memory_access_time maximum_bandwidth")
    equation = (
        bus_width
        / (
            handshake_time
            + sp.Max((3 * handshake_time), memory_access_time)
            + (3 * handshake_time)
        )
    ) - maximum_bandwidth

    output_sym = _get_output_sym(
        inputs,
        [
            bus_width,
            handshake_time,
            memory_access_time,
            maximum_bandwidth,
        ],
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_probability_of_failure(inputs) -> float:
    unit_map: Dict[str, str] = {
        "P": "",
        "n": "",
        "P_failure": "",
    }

    P, n, P_failure = sp.symbols("P n P_failure")
    equation = (P**n) - P_failure

    output_sym = _get_output_sym(inputs, [P, n, P_failure])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_probability_of_no_failure(inputs) -> float:
    unit_map: Dict[str, str] = {
        "P": "",
        "n": "",
        "P_failure": "",
    }

    P, n, P_failure = sp.symbols("P n P_failure")
    equation = ((1 - P) ** n) - P_failure

    output_sym = _get_output_sym(inputs, [P, n, P_failure])
    return _get_result(inputs, equation, output_sym, unit_map)
