import pytest

from src.machine_code_programs import (
    ADD,
    DEC,
    DIV,
    EQ,
    GT,
    HALT,
    INC,
    LDI,
    LT,
    MUL,
    NZ,
    SUB,
    ZERO,
    run_program,
)


@pytest.mark.parametrize(
    "x, y, expected_result",
    [
        (0, 0, True),
        (1, 0, False),
        (0, 1, False),
        (1, 1, True),
    ],
)
def test_EQ(x, y, expected_result) -> None:
    assert EQ(x, y) == expected_result


@pytest.mark.parametrize(
    "x, y, expected_result",
    [
        (0, 0, False),
        (1, 0, False),
        (0, 1, True),
        (1, 1, False),
    ],
)
def test_LT(x, y, expected_result) -> None:
    assert LT(x, y) == expected_result


@pytest.mark.parametrize(
    "x, y, expected_result",
    [
        (0, 0, False),
        (1, 0, True),
        (0, 1, False),
        (1, 1, False),
    ],
)
def test_GT(x, y, expected_result) -> None:
    assert GT(x, y) == expected_result


@pytest.mark.parametrize(
    "x, expected_result",
    [
        (0, True),
        (1, False),
    ],
)
def test_ZERO(x, expected_result) -> None:
    assert ZERO(x) == expected_result


@pytest.mark.parametrize(
    "x, expected_result",
    [
        (1, True),
        (0, False),
    ],
)
def test_NZ(x, expected_result) -> None:
    assert NZ(x) == expected_result


@pytest.mark.parametrize(
    "memory, Rx, Ry, Rz, expected_result",
    [
        ([2, 3, 0], 0, 1, 2, [2, 3, 5]),
        ([2, 3, 0], 0, 1, 1, [2, 5, 0]),
        ([2, 3, 0], 0, 1, 0, [5, 3, 0]),
    ],
)
def test_ADD(memory, Rx, Ry, Rz, expected_result) -> None:
    ADD(memory, Rx, Ry, Rz)
    assert memory == expected_result


@pytest.mark.parametrize(
    "memory, Rx, Ry, Rz, expected_result",
    [
        ([2, 3, 0], 0, 1, 2, [2, 3, -1]),
        ([2, 3, 0], 0, 1, 1, [2, -1, 0]),
        ([2, 3, 0], 0, 1, 0, [-1, 3, 0]),
    ],
)
def test_SUB(memory, Rx, Ry, Rz, expected_result) -> None:
    SUB(memory, Rx, Ry, Rz)
    assert memory == expected_result


@pytest.mark.parametrize(
    "memory, Rx, Ry, Rz, expected_result",
    [
        ([2, 3, 0], 0, 1, 2, [2, 3, 6]),
        ([2, 3, 0], 0, 1, 1, [2, 6, 0]),
        ([2, 3, 0], 0, 1, 0, [6, 3, 0]),
    ],
)
def test_MUL(memory, Rx, Ry, Rz, expected_result) -> None:
    MUL(memory, Rx, Ry, Rz)
    assert memory == expected_result


@pytest.mark.parametrize(
    "memory, Rx, Ry, Rz, expected_result",
    [
        ([12, 3, 0], 0, 1, 2, [12, 3, 4]),
        ([12, 3, 0], 0, 1, 1, [12, 4, 0]),
        ([12, 3, 0], 0, 1, 0, [4, 3, 0]),
    ],
)
def test_DIV(memory, Rx, Ry, Rz, expected_result) -> None:
    DIV(memory, Rx, Ry, Rz)
    assert memory == expected_result


@pytest.mark.parametrize(
    "memory, Rx, nn, expected_result",
    [
        ([0, 0, 0], 0, 1, [1, 0, 0]),
        ([0, 0, 0], 1, 2, [0, 2, 0]),
        ([0, 0, 0], 2, 4, [0, 0, 4]),
    ],
)
def test_LDI(memory, Rx, nn, expected_result) -> None:
    LDI(memory, Rx, nn)
    assert memory == expected_result


# @pytest.mark.parametrize(
#     "memory, Rx, Ry, expected_result",
#     [
#         (memory, Rx, Ry, expected_result),
#     ]
# )
# def test_LOAD(memory, Rx, Ry, expected_result) -> None:
#     assert LOAD(memory, Rx, Ry) == expected_result


