from src.add import add
import numpy as np

def test_add():
    assert add(1) == 101

def test2_add():
    a = add(np.array([1,2,3,4])) == np.array([101,102,103,104])
    assert a.all()
