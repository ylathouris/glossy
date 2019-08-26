# Glossy

>  _**Make your decorators glossy**_


<br/>

## Installation

```
pip install glossy
```


<br/>

## Flatter Decorators

Those who are new to python often find decorators difficult to get their head around. Glossy tries to simplify the creation of decorators by flattening the structure and reducing the number of wrapper functions required. For example:

**Before:**

```python
import functools
import time


def timer(func):
    """
    Timer Decorator

    Place this decorator on functions to see
    how long they take to execute.
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

    Place this decorator on functions to see
    how long they take to execute.
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

    Place this decorator on functions to raise
    an error when they exceed the given time limit.
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

    Place this decorator on functions to raise
    an error when they exceed the given time limit.
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

## Inspection

The `glossy` library contains some handy functions for inspecting your code. For example:

**Checking if a function is decorated**

```python
import glossy

glossy.is_decorated(func)  # returns True/False
```

**Getting all decorators on a function**

```python
import glossy

decorators = glossy.get_decorators(func)
```

**Getting a specific decorator**

```python
import glossy

decorators = glossy.get_decorator(func, "@timer")
```

**Checking if a function has a specific decorator**

```python
import glossy

glossy.has_decorator(func, decorator)
```

<br/>

## Testing & Mocking

Regular decorators are notoriously difficult to test and/or mock. In most cases, you need to patch the decorator before you import the code that uses the decorator. This is less than ideal. Using `glossy` decorators, you can easily mock all decorators on a function.

```python

@timeout(limit=1.0)
def slow(seconds):
    time.sleep(seconds)
    return True


def test_slow_has_timeout_decorator():
    """
    Test slow has the timeout decorator.
    """
    status = glossy.has_decorator(slow, timeout)

    assert status is True


def test_slow_without_timeout_decorator():
    """
    Test slow function without timeout decorator.
    """
    glossy.mock(timeout)

    result = slow(3)

    assert result is True

```
