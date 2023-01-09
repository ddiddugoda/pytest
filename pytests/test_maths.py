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