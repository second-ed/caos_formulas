import pytest

from src.formula_utils import ByteConverter, TimeConverter
from src.week6_formulas import *


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "total_network_bandwidth": 390.,
                "raw_bandwidth": 200,
                "bridge_bandwidth": 10,
            },
            390,
        ),
        (
            {
                "total_network_bandwidth": 390.0,
                # "raw_bandwidth": 200,
                "bridge_bandwidth": 10,
            },
            200,
        ),
        (
            {
                "total_network_bandwidth": 390.0,
                "raw_bandwidth": 200,
                # "bridge_bandwidth": 10,
            },
            10,
        ),
    ],
)
def test_total_network_bandwidth(inputs, expected_result):
    assert solve_total_network_bandwidth(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "packet_bytes_total": ByteConverter().convert(200, "B", "B"),
                "packet_bytes_payload": ByteConverter().convert(100, "B", "B"),
                "packet_bytes_overhead": ByteConverter().convert(100, "B", "B"),
            },
            ByteConverter().convert(200, "B", "B"),
        ),
        (
            {
                "packet_bytes_total": ByteConverter().convert(200, "B", "B"),
                # "packet_bytes_payload": ByteConverter().convert(100, "B", "B"),
                "packet_bytes_overhead": ByteConverter().convert(100, "B", "B"),
            },
            ByteConverter().convert(100, "B", "B"),
        ),
        (
            {
                "packet_bytes_total": ByteConverter().convert(200, "B", "B"),
                "packet_bytes_payload": ByteConverter().convert(100, "B", "B"),
                # "packet_bytes_overhead": ByteConverter().convert(100, "B", "B"),
            },
            ByteConverter().convert(100, "B", "B"),
        ),
    ],
)
def test_packet_bytes_total(inputs, expected_result):
    assert solve_packet_bytes_total(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "true_data_rate": 360,
                "raw_data_rate": 600,
                "efficiency": 0.6,
            },
            360,
        ),
        (
            {
                "true_data_rate": 360,
                # "raw_data_rate": 600,
                "efficiency": 0.6,
            },
            600,
        ),
        (
            {
                "true_data_rate": 360,
                "raw_data_rate": 600,
                # "efficiency": 0.6,
            },
            0.6,
        ),
    ],
)
def test_true_data_rate(inputs, expected_result):
    assert solve_true_data_rate(inputs) == expected_result


@pytest.mark.parametrize(
    "inputs, expected_result",
    [
        (
            {
                # "packet_latency": TimeConverter().convert(8, "s", "s"),
                "packet_size": ByteConverter().convert(512, "B", "B"),
                "raw_data_rate": 64,
            },
            TimeConverter().convert(8, "s", "s"),
        ),
        (
            {
                "packet_latency": TimeConverter().convert(8, "s", "s"),
                # "packet_size": ByteConverter().convert(512, "B", "B"),
                "raw_data_rate": 64,
            },
            ByteConverter().convert(512, "B", "B"),
        ),
        (
            {
                "packet_latency": TimeConverter().convert(8, "s", "s"),
                "packet_size": ByteConverter().convert(512, "B", "B"),
                # "raw_data_rate": 64,
            },
            64,
        ),
    ],
)
def test_packet_latency(inputs, expected_result):
    assert solve_packet_latency(inputs) == expected_result
