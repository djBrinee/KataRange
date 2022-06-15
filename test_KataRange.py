import pytest
from KataRange import RangeClass

c1 = RangeClass(2, 6)

def test_RangeContains():
    assert c1.Contains(2) == True

def test_GetAllPoints():
    assert c1.GetAllPoints() == "2,3,4,5"


