from string import digits, ascii_letters


def encode_to_base62(index: int) -> str:
    symbols = digits + ascii_letters
    result = ""

    while index > 0:
        remainder = index % 62
        result = symbols[remainder] + result
        index //= 62

    return result.rjust(7, "0")
