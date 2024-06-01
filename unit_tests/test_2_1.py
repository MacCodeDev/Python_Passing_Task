import pytest
from task_2_1 import my_function

def test_my_function():
    assert my_function(1, 2, c=4) == 7
    assert my_function(1, 2) == 6
    assert my_function(0, 0, 0) == 0