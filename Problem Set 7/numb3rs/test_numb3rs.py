from numb3rs import validate

def test_validate1():
    assert validate("1.2.3.4.5") == False
    assert validate("1.2.3.4") == True
    assert validate("1.2.3") == False

def test_validate2():
    assert validate("512.0.0.0") == False
    assert validate("0.512.0.0") == False