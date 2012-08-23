"""Monkey-patching module.

Code is from debug_toolbar.
"""
import types


def _replace_function(func, wrapped):
    if isinstance(func, types.FunctionType):
        if func.__module__ == '__builtin__':
            # oh shit
            __builtins__[func] = wrapped
        else:
            module = __import__(func.__module__, {}, {}, [func.__module__], 0)
            setattr(module, func.__name__, wrapped)
    elif getattr(func, 'im_self', None):
        # TODO: classmethods
        raise NotImplementedError
    elif hasattr(func, 'im_class'):
        # for unbound methods
        setattr(func.im_class, func.__name__, wrapped)
    else:
        raise NotImplementedError


def replace_call(func):
    def inner(callback):
        def wrapped(*args, **kwargs):
            return callback(func, *args, **kwargs)
        actual = getattr(func, '__wrapped__', func)
        wrapped.__wrapped__ = actual
        wrapped.__doc__ = getattr(actual, '__doc__', None)
        wrapped.__name__ = actual.__name__
        _replace_function(func, wrapped)
        return wrapped
    return inner
