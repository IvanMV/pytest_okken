import pytest

@pytest.mark.parametrize('value, expected',[(10, 20), (7, 15), (-1, -2)])
def test_double(value, expected):
    assert value*2 == expected
    
@pytest.mark.parametrize('value, expected',[(10, 20), ("a", "a*2"), (-1, -2)])
def test_double_eval(value, expected):
    assert eval(value*2) == expected
    
@pytest.mark.parametrize('value, expected',[("10*2", 20), ("a*2", "a*2"), (-1, -2)])
def test_double_eval_new(value, expected):
    assert eval(value) == expected