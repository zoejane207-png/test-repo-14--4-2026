from lib.high_value import *

def test_returns_value_first_as_higher():
    high_value = HighValue(10, 5)
    result = high_value.get_highest()
    assert result == "First value is higher"

def test_returns_value_second_as_higher():
    high_value = HighValue(2, 5)
    result = high_value.get_highest()
    assert result == "Second value is higher"

def test_returns_values_as_equal():
    high_value = HighValue(5, 5)
    result = high_value.get_highest()
    assert result == "Values are equal"

