from src.add import add
import numpy as np

def test_add():
    assert add(1) == 101

def test2_add():
    a = add(np.array([1,2,3,4])) == np.array([101,102,103,104])
    assert a.all()

def test3_add():
    a = add(np.array([1,2,3,4]),np.array([1,2,3,4])) == np.array([2,4,6,8])
    assert a.all()

def test4_add():
    assert add("3","4") == "34"
