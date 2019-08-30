[Home](../../README.md) | [Testing & Mocking](testing.md)

# Testing & Mocking

Technically speaking, the function being decorated isn’t part of your program’s public interface. The wrapper function returned by the outermost decorator is the function your users will actually interact with. Therefore, it makes sense that you would always test the function with the decorators. However, there are some cases, particularly when unit testing, when you may want to mock one or more of the decorators on your function. And, as it turns out this is quite difficult to do.

One approach is to mock or patch the decorator using a mocking library such as `unittest.mock`. However, the catch here is that it must be patched before it’s used. This means any modules which use the decorator must be imported after the patching has taken place.

Another approach is to bypass all the decorators by calling the wrapper function directly. If your decorators use `@functools.wraps` you will be able to access the underlying function using the `__wrapped__` attribute. This is pretty handy! That said, if your function has multiple decorators, you can’t really pick and choose which ones you’d like to bypass. It’s all or nothing.

Glossy provides some useful tools for mocking your decorators. If you're using glossy decorators, you can mock them like so:

```python
@timer
@timeout(limit=1)
def delay(seconds):
    time.sleep(seconds)
    return "Foobar"
```

```python
delay.mock_decorator(timout, limit=1)
delay(0.5)
```

