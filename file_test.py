import pytest
def test_5():
    a=2
    b=20
    resu=a+b
    assert resu

def test_6():
    x=10
    y=20
    assert x == y

def test_7():
    x=10
    y=10
    assert x == y

def some_test_2():         # invalid test case
    a=11
    b=22
    s=a+b
    assert s

@pytest.mark.regression
def test_some_03():
    x=22
    y=3
    d=x+y
    assert d

