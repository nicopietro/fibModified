from fib import fibonacci_iterative, fibonacci_recursive2
import pytest

def test_fib_9_is_34():
    assert fibonacci_iterative(9) == 34

def test_fib_negative_raise_error():
    with pytest.raises(ValueError):
        fibonacci_iterative(-1)

def test_fib_req_9_is_34():
    assert fibonacci_recursive2(9) == 34

def test_fib_req_negative_raise_error():
    with pytest.raises(ValueError):
        fibonacci_recursive2(-1)