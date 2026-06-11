# from calculator import square

# def main():
#     test_square()

# def test_square():
    # if square(2) != 4:
    #     print("2 squared was not 4.")
    # if square(3) != 9:
    #     print("3 squared was not 9.")
# but the testing code has becoem lengthier thanb the original code itself so we can use another keyword in python, namely "assert".


# If assert case is true then it'll give no error but if the boolean in assert is false then it'll give us an AssertionError.
    # assert square(2) == 4
    # assert square(3) == 9


# deal with errors we use try:
# Try for the corner cases:
    # try:
    #     assert square(2) == 4
    # except AssertionError:
    #     print("2 squared was not 4.")
    # try:
    #     assert square(3) == 9
    # except AssertionError:
    #     print("3 squared was not 9.")
    # try:
    #     assert square(-2) == 4
    # except AssertionError:
    #     print("-2 squared was not 4.")
    # try:
    #     assert square(-3) == 9
    # except AssertionError:
    #     print("-3 squared was not 9.")
    # try:
    #     assert square(0) == 0
    # except AssertionError:
    #     print("0 squared was not 0.")
# But this is also too much code for testing.

# if __name__ == "__main__":
#     main()

# So therres as 3rd party library called pytest. These can be used for unit testing i.e. test individual unit functions in code.

# from calculator import square

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(-3) == 9
    # assert square(0) == 0
# install = pip install pytest

# no need of main function in code for pytest. It'll handle the try except print block itself so no need to add it yourself.

# to run - pytest test_calculator.py 

# but if assert square(3) == 9 failed then it won't check for next lines so lets break test_sqaure 
from calculator import square
import pytest

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0
# pytest will test all 3 functions. if one fails then still other 2 will be executed.

def test_str():
    with pytest.raises(TypeError):
        square("cat")


