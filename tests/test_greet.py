from lib.greet import *

def test_greet_returns_hello_christina_for_christina():
    result = greet("Christina")
    assert result == "Hello, Christina!"