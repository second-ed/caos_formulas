from typing import Dict

import sympy as sp

import pytest 

from src.formula_utils import HertzConverter
from src.week2_formulas import *


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({
			#'n_addressable_locations': 65536,
			'total_address_lines': 16
		}, 65536),
        ({
			'n_addressable_locations': 65536,
			#'total_address_lines': 16
		}, 16),
    ]
)
def test_n_addressable_locations(inputs, expected_result):
    assert solve_n_addressable_locations(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({
            #"storage_capacity": 512,
            "n_addressable_locations": 16,
            "n_data_lines": 32,
		}, 512),
        ({
            "storage_capacity": 512,
            #"n_addressable_locations": 16,
            "n_data_lines": 32,
    		}, 16),
        ({
            "storage_capacity": 512,
            "n_addressable_locations": 16,
            #"n_data_lines": 32,
		}, 32),
    ]
)
def test_storage_capacity(inputs, expected_result):
    assert solve_storage_capacity(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({
            #"cycle_time_normal_mode": 5,
            "ras": 1,
            "cas": 1,
            "access_time": 2,
            "recovery_cycles": 1,
		}, 5),
        ({
            "cycle_time_normal_mode": 5,
            #"ras": 1,
            "cas": 1,
            "access_time": 2,
            "recovery_cycles": 1,
		}, 1),
        ({
            "cycle_time_normal_mode": 5,
            "ras": 1,
            #"cas": 1,
            "access_time": 2,
            "recovery_cycles": 1,
		}, 1),
        ({
            "cycle_time_normal_mode": 5,
            "ras": 1,
            "cas": 1,
            #"access_time": 2,
            "recovery_cycles": 1,
		}, 2),
        ({
            "cycle_time_normal_mode": 5,
            "ras": 1,
            "cas": 1,
            "access_time": 2,
            #"recovery_cycles": 1,
		}, 1),
    ]
)
def test_cycle_time_normal_mode(inputs, expected_result):
    assert solve_cycle_time_normal_mode(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({
            #"cycle_time_n_reads_burst_mode": 10,
            "ras": 1,
            "cas": 1,
            "wait_time": 1,
            "n": 5,
            "read_time": 1,
            "recovery_cycles": 2,
		}, 10),
        ({
            "cycle_time_n_reads_burst_mode": 10,
            #"ras": 1,
            "cas": 1,
            "wait_time": 1,
            "n": 5,
            "read_time": 1,
            "recovery_cycles": 2,
		}, 1),
        ({
            "cycle_time_n_reads_burst_mode": 10,
            "ras": 1,
            #"cas": 1,
            "wait_time": 1,
            "n": 5,
            "read_time": 1,
            "recovery_cycles": 2,
		}, 1),
        ({
            #"cycle_time_n_reads_burst_mode": 10,
            "ras": 1,
            "cas": 1,
            #"wait_time": 1,
            "n": 5,
            "read_time": 1,
            "recovery_cycles": 2,
		}, 1),
        ({
            "cycle_time_n_reads_burst_mode": 10,
            "ras": 1,
            "cas": 1,
            "wait_time": 1,
            #"n": 5,
            "read_time": 1,
            "recovery_cycles": 2,
		}, 5),
        ({
            "cycle_time_n_reads_burst_mode": 10,
            "ras": 1,
            "cas": 1,
            "wait_time": 1,
            "n": 5,
            #"read_time": 1,
            "recovery_cycles": 2,
		}, 1),
        ({
            "cycle_time_n_reads_burst_mode": 10,
            "ras": 1,
            "cas": 1,
            "wait_time": 1,
            "n": 5,
            "read_time": 1,
            #"recovery_cycles": 2,
		}, 2),
    ]
)
def test_cycle_time_n_reads_burst_mode(inputs, expected_result):
    assert solve_cycle_time_n_reads_burst_mode(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({
            #"cycle_time_fast_page_mode": 14,
            "ras": 1,
            "cas": 1,
            "wait_time": 2,
            "n": 3,
            "read_time": 1,
            "recovery_cycles": 5,
		}, 14),
        ({
            "cycle_time_fast_page_mode": 14,
            #"ras": 1,
            "cas": 1,
            "wait_time": 2,
            "n": 3,
            "read_time": 1,
            "recovery_cycles": 5,
		}, 1),
        ({
            "cycle_time_fast_page_mode": 14,
            "ras": 1,
            #"cas": 1,
            "wait_time": 2,
            "n": 3,
            "read_time": 1,
            "recovery_cycles": 5,
		}, 1),
        ({
            "cycle_time_fast_page_mode": 14,
            "ras": 1,
            "cas": 1,
            #"wait_time": 2,
            "n": 3,
            "read_time": 1,
            "recovery_cycles": 5,
		}, 2),
        ({
            "cycle_time_fast_page_mode": 14,
            "ras": 1,
            "cas": 1,
            "wait_time": 2,
            #"n": 3,
            "read_time": 1,
            "recovery_cycles": 5,
		}, 3),
        ({
            "cycle_time_fast_page_mode": 14,
            "ras": 1,
            "cas": 1,
            "wait_time": 2,
            "n": 3,
            #"read_time": 1,
            "recovery_cycles": 5,
		}, 1),
        ({
            "cycle_time_fast_page_mode": 14,
            "ras": 1,
            "cas": 1,
            "wait_time": 2,
            "n": 3,
            "read_time": 1,
            #"recovery_cycles": 5,
		}, 5),
    ]
)
def test_cycle_time_fast_page_mode(inputs, expected_result):
    assert solve_cycle_time_fast_page_mode(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({
            #"cycle_time_mode_mixtures": 2.9,
            "cycle_time_mode1": 3.5,
            "ratio_mode1": 0.6,
            "cycle_time_mode2": 2,
            "ratio_mode2": 0.4,
		}, 2.9),
        ({
            "cycle_time_mode_mixtures": 2.9,
            #"cycle_time_mode1": 3.5,
            "ratio_mode1": 0.6,
            "cycle_time_mode2": 2,
            "ratio_mode2": 0.4,
		}, 3.5),
        ({
            "cycle_time_mode_mixtures": 2.9,
            "cycle_time_mode1": 3.5,
            #"ratio_mode1": 0.6,
            "cycle_time_mode2": 2,
            "ratio_mode2": 0.4,
		}, 0.6),
        ({
            "cycle_time_mode_mixtures": 2.9,
            "cycle_time_mode1": 3.5,
            "ratio_mode1": 0.6,
            #"cycle_time_mode2": 2,
            "ratio_mode2": 0.4,
		}, 2),
        ({
            "cycle_time_mode_mixtures": 2.9,
            "cycle_time_mode1": 3.5,
            "ratio_mode1": 0.6,
            "cycle_time_mode2": 2,
            #"ratio_mode2": 0.4,
		}, 0.4),
    ]
)
def test_cycle_time_mode_mixtures(inputs, expected_result):
    assert solve_cycle_time_mode_mixtures(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({
            #"data_transfer_rate": 6.4,
            "bus_width": 32,
            "cycle_time_total": 5,
		}, 6.4),
        ({
            "data_transfer_rate": 6.4,
            #"bus_width": 32,
            "cycle_time_total": 5,
		}, 32),
        ({
            "data_transfer_rate": 6.4,
            "bus_width": 32,
            #"cycle_time_total": 5,
		}, 5),
    ]
)
def test_data_transfer_rate(inputs, expected_result):
    assert solve_data_transfer_rate(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({
            #"cache_read_time_avg": 1.60000,
            "cache_hit_rate": 0.9,
            "cache_hit_time_avg": 1,
            "cache_miss_rate": 0.1,
            "cache_miss_time_avg": 7,
		}, 1.6),
        ({
            "cache_read_time_avg": 1.60000,
            #"cache_hit_rate": 0.9,
            "cache_hit_time_avg": 1,
            "cache_miss_rate": 0.1,
            "cache_miss_time_avg": 7,
		}, 0.9),
        ({
            "cache_read_time_avg": 1.60000,
            "cache_hit_rate": 0.9,
            #"cache_hit_time_avg": 1,
            "cache_miss_rate": 0.1,
            "cache_miss_time_avg": 7,
		}, 1),
        ({
            "cache_read_time_avg": 1.60000,
            "cache_hit_rate": 0.9,
            "cache_hit_time_avg": 1,
            #"cache_miss_rate": 0.1,
            "cache_miss_time_avg": 7,
		}, 0.1),
        ({
            "cache_read_time_avg": 1.60000,
            "cache_hit_rate": 0.9,
            "cache_hit_time_avg": 1,
            "cache_miss_rate": 0.1,
            #"cache_miss_time_avg": 7,
		}, 7),
    ]
)
def test_cache_read_time_avg(inputs, expected_result):
    assert solve_cache_read_time_avg(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({
            #"cache_miss_time_avg": 7,
            "cache_hit_time_avg": 1,
            "main_memory_read_time": 6,
		}, 7),
        ({
            "cache_miss_time_avg": 7,
            #"cache_hit_time_avg": 1,
            "main_memory_read_time": 6,
		}, 1),
        ({
            "cache_miss_time_avg": 7,
            "cache_hit_time_avg": 1,
            #"main_memory_read_time": 6,
		}, 6),
    ]
)
def test_cache_miss_time_avg(inputs, expected_result):
    assert solve_cache_miss_time_avg(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({
            #"cycle_time_sec": 3.6,
            "n_clock_cycles": 720000000,
            "clock_freq": HertzConverter().convert(200, "MHz", "Hz"),
		}, 3.6),
        ({
            "cycle_time_sec": 3.6,
            #"n_clock_cycles": 720000000,
            "clock_freq": HertzConverter().convert(200, "MHz", "Hz"),
		}, 720000000),
        ({
            "cycle_time_sec": 3.6,
            "n_clock_cycles": 720000000,
            #"clock_freq": HertzConverter().convert(200, "MHz", "Hz"),
		}, HertzConverter().convert(200, "MHz", "Hz")),
    ]
)
def test_cycle_time_sec(inputs, expected_result):
    assert solve_cycle_time_sec(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({
            #"time_speedup": 2,
            "time_original": 4,
            "time_new": 2,
		}, 2),
        ({
            "time_speedup": 2,
            #"time_original": 4,
            "time_new": 2,
		}, 4),
        ({
            "time_speedup": 2,
            "time_original": 4,
            #"time_new": 2,
		}, 2),
    ]
)
def test_time_speedup(inputs, expected_result):
    assert solve_time_speedup(inputs) == expected_result


