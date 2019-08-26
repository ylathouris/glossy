from .decorators import simple, fancy


def with_no_decorators():
    """
    Example function with no decorators
    """
    pass


@simple
def with_simple_decorator():
    """
    Example function with one simple decorator
    """
    pass


@fancy()
def with_fancy_decorator():
    """
    Example function with one callable decorator
    """
    pass


@simple
@fancy()
def with_multiple_decorators():
    """
    Example function with multiple decorators
    """
    pass
