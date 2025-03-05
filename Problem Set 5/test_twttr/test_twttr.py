from twttr import shorten

def test_1():
    assert shorten("hello1") == "hll1"
    assert shorten("laptop!") == "lptp!"
def test_2():
    assert shorten("Ice cone") == "c cn"
    assert shorten("aei AEI") == " "