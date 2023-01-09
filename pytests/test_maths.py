"""
This module contains basic unit tests for math operations.
Their purpose is to show how to use the pytest framework by example. 
"""

# Basic test function
def test_one_plus_one():
    assert 1 + 1 == 2






# Test function to show assertion introspection
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c






# Test function that verifies an exception
def test_devide_by_zero():
    num = 1 / 0






# This contains basic unit tests for math operation
import pytest

# Test function
def test_one_plus_one():
    assert 1 + 1 == 2

# Test function verifies an exception
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    
    assert 'division by zero' in str(e.value)







# Multiplication tests

# two positive integers
# identity: multplying any number by 1
# zero: multplying any number by 0
# positive by a negative
# negative by a negative
# multiply floats

def test_multiply_two_positive_ints():
    assert 3 * 5 == 15

def test_multipy_identity():
    assert 1 * 2 == 2

def test_multiply_zero():
    assert 0 * 4 == 0 







# Parameterized test function
products = [
    (1, 3, 3),          #positive integers
    (1, 5, 5),          #identity
    (0, 5, 0),          #zero
    (2, -2, -4),        #positive by negative
    (-5, -5, 25),       #negative by negative
    (3.5, 6.2, 21.7)    #floats
]

@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product