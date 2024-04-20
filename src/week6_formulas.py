from typing import Dict

import sympy as sp

from src.formula_utils import _get_result, _get_output_sym


def solve_total_network_bandwidth(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "total_network_bandwidth": "",
        "raw_bandwidth": "",
        "bridge_bandwidth": "",
    }

    total_network_bandwidth, raw_bandwidth, bridge_bandwidth = sp.symbols(
        "total_network_bandwidth raw_bandwidth bridge_bandwidth"
    )
    equation = ((2 * raw_bandwidth) - bridge_bandwidth) - total_network_bandwidth
    output_sym = _get_output_sym(
        inputs, [total_network_bandwidth, raw_bandwidth, bridge_bandwidth]
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_packet_bytes_total(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "packet_bytes_total": "",
        "packet_bytes_payload": "",
        "packet_bytes_overhead": "",
    }

    packet_bytes_total, packet_bytes_payload, packet_bytes_overhead = sp.symbols(
        "packet_bytes_total packet_bytes_payload packet_bytes_overhead"
    )
    equation = (packet_bytes_payload + packet_bytes_overhead) - packet_bytes_total
    output_sym = _get_output_sym(
        inputs, [packet_bytes_total, packet_bytes_payload, packet_bytes_overhead]
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_true_data_rate(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "true_data_rate": "",
        "raw_data_rate": "",
        "efficiency": "",
    }

    true_data_rate, raw_data_rate, efficiency = sp.symbols(
        "true_data_rate raw_data_rate efficiency"
    )
    equation = (raw_data_rate * efficiency) - true_data_rate
    output_sym = _get_output_sym(inputs, [true_data_rate, raw_data_rate, efficiency])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_packet_latency(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "packet_latency": "",
        "packet_size": "",
        "raw_data_rate": "",
    }

    packet_latency, packet_size, raw_data_rate = sp.symbols(
        "packet_latency packet_size raw_data_rate"
    )
    equation = (packet_size / raw_data_rate) - packet_latency
    output_sym = _get_output_sym(inputs, [packet_latency, packet_size, raw_data_rate])
    return _get_result(inputs, equation, output_sym, unit_map)
