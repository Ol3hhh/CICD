import pytest
import binary


@pytest.mark.parametrize(
    "dec, expected",
    [(0, "0"), (1, "1"), (5, "101"), (25, "11001"), (15, "1111"), (100, "1100100")],
)
def test_dec2bin_correct_conversion(dec, expected):
    assert binary.dec2bin(dec) == expected


@pytest.mark.parametrize("invalid_dec", [-1, -5, 101, 200])
def test_dec2bin_out_of_range(invalid_dec):
    with pytest.raises(ValueError):
        binary.dec2bin(invalid_dec)


@pytest.mark.parametrize("non_int", [5.5, 0.1, 99.9])
def test_dec2bin_not_an_integer(non_int):
    with pytest.raises(TypeError):
        binary.dec2bin(non_int)
