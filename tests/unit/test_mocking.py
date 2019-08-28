import glossy
import pytest

from .. import examples


def test_mock_decorator_on_func_with_no_decorators_raises_error():
    func = examples.get_function("with_no_decorators")
    decorator = examples.get_decorator("simple")
    with pytest.raises(AttributeError):
        getattr(func, "mock")(func, decorator)
