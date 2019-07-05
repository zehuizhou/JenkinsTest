import pytest

print("12345678")
@pytest.fixture()
def test_1():
    assert 1 == 1