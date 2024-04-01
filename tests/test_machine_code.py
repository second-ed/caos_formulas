import pytest

from src.machine_code_programs import ADD, EQ, GT, LT, MUL, NZ, SUB, ZERO


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
    ],
)
def test_MUL(memory, Rx, Ry, Rz, expected_result) -> None:
    MUL(memory, Rx, Ry, Rz)
    assert memory == expected_result


# @pytest.mark.parametrize(
#     "memory, Rx, Ry, Rz, expected_result",
#     [
#         (memory, Rx, Ry, Rz, expected_result),
#     ]
# )
# def test_DIV(memory, Rx, Ry, Rz, expected_result) -> None:
#     assert DIV(memory, Rx, Ry, Rz) == expected_result


# @pytest.mark.parametrize(
#     "memory, Rx, nn, expected_result",
#     [
#         (memory, Rx, nn, expected_result),
#     ]
# )
# def test_LDI(memory, Rx, nn, expected_result) -> None:
#     assert LDI(memory, Rx, nn) == expected_result


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


# @pytest.mark.parametrize(
#     "memory, Rx, expected_result",
#     [
#         (memory, Rx, expected_result),
#     ]
# )
# def test_INC(memory, Rx, expected_result) -> None:
#     assert INC(memory, Rx) == expected_result


# @pytest.mark.parametrize(
#     "memory, Rx, expected_result",
#     [
#         (memory, Rx, expected_result),
#     ]
# )
# def test_DEC(memory, Rx, expected_result) -> None:
#     assert DEC(memory, Rx) == expected_result


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


# @pytest.mark.parametrize(
#     "program, memory, expected_result",
#     [
#         (program, memory, expected_result),
#     ]
# )
# def test_run_program(program, memory, expected_result) -> None:
#     assert run_program(program, memory) == expected_result
