import pytest
def test_001():
    a=2
    b=20
    resu=a+b
    assert resu

@pytest.mark.skip
def test_2():
    x=10
    y=20
    assert x == y

@pytest.mark.skipif(True)
def test_3():
    x=10
    y=10
    assert x == y

def some_test_01():         # invalid test case
    a=11
    b=22
    s=a+b
    assert s

def test_some():
    x=22
    y=3
    d=x+y
    assert d


