from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("hello you") == 0
def test_h():
    assert value("hey") == 20
    assert value("good evening") == 100