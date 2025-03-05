from project import simple_rec, aces_rec, split_rec

def test_simple_rec():
    assert simple_rec(18, 5) == "stand"
    assert simple_rec(7, 10) == "hit"
    assert simple_rec(9, 3) == "double"

def test_aces_rec():
    assert aces_rec(9, 6) == "stand"
    assert aces_rec(3, 5) == "double"
    assert aces_rec(7, 11) == "hit"

def test_split_rec():
    assert split_rec(11, 10) == "split"
    assert split_rec(10, 5) == "stand"
    assert split_rec(2, 8) == "hit"