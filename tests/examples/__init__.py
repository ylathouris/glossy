from . import functions
from . import decorators


__all__ = ["get_function", "get_decorator"]


def get_function(name):
    """
    Get example function.

    Args:
        name (str): The name of an example function.
    """
    global functions

    obj = getattr(functions, name, None)
    if not obj:
        functions = [fn for fn in dir(functions) if not fn.startswith("_")]
        options = "\n\t- ".join(functions)
        msg = (
            f"Cannot find example function: {name}\n"
            f"Did you mean one of: \n\t- {options}"
        )
        raise ValueError(msg)

    return obj


def get_decorator(name):
    """
    Get example decorator.

    Args:
        name (str): The name of an example decorator.
    """
    global decorators

    obj = getattr(decorators, name, None)
    if not obj:
        decorators = [d for d in dir(decorators) if not d.startswith("_")]
        options = "\n\t- ".join(decorators)
        msg = (
            f"Cannot find example decorator: {name}\n"
            f"Did you mean one of: \n\t- {options}"
        )
        raise ValueError(msg)

    return obj
