import glossy

from .. import examples


def test_is_decoratored_on_func_with_no_decorators_returns_false():
    func = examples.get_function("with_no_decorators")
    result = glossy.is_decorated(func)
    assert result is False


def test_is_decoratored_on_func_with_decorators_returns_true():
    func = examples.get_function("with_multiple_decorators")
    result = glossy.is_decorated(func)
    assert result is True


def test_get_decorators_on_func_with_no_decorators_returns_empty_list():
    func = examples.get_function("with_no_decorators")
    decorators = glossy.get_decorators(func)
    assert decorators == []


def test_get_decorators_on_func_with_simple_decorator_returns_simple_decorator():
    func = examples.get_function("with_simple_decorator")
    decorators = glossy.get_decorators(func)
    expected = [examples.get_decorator("simple")]
    assert decorators == expected


def test_get_decorators_on_func_with_fancy_decorator_returns_fancy_decorator():
    func = examples.get_function("with_fancy_decorator")
    decorators = glossy.get_decorators(func)
    expected = [examples.get_decorator("fancy")]
    assert decorators == expected


def test_get_decorators_on_func_with_multiple_decorators_returns_expected():
    func = examples.get_function("with_multiple_decorators")
    decorators = glossy.get_decorators(func)
    expected = [examples.get_decorator("simple"), examples.get_decorator("fancy")]
    assert decorators == expected


def test_get_decorator_with_valid_name_returns_expected():
    func = examples.get_function("with_simple_decorator")
    decorator = glossy.get_decorator(func, "@simple")
    expected = examples.get_decorator("simple")
    assert decorator == expected


def test_get_decorator_with_valid_name_on_func_with_multiple_decorators_returns_expected():
    func = examples.get_function("with_multiple_decorators")

    decorator = glossy.get_decorator(func, "@simple")
    expected = examples.get_decorator("simple")
    assert decorator == expected

    decorator = glossy.get_decorator(func, "@fancy")
    expected = examples.get_decorator("fancy")
    assert decorator == expected


def test_get_decorator_with_invalid_name_returns_none():
    func = examples.get_function("with_simple_decorator")
    decorator = glossy.get_decorator(func, "bogus")
    assert decorator is None


def test_get_decorator_on_func_with_no_decorators_returns_none():
    func = examples.get_function("with_no_decorators")
    decorator = glossy.get_decorator(func, "@bogus")
    assert decorator is None


def test_has_decorator_with_valid_decorator_returns_true():
    func = examples.get_function("with_simple_decorator")
    simple = examples.get_decorator("simple")
    result = glossy.has_decorator(func, simple)
    assert result is True


def test_has_decorator_with_invalid_decorator_returns_false():
    func = examples.get_function("with_simple_decorator")
    simple = examples.get_decorator("fancy")
    result = glossy.has_decorator(func, simple)
    assert result is False


def test_has_decorator_on_func_with_no_decorators_returns_false():
    func = examples.get_function("with_no_decorators")
    simple = examples.get_decorator("simple")
    result = glossy.has_decorator(func, simple)
    assert result is False


def test_has_decorators_with_valid_decorators_returns_true():
    func = examples.get_function("with_multiple_decorators")
    simple = examples.get_decorator("simple")
    fancy = examples.get_decorator("fancy")
    result = glossy.has_decorators(func, [simple, fancy])
    assert result is True


def test_has_decorators_with_invalid_decorators_returns_false():
    func = examples.get_function("with_simple_decorator")
    simple = examples.get_decorator("simple")
    fancy = examples.get_decorator("fancy")
    result = glossy.has_decorators(func, [simple, fancy])
    assert result is False


def test_has_decorators_on_func_with_no_decorators_returns_false():
    func = examples.get_function("with_no_decorators")
    simple = examples.get_decorator("simple")
    result = glossy.has_decorators(func, [simple])
    assert result is False


# func = glossyy.inspect(foo)
# assert func.decorated_by(timeout, limit=1.0)
