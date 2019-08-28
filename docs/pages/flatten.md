[Home](../../README.md) | [Flatter  Decorators](flatten.md)

# Flatter Decorators

Those who are new to python often find decorators difficult to get their head around. Glossy tries to simplify the creation of decorators by flattening the structure and reducing the number of wrapper functions needed. For example:

**Before:**

```python
import functools
import time


def timer(func):
    """
    Timer Decorator

    Place this decorator on functions to see how long they
    take to execute.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        secs = time.time() - start
        name = func.__name__
        print(f"Function {name} took {secs} seconds")
        return return_value

    return wrapper
```

**After:**

```python
import glossy
import time


@glossy.decorator
def timer(func, *args, **kwargs):
    """
    Timer

    Place this decorator on functions to see how long
    they take to execute.
    """
    start = time.time()
    result = func(*args, **kwargs)
    secs = time.time() - start
    name = func.__name__
    print(f"Function {name} took {secs} seconds")
    return result
```

In the first example, the top-level wrapper takes the function being decorated as input and returns a `wrapper` function. The inner wrapper is then responsible for calling the decorated function with the expected arguments and keyword arguments.

In the second example, we don't need multiple layers. By using the `glossy.decorator` utility, our decorator takes the fucntion being decorated as input and it also takes the expected arguments and keyword arguments.

Glossy works with more complex decorators too!  For example:

**Before:**

```python
import functools
import time


def timeout(limit=5):
    """
    Timeout

    Place this decorator on functions to raise an error
    when they exceed the given time limit.
    """

    def outer_wrapper(func):

        @functools.wraps(func)
        def inner_wrapper(*args, **kwargs):
            start = time.time()
            return_value = func(*args, **kwargs)
            duration = time.time() - start

            if duration >= timeout:
            name = func.__name__
            msg = f"Function {name} exceeded timeout: {limit}"
            raise TimeoutError(msg)

            return return_value

        return inner_wrapper

    return outer_wrapper
```

**After:**

```python

def timeout(limit=5):
    """
    Timeout

    Place this decorator on functions to raise an error
    when they exceed the given time limit.
    """

    @decorator
    def _timeout(func, *args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        if duration > limit:
            name = func.__name__
            msg = f"Function {name} exceeded timeout: {limit}"
            raise TimeoutError(msg)

        return result

    return _timeout
```

<br/>
