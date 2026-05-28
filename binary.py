"""dec 2 bin converter"""


def dec2bin(dec: int) -> str:
    """main function"""
    if not isinstance(dec, int) or isinstance(dec, bool):
        raise TypeError("not natural number")

    if dec < 0 or dec > 100:
        raise ValueError("not in 0, 100")

    if dec == 0:
        return "0"

    binary_str = ""
    while dec > 0:
        remainder = dec % 2
        binary_str = str(remainder) + binary_str
        dec = dec // 2

    return binary_str
