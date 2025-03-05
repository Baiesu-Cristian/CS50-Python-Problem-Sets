from plates import is_valid

def test_1():
    assert is_valid("ABC123") == True
    assert is_valid("ABC!!!") == False

def test_2():
    assert is_valid("A") == False
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("11") == False
    assert is_valid("ABCD123") == False

def test_3():
    assert is_valid("AB12CD") == False
    assert is_valid("ABC012") == False