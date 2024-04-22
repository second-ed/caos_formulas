import pytest

from src.formula_utils import ByteConverter, HertzConverter, TimeConverter
from src.week3_formulas import *


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "cycles_total": 9,
                "cycles_payload": 5,
                "cycles_overhead": 4,
            },
            9,
        ),
        (
            {
                "cycles_total": 9,
                # "cycles_payload": 5,
                "cycles_overhead": 4,
            },
            5,
        ),
        (
            {
                "cycles_total": 9,
                "cycles_payload": 5,
                # "cycles_overhead": 4
            },
            4,
        ),
    ],
)
def test_cycles_total(inputs, expected_result):
    assert solve_cycles_total(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "bus_data_transfer_rate": 160000000.,
                "bus_freq": HertzConverter().convert(200, "MHz", "Hz"),
                "amount_of_data": ByteConverter().convert(32, "b", "B"),
                "cycles_total": 5,
            },
            160000000,
        ),
        (
            {
                "bus_data_transfer_rate": 160000000.0,
                # "bus_freq": HertzConverter().convert(200, "MHz", "Hz"),
                "amount_of_data": ByteConverter().convert(32, "b", "B"),
                "cycles_total": 5,
            },
            HertzConverter().convert(200, "MHz", "Hz"),
        ),
        (
            {
                "bus_data_transfer_rate": 160000000.0,
                "bus_freq": HertzConverter().convert(200, "MHz", "Hz"),
                # "amount_of_data": ByteConverter().convert(32, "b", "B"),
                "cycles_total": 5,
            },
            ByteConverter().convert(32, "b", "B"),
        ),
        (
            {
                "bus_data_transfer_rate": 160000000.0,
                "bus_freq": HertzConverter().convert(200, "MHz", "Hz"),
                "amount_of_data": ByteConverter().convert(32, "b", "B"),
                # "cycles_total": 5,
            },
            5,
        ),
    ],
)
def test_bus_data_transfer_rate(inputs, expected_result):
    assert solve_bus_data_transfer_rate(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "cycles_block": 16.00000,
                "size_block": ByteConverter().convert(256, "b", "B"),
                "size_bus_width": ByteConverter().convert(16, "b", "B"),
            },
            16,
        ),
        (
            {
                "cycles_block": 16.00000,
                # "size_block": ByteConverter().convert(256, "b", "B"),
                "size_bus_width": ByteConverter().convert(16, "b", "B"),
            },
            ByteConverter().convert(256, "b", "B"),
        ),
        (
            {
                "cycles_block": 16.00000,
                "size_block": ByteConverter().convert(256, "b", "B"),
                # "size_bus_width": ByteConverter().convert(16, "b", "B"),
            },
            ByteConverter().convert(16, "b", "B"),
        ),
    ],
)
def test_cycles_block(inputs, expected_result):
    assert solve_cycles_block(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "bus_data_transfer_efficiency": 60.00,
                "cycles_block": 6,
                "cycles_overhead": 4,
            },
            60,
        ),
        (
            {
                "bus_data_transfer_efficiency": 60.00,
                # "cycles_block": 6,
                "cycles_overhead": 4,
            },
            6,
        ),
        (
            {
                "bus_data_transfer_efficiency": 60.00,
                "cycles_block": 6,
                # "cycles_overhead": 4,
            },
            4,
        ),
    ],
)
def test_bus_data_transfer_efficiency(inputs, expected_result):
    assert solve_bus_data_transfer_efficiency(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "read_time_synchronous": TimeConverter().convert(0.00016, "s", "s"),
                "time_send_address": TimeConverter().convert(20, "µs", "s"),
                "time_memory_access": TimeConverter().convert(20, "µs", "s"),
                "time_send_data": TimeConverter().convert(120, "µs", "s"),
            },
            0.00016,
        ),
        (
            {
                "read_time_synchronous": TimeConverter().convert(0.00016, "s", "s"),
                # "time_send_address": TimeConverter().convert(20, "µs", "s"),
                "time_memory_access": TimeConverter().convert(20, "µs", "s"),
                "time_send_data": TimeConverter().convert(120, "µs", "s"),
            },
            TimeConverter().convert(20, "µs", "s"),
        ),
        (
            {
                "read_time_synchronous": TimeConverter().convert(0.00016, "s", "s"),
                "time_send_address": TimeConverter().convert(20, "µs", "s"),
                # "time_memory_access": TimeConverter().convert(20, "µs", "s"),
                "time_send_data": TimeConverter().convert(120, "µs", "s"),
            },
            TimeConverter().convert(20, "µs", "s"),
        ),
        (
            {
                "read_time_synchronous": TimeConverter().convert(0.00016, "s", "s"),
                "time_send_address": TimeConverter().convert(20, "µs", "s"),
                "time_memory_access": TimeConverter().convert(20, "µs", "s"),
                # "time_send_data": TimeConverter().convert(120, "µs", "s"),
            },
            TimeConverter().convert(120, "µs", "s"),
        ),
    ],
)
def test_read_time_synchronous(inputs, expected_result):
    assert pytest.approx(solve_read_time_synchronous(inputs)) == pytest.approx(
        expected_result
    )


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "read_time_asynchronous": TimeConverter().convert(0.0002, "s", "s"),
                "time_handshake": TimeConverter().convert(20, "µs", "s"),
                "time_memory_access": TimeConverter().convert(120, "µs", "s"),
            },
            TimeConverter().convert(0.0002, "s", "s"),
        ),
    ],
)
def test_read_time_asynchronous(inputs, expected_result):
    assert pytest.approx(solve_read_time_asynchronous(inputs)) == pytest.approx(
        expected_result
    )


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "bandwidth_max_for_bus": 40,
                "n_bytes_to_transfer": ByteConverter().convert(512, "b", "B"),
                "read_time_per_block": TimeConverter().convert(100, "ms", "s"),
                "n_blocks_total": 16,
            },
            40,
        ),
        (
            {
                "bandwidth_max_for_bus": 40,
                # "n_bytes_to_transfer": ByteConverter().convert(512, "b", "B"),
                "read_time_per_block": TimeConverter().convert(100, "ms", "s"),
                "n_blocks_total": 16,
            },
            ByteConverter().convert(512, "b", "B"),
        ),
        (
            {
                "bandwidth_max_for_bus": 40,
                "n_bytes_to_transfer": ByteConverter().convert(512, "b", "B"),
                # "read_time_per_block": TimeConverter().convert(100, "ms", "s"),
                "n_blocks_total": 16,
            },
            TimeConverter().convert(100, "ms", "s"),
        ),
        (
            {
                "bandwidth_max_for_bus": 40,
                "n_bytes_to_transfer": ByteConverter().convert(512, "b", "B"),
                "read_time_per_block": TimeConverter().convert(100, "ms", "s"),
                # "n_blocks_total": 16,
            },
            16,
        ),
    ],
)
def test_bandwidth_max_for_bus(inputs, expected_result):
    assert solve_bandwidth_max_for_bus(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "rotational_latency_time_sec": 0.03,
                "rotations_per_min": 2000
            },
            0.03,
        ),
        (
            {
                "rotational_latency_time_sec": 0.03,
                # "rotations_per_min": 2000
            },
            2000,
        ),
    ],
)
def test_rotational_latency_time_sec(inputs, expected_result):
    assert solve_rotational_latency_time_sec(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "disk_access_time_worst": TimeConverter().convert(0.13, "s", "s"),
                "time_rotational_latency": TimeConverter().convert(120, "ms", "s"),
                "time_head_seek": TimeConverter().convert(10, "ms", "s"),
            },
            TimeConverter().convert(0.13, "s", "s"),
        ),
        (
            {
                "disk_access_time_worst": TimeConverter().convert(0.13, "s", "s"),
                # "time_rotational_latency": TimeConverter().convert(120, "ms", "s"),
                "time_head_seek": TimeConverter().convert(10, "ms", "s"),
            },
            TimeConverter().convert(120, "ms", "s"),
        ),
        (
            {
                "disk_access_time_worst": TimeConverter().convert(0.13, "s", "s"),
                "time_rotational_latency": TimeConverter().convert(120, "ms", "s"),
                # "time_head_seek": TimeConverter().convert(10, "ms", "s"),
            },
            TimeConverter().convert(10, "ms", "s"),
        ),
    ],
)
def test_disk_access_time_worst(inputs, expected_result):
    assert solve_disk_access_time_worst(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "disk_access_time_avg": TimeConverter().convert(0.00500 , "s", "s"),
                "disk_access_time_worst": TimeConverter().convert(10, "ms", "s"),
            },
            TimeConverter().convert(0.00500, "s", "s"),
        ),
        (
            {
                "disk_access_time_avg": TimeConverter().convert(0.00500, "s", "s"),
                # "disk_access_time_worst": TimeConverter().convert(10, "ms", "s"),
            },
            TimeConverter().convert(10, "ms", "s"),
        ),
    ],
)
def test_disk_access_time_avg(inputs, expected_result):
    assert solve_disk_access_time_avg(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "track_size": 64,
                "sector_size": 4,
                "sectors_per_track": 16,
            },
            64,
        ),
        (
            {
                "track_size": 64,
                # "sector_size": 4,
                "sectors_per_track": 16,
            },
            4,
        ),
        (
            {
                "track_size": 64,
                "sector_size": 4,
                # "sectors_per_track": 16,
            },
            16,
        ),
    ],
)
def test_track_size(inputs, expected_result):
    assert solve_track_size(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "data_transfer_rate_disk": 460800.00000,
                "track_size": 64,
                "rotations_per_sec": 7200,
            },
            460800,
        ),
        (
            {
                "data_transfer_rate_disk": 460800.00000,
                # "track_size": 64,
                "rotations_per_sec": 7200,
            },
            64,
        ),
        (
            {
                "data_transfer_rate_disk": 460800.00000,
                "track_size": 64,
                # "rotations_per_sec": 7200,
            },
            7200,
        ),
    ],
)
def test_data_transfer_rate_disk(inputs, expected_result):
    assert solve_data_transfer_rate_disk(inputs) == expected_result
