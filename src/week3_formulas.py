from typing import Dict

import sympy as sp

from src.formula_utils import _get_result, _get_output_sym


def solve_cycles_total(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "cycles_total": "",
        "cycles_payload": "",
        "cycles_overhead": "",
    }

    cycles_total, cycles_payload, cycles_overhead = sp.symbols(
        "cycles_total cycles_payload cycles_overhead"
    )
    equation = (cycles_payload + cycles_overhead) - cycles_total
    output_sym = _get_output_sym(
        inputs, [cycles_total, cycles_payload, cycles_overhead]
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_bus_data_transfer_rate(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "bus_data_transfer_rate": "",
        "bus_freq": "",
        "amount_of_data": "",
        "cycles_total": "",
    }

    bus_data_transfer_rate, bus_freq, amount_of_data, cycles_total = sp.symbols(
        "bus_data_transfer_rate bus_freq amount_of_data cycles_total"
    )
    equation = ((bus_freq * amount_of_data) / cycles_total) - bus_data_transfer_rate
    output_sym = _get_output_sym(
        inputs, [bus_data_transfer_rate, bus_freq, amount_of_data, cycles_total]
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_cycles_block(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "cycles_block": "",
        "size_block": "",
        "size_bus_width": "",
    }

    cycles_block, size_block, size_bus_width = sp.symbols(
        "cycles_block size_block size_bus_width"
    )
    equation = (size_block / size_bus_width) - cycles_block
    output_sym = _get_output_sym(inputs, [cycles_block, size_block, size_bus_width])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_bus_data_transfer_efficiency(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "bus_data_transfer_efficiency": "",
        "cycles_block": "",
        "cycles_overhead": "",
    }

    bus_data_transfer_efficiency, cycles_block, cycles_overhead = sp.symbols(
        "bus_data_transfer_efficiency cycles_block cycles_overhead"
    )
    equation = (
        (cycles_block / (cycles_block + cycles_overhead)) * 100
    ) - bus_data_transfer_efficiency
    output_sym = _get_output_sym(
        inputs, [bus_data_transfer_efficiency, cycles_block, cycles_overhead]
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_read_time_synchronous(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "read_time_synchronous": "",
        "time_send_address": "",
        "time_memory_access": "",
        "time_send_data": "",
    }

    (
        read_time_synchronous,
        time_send_address,
        time_memory_access,
        time_send_data,
    ) = sp.symbols(
        "read_time_synchronous time_send_address time_memory_access time_send_data"
    )
    equation = (
        time_send_address + time_memory_access + time_send_data
    ) - read_time_synchronous
    output_sym = _get_output_sym(
        inputs,
        [read_time_synchronous, time_send_address, time_memory_access, time_send_data],
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_read_time_asynchronous(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "read_time_asynchronous": "",
        "time_handshake": "",
        "time_memory_access": "",
    }

    read_time_asynchronous, time_handshake, time_memory_access = sp.symbols(
        "read_time_asynchronous time_handshake time_memory_access"
    )
    equation = (
        ((1 + 3) * time_handshake) + sp.Max(time_memory_access, (3 * time_handshake))
    ) - read_time_asynchronous
    output_sym = _get_output_sym(
        inputs, [read_time_asynchronous, time_handshake, time_memory_access]
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_bandwidth_max_for_bus(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "bandwidth_max_for_bus": "",
        "n_bytes_to_transfer": "",
        "read_time_per_block": "",
        "n_blocks_total": "",
    }

    (
        bandwidth_max_for_bus,
        n_bytes_to_transfer,
        read_time_per_block,
        n_blocks_total,
    ) = sp.symbols(
        "bandwidth_max_for_bus n_bytes_to_transfer read_time_per_block n_blocks_total"
    )
    equation = (
        n_bytes_to_transfer / (read_time_per_block * n_blocks_total)
    ) - bandwidth_max_for_bus
    output_sym = _get_output_sym(
        inputs,
        [
            bandwidth_max_for_bus,
            n_bytes_to_transfer,
            read_time_per_block,
            n_blocks_total,
        ],
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_disk_revolution_time_sec(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "disk_revolution_time_sec": "",
        "rotations_per_min": "",
    }

    disk_revolution_time_sec, rotations_per_min = sp.symbols(
        "disk_revolution_time_sec rotations_per_min"
    )
    equation = (60 / rotations_per_min) - disk_revolution_time_sec
    output_sym = _get_output_sym(inputs, [disk_revolution_time_sec, rotations_per_min])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_disk_access_time_worst(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "disk_access_time_worst": "",
        "time_rotational_latency": "",
        "time_head_seek": "",
    }

    disk_access_time_worst, time_rotational_latency, time_head_seek = sp.symbols(
        "disk_access_time_worst time_rotational_latency time_head_seek"
    )
    equation = (time_rotational_latency + time_head_seek) - disk_access_time_worst
    output_sym = _get_output_sym(
        inputs, [disk_access_time_worst, time_rotational_latency, time_head_seek]
    )
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_disk_access_time_avg(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "disk_access_time_avg": "",
        "disk_access_time_worst": "",
    }

    disk_access_time_avg, disk_access_time_worst = sp.symbols(
        "disk_access_time_avg disk_access_time_worst"
    )
    equation = (disk_access_time_worst / 2) - disk_access_time_avg
    output_sym = _get_output_sym(inputs, [disk_access_time_avg, disk_access_time_worst])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_track_size(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "track_size": "",
        "sector_size": "",
        "sectors_per_track": "",
    }

    track_size, sector_size, sectors_per_track = sp.symbols(
        "track_size sector_size sectors_per_track"
    )
    equation = (sector_size * sectors_per_track) - track_size
    output_sym = _get_output_sym(inputs, [track_size, sector_size, sectors_per_track])
    return _get_result(inputs, equation, output_sym, unit_map)


def solve_data_transfer_rate_disk(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "data_transfer_rate_disk": "",
        "track_size": "",
        "rotations_per_sec": "",
    }

    data_transfer_rate_disk, track_size, rotations_per_sec = sp.symbols(
        "data_transfer_rate_disk track_size rotations_per_sec"
    )
    equation = (track_size * rotations_per_sec) - data_transfer_rate_disk
    output_sym = _get_output_sym(
        inputs, [data_transfer_rate_disk, track_size, rotations_per_sec]
    )
    return _get_result(inputs, equation, output_sym, unit_map)
