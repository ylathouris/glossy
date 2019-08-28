import collections
import time
import pytest

from glossy import decorator, Decorated


@decorator
def timer(func, *args, **kwargs):
    """
    Timer

    This decorator function is used to time the given
    function execution.
    """
    start = time.time()
    result = func(*args, **kwargs)
    duration = time.time() - start
    print(f"Function {func.__name__} took {duration} seconds")
    return result


def timeout(limit=5):
    """
    Timeout

    This decorator is used to raise a timeout error when the
    given function exceeds the given timeout limit.
    """

    @decorator
    def _timeout(func, *args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        if duration > limit:
            msg = f"Function {func.__name__} exceeded timeout limit ({limit} seconds)"
            raise TimeoutError(msg)

        return result

    return _timeout


@timer
@timeout(limit=0.5)
def delay(seconds=0.25):
    """
    Delay

    This function sleeps for the given number of seconds
    before returning a value. It has two decorators, one
    to measure how long the function takes to run and
    another to raise a timeout error if the function
    takes longer than 0.5 seconds.
    """
    time.sleep(seconds)
    return "Finished!"


def dummy_decorator():
    pass


def test_glossy_decorator_returns_decorated_object():
    assert isinstance(delay, Decorated)


def test_decorated_repr_returns_expected():
    assert repr(delay).startswith("<glossy.Decorated(delay) at")


def test_decorated_has___wrappers___property():
    assert hasattr(delay, "__wrappers__")


def test_wrapped_property_returns_original_function():
    assert delay.wrapped == delay.__wrapped__


def test_decorators_property_returns_expected():
    expected = [timeout, timer]
    for index, source in enumerate(delay.decorators):
        target = expected[index]
        assert source.__module__ == target.__module__
        assert source.__name__ == target.__name__


def test_get_decorator_info_with_valid_decorator_returns_info():
    expected = {
        "obj": timeout,
        "name": timeout.__name__,
        "args": [],
        "kwargs": collections.OrderedDict({"limit": 0.5}),
    }
    info = delay.get_decorator_info(timeout)
    assert info == expected


def test_get_decorator_info_with_invalid_decorator_returns_none():
    info = delay.get_decorator_info(dummy_decorator)
    assert info is None


def test_mock_timeout_decorator_no_parameters():
    # Throws error when not mocked
    with pytest.raises(TimeoutError):
        delay(0.75)

    # Passes when mocked
    delay.mock(timeout)
    delay(0.75)


def test_mock_decorator_that_doesnt_exist_raises_value_error():
    with pytest.raises(ValueError):
        delay.mock(dummy_decorator)
