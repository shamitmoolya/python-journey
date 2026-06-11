import pytest

from convert import convert

def test_int_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000

def test_error():
    with pytest.raises(TypeError):
        convert("1")
    with pytest.raises(TypeError):
        convert("cat")

def test_float_conversion():
    # assert convert(0.001) == pytest.approx(149597870.691)

    assert convert(0.001) == pytest.approx(149597870.691, abs=0.1)
    # here abs is tolerance i.e. +-0.1

    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-2)