# @pytest.mark.parametrize(
#     "memory, Rx, Ry, expected_result",
#     [
#         (memory, Rx, Ry, expected_result),
#     ]
# )
# def test_STORE(memory, Rx, Ry, expected_result) -> None:
#     assert STORE(memory, Rx, Ry) == expected_result


@pytest.mark.parametrize(
    "memory, Rx, expected_result",
    [
        ([0, 0], 0, [1, 0]),
        ([0, 0], 1, [0, 1]),
        ([1, 0], 0, [2, 0]),
        ([1, 0], 1, [1, 1]),
    ],
)
def test_INC(memory, Rx, expected_result) -> None:
    INC(memory, Rx)
    assert memory == expected_result


@pytest.mark.parametrize(
    "memory, Rx, expected_result",
    [
        ([0, 0], 0, [-1, 0]),
        ([0, 0], 1, [0, -1]),
        ([1, 0], 0, [0, 0]),
        ([1, 0], 1, [1, -1]),
    ],
)
def test_DEC(memory, Rx, expected_result) -> None:
    DEC(memory, Rx)
    assert memory == expected_result


# @pytest.mark.parametrize(
#     "memory, Rx, Ry, comparison_op, expected_result",
#     [
#         (memory, Rx, Ry, comparison_op, expected_result),
#     ]
# )
# def test_CMP(memory, Rx, Ry, comparison_op, expected_result) -> None:
#     assert CMP(memory, Rx, Ry, comparison_op) == expected_result


# @pytest.mark.parametrize(
#     "memory, Rx, nn, comparison_op, expected_result",
#     [
#         (memory, Rx, nn, comparison_op, expected_result),
#     ]
# )
# def test_CMP_NN(memory, Rx, nn, comparison_op, expected_result) -> None:
#     assert CMP_NN(memory, Rx, nn, comparison_op) == expected_result


# @pytest.mark.parametrize(
#     "i, expected_result",
#     [
#         (i, expected_result),
#     ]
# )
# def test_JMP(i, expected_result) -> None:
#     assert JMP(i) == expected_result


# @pytest.mark.parametrize(
#     "i, condition, expected_result",
#     [
#         (i, condition, expected_result),
#     ]
# )
# def test_JMP_CC(i, condition, expected_result) -> None:
#     assert JMP_CC(i, condition) == expected_result


# @pytest.mark.parametrize(
#     ", expected_result",
#     [
#         (, expected_result),
#     ]
# )
# def test_HALT(, expected_result) -> None:
#     assert HALT() == expected_result


@pytest.mark.parametrize(
    "program, memory, expected_result",
    [
        (
            [
                (LDI, (1, 100)),
                (LDI, (2, 25)),
                (DIV, (1, 2, 3)),
                (HALT, ()),
            ],
            [0 for _ in range(16)],
            [0, 100, 25, 4.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ),
        (
            [
                (LDI, (1, 5)),
                (LDI, (2, 7)),
                (LDI, (3, 9)),
                (ADD, (1, 2, 1)),
                (ADD, (1, 3, 1)),
                (LDI, (4, 3)),
                (DIV, (1, 4, 1)),
                (HALT, ()),
            ],
            [0 for _ in range(16)],
            [0, 7.0, 7, 9, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ),
        (
            [
                (LDI, (0, 9)),
                (LDI, (1, 3)),
                (LDI, (2, 0)),
                (LDI, (3, 0)),
                (ADD, (0, 1, 2)),
                (MUL, (2, 0, 3)),
                (HALT, ()),
            ],
            [0 for _ in range(16)],
            [9, 3, 12, 108, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ),
        (
            [
                (LDI, (1, 3)),
                (LDI, (2, 5)),
                (LDI, (3, 6)),
                (LDI, (4, 4)),
                (LDI, (6, 0)),
                (MUL, (1, 2, 1)),
                (MUL, (3, 4, 3)),
                (SUB, (3, 1, 6)),
                (HALT, ()),
            ],
            [0 for _ in range(16)],
            [0, 15, 5, 24, 4, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ),
    ],
)
def test_run_program(program, memory, expected_result) -> None:
    assert run_program(program, memory) == expected_result
