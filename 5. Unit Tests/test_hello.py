from hello import hello

def test_default():
    assert hello() == "hello, World"

# def test_argument():
#     assert hello("David") == "hello, David"

def test_argument():
    for name in ["Hermonie", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"

# but keep tests simple so that you don't need tests for tests and so on.

