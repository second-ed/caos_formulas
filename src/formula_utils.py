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


def _solve_equation(equation, inputs, output_sym):
    print(equation)
    return sp.solve(equation.subs(inputs), output_sym)


def _get_output_sym(inputs, symbols):
    for sym in symbols:
        if str(sym) not in inputs:
            output_sym = sym
            return output_sym
    return None


def _get_result(inputs, equation, output_sym, unit_map) -> float:
    if output_sym:
        result = _solve_equation(equation, inputs, output_sym)[0]
        unit = unit_map[str(output_sym)]
        try:
            print(f"{result :.5f} {unit}")
        except TypeError as e:
            print(e)
        return float(result)
    else:
        raise ValueError("All inputs provided, no variable to solve for")
