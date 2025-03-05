from um import count

def test_count1():
    assert count("um,") == 1
    assert count("yummy") == 0

def test_count2():
    assert count("Um,") == 1
    assert count("UM UM...") == 2

def test_count3():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2