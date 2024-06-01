import pytest
from task_2_2 import PowerGenerator

def test_power_generator():
    gen = PowerGenerator(2, 3)
    power = next(gen)
    assert power == 1

    power = next(gen)
    assert power == 2

    power = next(gen)
    assert power == 4

    power = next(gen)
    assert power == 8

    with pytest.raises(StopIteration):
        next(gen)