from typing import Dict

import sympy as sp

from src.formula_utils import _get_result, _get_output_sym


def solve_compression_ratio(inputs: Dict) -> float:
    unit_map: Dict[str, str] = {
        "compression_ratio": "",
        "original_size": "",
        "compressed_size": "",
    }

    compression_ratio, original_size, compressed_size = sp.symbols(
        "compression_ratio original_size compressed_size"
    )
    equation = (original_size / compressed_size) - compression_ratio
    output_sym = _get_output_sym(
        inputs, [compression_ratio, original_size, compressed_size]
    )
    return _get_result(inputs, equation, output_sym, unit_map)
