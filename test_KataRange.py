import pytest
from KataRange import RangeClass

c1 = RangeClass(1, 6)

def test_RangeContains():
    assert c1.Contains(2) == True


