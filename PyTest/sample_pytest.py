import pytest

def test_upper():
    assert 'foo'.upper() == 'FOO'

@pytest.mark.parametrize("obj", ['1', '2', 'Foo'])
def test_isdigit(obj):
    try:
        assert obj.isdigit()
    except AssertionError as e:
        print(e)
