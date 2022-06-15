import pytest
from KataRange import RangeClass

c1 = RangeClass(2, 6)
c2 = RangeClass(2, 5)

def test_RangeContains():
    assert c1.Contains(2) == True

def test_GetAllPoints():
    assert c1.GetAllPoints() == "2,3,4,5"

def test_NoContain():
    assert c2.Contains(100) == False
    
def test_EndPoints():
    assert c1.EndPoints() == "2,5"
