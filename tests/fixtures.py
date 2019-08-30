import pytest

from glossy import decorated


@pytest.fixture(autouse=True)
def clear_mocks():
    """
    Clear Mocks

    This fixture is used to clear all mocks automatically after
    each test.
    """
    yield
    decorated.clear_mocks()
