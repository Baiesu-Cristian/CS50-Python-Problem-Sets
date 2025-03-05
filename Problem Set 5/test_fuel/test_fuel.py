from fuel import convert
from fuel import gauge
import pytest

def test_c():
    assert convert("1/2") == 50

def test_g():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"

def test_ve():
    with pytest.raises(ValueError):
        convert("2/1")

def test_zde():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")