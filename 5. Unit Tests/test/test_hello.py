from hello import hello

def test_default():
    assert hello() == "hello, World"


def test_argument():
    assert hello("David") == "hello, David"


# to run test on whole folder :
# pytest test

# but you will have to add __init__.py in your folder to make it a package.