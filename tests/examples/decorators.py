import functools
import time


def simple(func):
    """
    Simple Decorator

    This is a simple decorator function. It takes the function
    being decorating as input and returns a wrapped version of that
    function as output. This makes it possible to inject custom
    logic berore and after the function execution.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Function Wrapper

        This is the wrapper function which allows users to inject
        logic before and after the given decorated function.
        """
        result = func(*args, **kwargs)
        return result

    return wrapper


def fancy(options="some_options"):
    """
    Fancy Decorator

    This is a slightly more complex decorator. Instead of taking
    the decorated function as input, it accepts some options and
    then returns a simple decorator like the one in the example above.
    This allows the behaviour of the decorator to be configurable.
    """

    def simple(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result

        return wrapper

    return simple


def timer(func):
    """
    Timer Decorator

    This is an example of a simple decorator function. It takes the
    function being decorating as input and returns a wrapper. In this
    case, the wrapper is used to time the execution of the decorated
    function.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        duration = time.time() - start
        print(f"Function {func.__name__} took {duration} second(s)")
        return return_value

    return wrapper


def timeout(limit=5):
    """
    Timeout Decorator

    This is an example of a fancy decorator. It takes some
    configuration options and returns another decorator, which then
    returns the function wrapper. The wrapper is used to time the
    execution of the decorated function (just like the
    timer decorator does). However, in this case, a timeout error
    will be thrown if the function call took longer than the `limit`
    passed to the decorator.
    """

    def outer_wrapper(func):
        @functools.wraps(func)
        def inner_wrapper(*args, **kwargs):
            start = time.time()
            return_value = func(*args, **kwargs)
            duration = time.time() - start

            if duration >= timeout:
                msg = f"Function {func.__name__} exceed timeout limit {limit}"
                raise TimeoutError(msg)

            return return_value

        return inner_wrapper

    return outer_wrapper
