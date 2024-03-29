from typing import Dict, Tuple

import sympy as sp

from src.constants import BYTES_MAP, HZ_MAP, TIME_MAP


class HertzConverter:
    @staticmethod
    def convert(value: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in HZ_MAP or to_unit not in HZ_MAP:
            raise ValueError("Invalid units provided")
        return value * HZ_MAP[from_unit] / HZ_MAP[to_unit]


class ByteConverter:
    @staticmethod
    def convert(value, from_unit, to_unit):
        if from_unit not in BYTES_MAP or to_unit not in BYTES_MAP:
            raise ValueError("Invalid units provided")

        return value * BYTES_MAP[from_unit] / BYTES_MAP[to_unit]


class TimeConverter:
    @staticmethod
    def convert(value: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in TIME_MAP or to_unit not in TIME_MAP:
            raise ValueError("Invalid units provided")

        base_value = value * TIME_MAP[from_unit]
        target_value = base_value / TIME_MAP[to_unit]
        return target_value


def solve_equation(equation, inputs, output_sym):
    return sp.solve(equation.subs(inputs), output_sym)


def solve_clock_freq(inputs: Dict) -> Tuple[float, str]:
    unit_map: Dict[str, str] = {"t": "s", "f": "Hz"}

    t, f = sp.symbols("t f")
    equation = 1 / t - f

    output_sym = None
    for sym in [t, f]:
        if str(sym) not in inputs:
            output_sym = sym
            break

    if output_sym:
        result = solve_equation(equation, inputs, output_sym)[0]
        unit = unit_map[str(output_sym)]
        return result, f"{result :.5f} {unit}"
    else:
        raise ValueError("All inputs provided, no variable to solve for")


def solve_max_speedup(inputs: Dict) -> Tuple[float, str]:
    unit_map: Dict[str, str] = {"max_speedup": "", "P": ""}

    max_speedup, P = sp.symbols("max_speedup P")
    equation = 1 / (1 - P) - max_speedup

    output_sym = None
    for sym in [max_speedup, P]:
        if str(sym) not in inputs:
            output_sym = sym
            break

    if output_sym:
        result = solve_equation(equation, inputs, output_sym)[0]
        unit = unit_map[str(output_sym)]
        return result, f"{result :.5f} {unit}"
    else:
        raise ValueError("All inputs provided, no variable to solve for")


def solve_true_speedup(inputs: Dict) -> Tuple[float, str]:
    unit_map: Dict[str, str] = {"true_speedup": "", "P": "", "n": ""}

    true_speedup, P, n = sp.symbols("true_speedup P n")
    equation = 1 / ((1 - P) + (P / n)) - true_speedup

    output_sym = None
    for sym in [true_speedup, P, n]:
        if str(sym) not in inputs:
            output_sym = sym
            break

    if output_sym:
        result = solve_equation(equation, inputs, output_sym)[0]
        unit = unit_map[str(output_sym)]
        return result, f"{result :.5f} {unit}"
    else:
        raise ValueError("All inputs provided, no variable to solve for")


def solve_branch_prediction(inputs: Dict) -> Tuple[float, str]:
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

    output_sym = None
    for sym in [cycles_saved, cycles_cost, p_correct, p_incorrect, total_savings]:
        if str(sym) not in inputs:
            output_sym = sym
            break

    if output_sym:
        result = solve_equation(equation, inputs, output_sym)[0]
        unit = unit_map[str(output_sym)]
        return result, f"{result :.5f} {unit}"
    else:
        raise ValueError("All inputs provided, no variable to solve for")


def solve_address_locations(inputs) -> Tuple[float, str]:
    unit_map = {
        "address_lines": "bits",
        "address_locations": "locations",
    }

    address_lines, address_locations = sp.symbols("address_lines address_locations")
    equation = (2**address_lines) - address_locations

    output_sym = None
    for sym in [address_lines, address_locations]:
        if str(sym) not in inputs:
            output_sym = sym
            break

    if output_sym:
        result = solve_equation(equation, inputs, output_sym)[0]
        unit = unit_map[str(output_sym)]
        return result, f"{result} {unit}"
    else:
        raise ValueError("All inputs provided, no variable to solve for")


def solve_storage_capacity(inputs) -> Tuple[float, str]:
    n_data_lines_bytes = ByteConverter().convert(inputs["data_lines"], "b", "B")
    n_memory_locs, _ = solve_address_locations(
        {"address_lines": inputs["address_lines"]}
    )
    total_bytes = n_data_lines_bytes * n_memory_locs
    result = ByteConverter().convert(total_bytes, "B", inputs["to_unit"])
    return result, f"{result :.5f} {inputs['to_unit']}"


def solve_avg_memory_read_time(inputs) -> Tuple[float, str]:
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

    output_sym = None
    for sym in [
        access_time,
        recovery_cycles,
        ras_cycles,
        cas_cycles,
        avg_memory_read_time,
    ]:
        if str(sym) not in inputs:
            output_sym = sym
            break

    if output_sym:
        result = solve_equation(equation, inputs, output_sym)[0]
        unit = unit_map[str(output_sym)]
        return result, f"{result :.5f} {unit}"
    else:
        raise ValueError("All inputs provided, no variable to solve for")


def solve_memory_data_rate(inputs, units: str) -> Tuple[float, str]:
    unit_map: Dict[str, str] = {
        "memory_read_time": "clock read time",
        "memory_width": "bits",
        "clock_rate": "Hz",
        "memory_data_rate": f"{units} per second",
    }

    memory_read_time, memory_width, clock_rate, memory_data_rate = sp.symbols(
        "memory_read_time memory_width clock_rate memory_data_rate"
    )
    equation = ((clock_rate / memory_read_time) * memory_width) - memory_data_rate

    output_sym = None
    for sym in [memory_read_time, memory_width, clock_rate, memory_data_rate]:
        if str(sym) not in inputs:
            output_sym = sym
            break

    if output_sym:
        result = ByteConverter().convert(
            solve_equation(equation, inputs, output_sym)[0], "B", units
        )
        unit = unit_map[str(output_sym)]
        return result, f"{result :.5f} {unit}"
    else:
        raise ValueError("All inputs provided, no variable to solve for")


def solve_cache_avg_read_time(inputs) -> Tuple[float, str]:
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
        # + ((1 - p_cache) * dram)
        - cache_avg_read_time
    )

    output_sym = None
    for sym in [p_cache, sram, dram, ras, cas, cache_avg_read_time]:
        if str(sym) not in inputs:
            output_sym = sym
            break

    if output_sym:
        result = solve_equation(equation, inputs, output_sym)[0]
        unit = unit_map[str(output_sym)]
        return result, "{:.5f} {}".format(result, unit)
    else:
        raise ValueError("All inputs provided, no variable to solve for")
