import numpy as np
import sympy as sp
import pytest

from src.formulas import (
    ByteConverter,
    HertzConverter,
    TimeConverter,
    _get_output_sym,
    _get_result,
    solve_address_locations,
    solve_asynchronous_bus_max_bandwidth,
    solve_avg_memory_read_time,
    solve_branch_prediction,
    solve_cache_avg_read_time,
    solve_clock_freq,
    solve_data_transfer_efficiency,
    solve_data_transfer_rate,
    solve_gustafsons_law,
    solve_max_speedup,
    solve_memory_data_rate,
    solve_probability_of_failure,
    solve_probability_of_no_failure,
    solve_reads_per_sec,
    solve_storage_capacity,
    solve_synchronous_bus_max_bandwidth,
    solve_true_speedup,
)


@pytest.mark.parametrize(
    "converter, from_unit, to_unit",
    [
        (ByteConverter(), "GB", "blah"),
        (ByteConverter(), "blah", "MB"),
        (HertzConverter(), "GHz", "blah"),
        (HertzConverter(), "blah", "MHz"),
        (TimeConverter(), "ms", "blah"),
        (TimeConverter(), "blah", "µs"),
    ],
)
def test_raises_converter(converter, from_unit, to_unit):
    with pytest.raises(ValueError):
        converter.convert(1, from_unit, to_unit)


@pytest.mark.parametrize(
    "inputs, symbols, expected_result",
    [
        ({"a": 1, "b": 2, "c": 3}, [*sp.symbols("a b c")], None),
        ({"a": 1, "b": 2}, [*sp.symbols("a b c")], sp.Symbol("c")),
    ],
)
def test_get_output_sym(inputs, symbols, expected_result):
    assert _get_output_sym(inputs, symbols) == expected_result


