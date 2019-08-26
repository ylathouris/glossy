import gloss
import pytest

from .. import examples


def xtest_mock_decorator_on_func_with_no_decorators_raises_error():
    func = examples.get_function("with_no_decorators")
    with pytest.raises(ValueError):
        gloss.mock(func, "@timer")
