import pytest
from task_2_4 import is_prime, find_twin_primes

def test_is_prime():
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(0)
    assert not is_prime(1)
    assert not is_prime(-3)

def test_find_twin_primes():
    assert find_twin_primes(1, 10) == [(3, 5), (5, 7)]
    assert find_twin_primes(10, 20) == [(11, 13), (17, 19)]
    assert find_twin_primes(20, 30) == [(29, 31)]
    assert find_twin_primes(30, 40) == []
    assert find_twin_primes(1, 1) == []