def test_raises_get_result():
    with pytest.raises(ValueError):
        _get_result({}, [], None, {})


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({"f": 100}, 0.01),
        ({"t": 0.01}, 100),
    ],
)
def test_solve_clock_freq(inputs, expected_result) -> None:
    assert float(solve_clock_freq(inputs)) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({"P": 0.5}, 2.0),
        ({"P": 0.2}, 1.25),
        ({"P": 0.99}, 100),
        ({"max_speedup": 2.0}, 0.5),
        ({"max_speedup": 4.0}, 0.75),
    ],
)
def test_solve_max_speedup(inputs, expected_result) -> None:
    assert float(solve_max_speedup(inputs)) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({"P": 0.5, "n": 3}, 1.5),
        ({"P": 0.5, "true_speedup": 1.5}, 3),
        ({"true_speedup": 1.5, "n": 3}, 0.5),
    ],
)
def test_solve_true_speedup(inputs, expected_result) -> None:
    assert float(solve_true_speedup(inputs)) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({"P": 0.5, "n": 4}, 2.5000000),
        ({"P": 0.5, "speedup": 2.5}, 4),
        ({"speedup": 2.5, "n": 4}, 0.5),
    ],
)
def test_solve_gustafsons_law(inputs, expected_result) -> None:
    assert float(solve_gustafsons_law(inputs)) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                "cycles_saved": 3,
                "cycles_cost": 2,
                "p_correct": 0.4,
                "p_incorrect": 0.6,
                # "total_savings": 0,
            },
            0,
        ),
        (
            {
                "cycles_saved": 3,
                "cycles_cost": 2,
                # "p_correct": 0.4,
                "p_incorrect": 0.6,
                "total_savings": 0,
            },
            0.4,
        ),
        (
            {
                # "cycles_saved": 3,
                "cycles_cost": 2,
                "p_correct": 0.4,
                "p_incorrect": 0.6,
                "total_savings": 0,
            },
            3,
        ),
        (
            {
                "cycles_saved": 3,
                # "cycles_cost": 2,
                "p_correct": 0.4,
                "p_incorrect": 0.6,
                "total_savings": 0,
            },
            2,
        ),
    ],
)
def test_solve_branch_prediction(inputs, expected_result) -> None:
    assert np.allclose(float(solve_branch_prediction(inputs)), expected_result)


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "reads_per_sec": 266600000.0,
                "freq": HertzConverter().convert(1333, "MHz", "Hz"),
                "clocks_per_read": 5,
            },
            266600000.0,
        ),
        (
            {
                "reads_per_sec": 266600000.0,
                # "freq": HertzConverter().convert(1333, "MHz", "Hz"),
                "clocks_per_read": 5,
            },
            HertzConverter().convert(1333, "MHz", "Hz"),
        ),
        (
            {
                "reads_per_sec": 266600000.0,
                "freq": HertzConverter().convert(1333, "MHz", "Hz"),
                # "clocks_per_read": 5,
            },
            5,
        ),
    ],
)
def test_solve_reads_per_sec(inputs, expected_result) -> None:
    assert float(solve_reads_per_sec(inputs)) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({"address_locations": 65536}, 16.0),
        ({"address_lines": 16}, 65536),
    ],
)
def test_solve_address_locations(inputs, expected_result) -> None:
    assert float(solve_address_locations(inputs)) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        ({"address_lines": 32, "data_lines": 64}, 34359738368.0000),
    ],
)
def test_solve_storage_capacity(inputs, expected_result) -> None:
    assert float(solve_storage_capacity(inputs)) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                "access_time": 5,
                "recovery_cycles": 2,
                "ras_cycles": 1,
                "cas_cycles": 1,
            },
            9,
        ),
    ],
)
def test_solve_avg_memory_read_time(inputs, expected_result) -> None:
    assert float(solve_avg_memory_read_time(inputs)) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                "memory_read_time": 5,
                "memory_width": ByteConverter().convert(32, "b", "B"),
                "clock_rate": HertzConverter().convert(1, "GHz", "Hz"),
            },
            800000000,
        ),
    ],
)
def test_solve_memory_data_rate(inputs, expected_result) -> None:
    assert float(solve_memory_data_rate(inputs)) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                "p_cache": 0.9,
                "sram": 1.0,
                "dram": 3.0,
                "ras": 1.0,
                "cas": 1.0,
            },
            3.300,
        ),
    ],
)
def test_solve_cache_avg_read_time(inputs, expected_result) -> None:
    assert float(solve_cache_avg_read_time(inputs)) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                "protocol_overhead": 5,
                "bus_width": ByteConverter().convert(32, "b", "B"),
                "bus_frequency": HertzConverter().convert(200, "MHz", "Hz"),
            },
            133333333.333333,
        ),
        (
            {
                "protocol_overhead": 5,
                "bus_width": ByteConverter().convert(32, "b", "B"),
                "bus_frequency": HertzConverter().convert(240, "MHz", "Hz"),
                # "data_transfer_rate": 160000000.000000,
            },
            160000000.000000,
        ),
        (
            {
                "protocol_overhead": 5,
                "bus_width": ByteConverter().convert(32, "b", "B"),
                # "bus_frequency": HertzConverter().convert(240, "MHz", "Hz"),
                "data_transfer_rate": 160000000.000000,
            },
            HertzConverter().convert(240, "MHz", "Hz"),
        ),
        (
            {
                "protocol_overhead": 5,
                # "bus_width": ByteConverter().convert(32, "b", "B"),
                "bus_frequency": HertzConverter().convert(240, "MHz", "Hz"),
                "data_transfer_rate": 160000000.000000,
            },
            ByteConverter().convert(32, "b", "B"),
        ),
        (
            {
                # "protocol_overhead": 5,
                "bus_width": ByteConverter().convert(32, "b", "B"),
                "bus_frequency": HertzConverter().convert(240, "MHz", "Hz"),
                "data_transfer_rate": 160000000.000000,
            },
            5,
        ),
    ],
)
def test_solve_data_transfer_rate(inputs, expected_result) -> None:
    assert float(solve_data_transfer_rate(inputs)) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                "protocol_overhead": 4,
                "bus_width": ByteConverter().convert(4, "B", "B"),
                "block_size": ByteConverter().convert(16, "B", "B"),
                # "data_transfer_efficiency": 0.5,
            },
            0.5,
        ),
        (
            {
                "protocol_overhead": 4,
                "bus_width": ByteConverter().convert(4, "B", "B"),
                # "block_size": ByteConverter().convert(16, "B", "B"),
                "data_transfer_efficiency": 0.5,
            },
            16,
        ),
        (
            {
                "protocol_overhead": 4,
                # "bus_width": ByteConverter().convert(4, "B", "B"),
                "block_size": ByteConverter().convert(16, "B", "B"),
                "data_transfer_efficiency": 0.5,
            },
            4,
        ),
        (
            {
                # "protocol_overhead": 4,
                "bus_width": ByteConverter().convert(4, "B", "B"),
                "block_size": ByteConverter().convert(16, "B", "B"),
                "data_transfer_efficiency": 0.5,
            },
            4,
        ),
    ],
)
def test_solve_data_transfer_efficiency(inputs, expected_result) -> None:
    assert float(solve_data_transfer_efficiency(inputs)) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                "bus_frequency": HertzConverter().convert(10, "Hz", "Hz"),
                "bus_width": ByteConverter().convert(10, "B", "B"),
                "clock_cycle_time": TimeConverter().convert(10, "ns", "s"),
                "ras": 0.5,
                "cas": 0.5,
                "send_clocks": 1,
                "memory_access_time": TimeConverter().convert(20, "ns", "s"),
                # "maximum_bandwidth": 250000000.000000,
            },
            250000000.000000,
        ),
        (
            {
                "bus_frequency": HertzConverter().convert(10, "Hz", "Hz"),
                "bus_width": ByteConverter().convert(10, "B", "B"),
                "clock_cycle_time": TimeConverter().convert(10, "ns", "s"),
                "ras": 0.5,
                "cas": 0.5,
                "send_clocks": 1,
                # "memory_access_time": TimeConverter().convert(20, "ns", "s"),
                "maximum_bandwidth": 250000000.000000,
            },
            TimeConverter().convert(20, "ns", "s"),
        ),
        (
            {
                "bus_frequency": HertzConverter().convert(10, "Hz", "Hz"),
                "bus_width": ByteConverter().convert(10, "B", "B"),
                "clock_cycle_time": TimeConverter().convert(10, "ns", "s"),
                "ras": 0.5,
                "cas": 0.5,
                # "send_clocks": 1,
                "memory_access_time": TimeConverter().convert(20, "ns", "s"),
                "maximum_bandwidth": 250000000.000000,
            },
            1,
        ),
        (
            {
                "bus_frequency": HertzConverter().convert(10, "Hz", "Hz"),
                "bus_width": ByteConverter().convert(10, "B", "B"),
                "clock_cycle_time": TimeConverter().convert(10, "ns", "s"),
                "ras": 0.5,
                # "cas": 0.5,
                "send_clocks": 1,
                "memory_access_time": TimeConverter().convert(20, "ns", "s"),
                "maximum_bandwidth": 250000000.000000,
            },
            0.5,
        ),
        (
            {
                "bus_frequency": HertzConverter().convert(10, "Hz", "Hz"),
                "bus_width": ByteConverter().convert(10, "B", "B"),
                "clock_cycle_time": TimeConverter().convert(10, "ns", "s"),
                # "ras": 0.5,
                "cas": 0.5,
                "send_clocks": 1,
                "memory_access_time": TimeConverter().convert(20, "ns", "s"),
                "maximum_bandwidth": 250000000.000000,
            },
            0.5,
        ),
        (
            {
                "bus_frequency": HertzConverter().convert(10, "Hz", "Hz"),
                "bus_width": ByteConverter().convert(10, "B", "B"),
                # "clock_cycle_time": TimeConverter().convert(10, "ns", "s"),
                "ras": 0.5,
                "cas": 0.5,
                "send_clocks": 1,
                "memory_access_time": TimeConverter().convert(20, "ns", "s"),
                "maximum_bandwidth": 250000000.000000,
            },
            TimeConverter().convert(10, "ns", "s"),
        ),
        (
            {
                "bus_frequency": HertzConverter().convert(10, "Hz", "Hz"),
                # "bus_width": ByteConverter().convert(10, "B", "B"),
                "clock_cycle_time": TimeConverter().convert(10, "ns", "s"),
                "ras": 0.5,
                "cas": 0.5,
                "send_clocks": 1,
                "memory_access_time": TimeConverter().convert(20, "ns", "s"),
                "maximum_bandwidth": 250000000.000000,
            },
            ByteConverter().convert(10, "B", "B"),
        ),
    ],
)
def test_solve_synchronous_bus_max_bandwidth(inputs, expected_result) -> None:
    assert float(solve_synchronous_bus_max_bandwidth(inputs)) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                "bus_width": ByteConverter().convert(10, "B", "B"),
                "handshake_time": TimeConverter().convert(50, "ns", "s"),
                "memory_access_time": TimeConverter().convert(250, "ns", "s"),
                # "maximum_bandwidth": 14035087.7192982,
            },
            22222222.2222222,
        ),
    ],
)
def test_solve_asynchronous_bus_max_bandwidth(inputs, expected_result) -> None:
    assert float(solve_asynchronous_bus_max_bandwidth(inputs)) == pytest.approx(
        expected_result
    )


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {"n": 2, "P_failure": 0.000025},
            -0.005,
        ),
        (
            {"P": 0.005, "P_failure": 0.000025},
            2,
        ),
        (
            {
                "P": 0.005,
                "n": 2,
            },
            0.000025,
        ),
    ],
)
def test_solve_probability_of_failure(inputs, expected_result) -> None:
    assert float(solve_probability_of_failure(inputs)) == pytest.approx(expected_result)


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {"n": 3, "P_failure": 0.985074875},
            0.005,
        ),
        (
            {"P": 0.005, "P_failure": 0.985074875},
            3,
        ),
        (
            {"P": 0.005, "n": 3},
            0.985074875,
        ),
    ],
)
def test_solve_probability_of_no_failure(inputs, expected_result) -> None:
    assert float(solve_probability_of_no_failure(inputs)) == pytest.approx(
        expected_result
    )
