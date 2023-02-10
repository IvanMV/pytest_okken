import pytest

def test_one():
    with pytest.raises(TypeError):
        x = '12'
        y = 100
        y/x
        