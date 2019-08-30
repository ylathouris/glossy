[Home](../../README.md) | [Discoverablity](discover.md)

# Discoverablity

When using decorators on a function or class, you're effectively wrapping that function of class in another function. In fact, that's precisely what a decorator is - it's a function which takes a function as input and returns a function as output.

When using glossy decorators, glossy will return a `glossy.Decorated` object. This object represents the decorated function.

For example:

```python
import glossy

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


@timer
def hello():
    """
    Hello World!
    """
    print("Hello World!")

```

```
>>> hello
<glossy.Decorated(hello) at 0x102ce6518>
```

The `glossy.Decorated` object behaves a lot like the
original function object (`foo`) but it has some special features. Firstly, it does it's best to look and feel like the original function. It uses the `@functools.wraps` utility to achieve this. For example:

```
>>> hello.__name__
"hello"

>>> hello.__doc__
"Hello World!"

>>> hello.__wrapped__
<function hello at 0x10304c598>
```

The `@functools.wraps` utility adds the `__wrapped__` attrubute to the decorated function. This is pretty cool. Glossy goes one step further by adding a `__wrappers__`. This attribute contains a list of all the decorators wrapping the original function. In this case, there is just one:


```
>>> hello.__wrappers__
[
    {
        'decorator': <function timer at 0x102ce31e0>,
        'parameters': None
    }
]
```

Let's add another decorator to our function. We'll use the timeout decorator mentioned elsewhere in the documentation.

```python
@timer
@timeout(limit=1)
def hello():
    """
    Hello World!
    """
    print("Hello World!")
```

Now let's see what `__wrappers__` contains:

```
>>> hello.__wrappers__
[
    {
        'decorator': <function timeout at 0x102ce32f0>,
        'parameters': ([], OrderedDict([('limit', 1)]))
    },
    {
        'decorator': <function timer at 0x102ce31e0>,
        'parameters': None
    }
]
```

Glossy keeps track of the parameters passed to the decorator when it was applied to the function. This is particularly useful when Testing & Mocking

