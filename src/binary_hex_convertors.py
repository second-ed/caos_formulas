def num_to_binary(
    number,
    width: int = 4,
    use_pad: bool = True,
    use_sign: bool = True,
    show_working: bool = True,
) -> str:
    sign_pad = ""
    if number < 0:
        sign_pad += "-"
        number = abs(number)

    binarynumber = ""
    if number != 0:
        while number >= 1:
            if number % 2 == 0:
                if show_working:
                    print(f"{int(number)} % 2 == 0: add 0")
                binarynumber = binarynumber + "0"
                number //= 2
            else:
                if show_working:
                    print(f"{int(number)} % 2 != 0: add 1")
                binarynumber = binarynumber + "1"
                number = (number - 1) // 2

    else:
        binarynumber = "0"

    res: str = "".join(reversed(binarynumber))

    while len(res) > width:
        width += 4

    if use_pad:
        pad = "0" * (width - len(res))
        res = pad + res
    if use_sign:
        res = sign_pad + res

    return res


def binary_to_num(binary_str: str, show_working: bool = True) -> int:
    if binary_str[0] == "-":
        mult = -1
    else:
        mult = 1
    result = 0
    for i, bit in enumerate(reversed(binary_str)):
        if bit == "1":
            value = 2**i
            if show_working:
                print(f"bit == 1: adding {value} (2^{i})")
            result += value
        else:
            if show_working:
                print("bit == 0: adding 0")
    return result * mult


def num_to_hexadecimal(number, show_working: bool = True) -> str:
    sign_pad = ""
    hex_characters = "0123456789ABCDEF"
    if number == 0:
        return "0X0"
    if number < 0:
        sign_pad += "-"
        number = abs(number)

    hexadecimal = ""
    while number > 0:
        remainder = number % 16
        if show_working:
            print(f"{number} % 16 == {remainder}: add {hex_characters[remainder]}")
        hexadecimal = hex_characters[remainder] + hexadecimal
        number //= 16

    return sign_pad + "0X" + hexadecimal


def hexadecimal_to_num(hex_str: str, show_working: bool = True) -> int:
    if hex_str[0] == "-":
        mult = -1
    else:
        mult = 1
    hex_characters = "0123456789ABCDEF"
    result = 0
    for i, digit in enumerate(reversed(hex_str.upper().lstrip("-0X"))):
        if digit not in hex_characters:
            raise ValueError(f"Invalid hexadecimal character: {digit}")
        value = hex_characters.index(digit)
        value = 16**i * value
        if show_working:
            print(f"element == {digit}:  adding {value} (16^{i} * {value})")
        result += value
    return mult * result
