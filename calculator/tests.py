import unittest
from pkg.calculator import Calculator

calculator = Calculator()

def test_addition():
    result = calculator.evaluate("3 + 5")
    assert result == 8
    print("test_addition passed")

def test_subtraction():
    result = calculator.evaluate("10 - 4")
    assert result == 6
    print("test_subtraction passed")

def test_multiplication():
    result = calculator.evaluate("3 * 4")
    assert result == 12
    print("test_multiplication passed")

def test_division():
    result = calculator.evaluate("10 / 2")
    assert result == 5
    print("test_division passed")

def test_nested_expression():
    result = calculator.evaluate("3 * 4 + 5")
    assert result == 17
    print("test_nested_expression passed")

def test_complex_expression():
    result = calculator.evaluate("2 * 3 - 8 / 2 + 5")
    assert result == 7
    print("test_complex_expression passed")

def test_empty_expression():
    result = calculator.evaluate("")
    assert result is None
    print("test_empty_expression passed")

def test_invalid_operator():
    try:
        calculator.evaluate("$ 3 5")
    except ValueError:
        print("test_invalid_operator passed")
        return
    assert False

def test_not_enough_operands():
    try:
        calculator.evaluate("+ 3")
    except ValueError:
        print("test_not_enough_operands passed")
        return
    assert False


test_addition()
test_subtraction()
test_multiplication()
test_division()
test_nested_expression()
test_complex_expression()
test_empty_expression()
test_invalid_operator()
test_not_enough_operands()