from sys import _getframe


def check_args_instance_of(base_class):
    def wrap(base_function):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, base_class):
                    raise ValueError("{} is defined only for instances of {}".format(
                        base_function.__name__, base_class.__name__))
            return base_function(*args, **kwargs)
        wrapper.__doc__ = base_function.__doc__
        return wrapper
    return wrap


# Tail call optimization based on the solution posted by Crutcher Dunnavant on ActiveState:
# http://code.activestate.com/recipes/474088-tail-call-optimization-decorator/
# Note that this relies on the `sys._getframe()` function, which is only guaranteed to be implemented in CPython.

class TailRecursionException(Exception):
    pass


def optimize_tail_call(recursive_function):
    def wrapper(*args, **kwargs):
        frame = _getframe()
        if frame.f_back and frame.f_back.f_back and frame.f_back.f_back.f_code == frame.f_code:
            raise TailRecursionException(*args, **kwargs)
        else:
            while True:
                try:
                    return recursive_function(*args, **kwargs)
                except TailRecursionException as e:
                    args = e.args
    wrapper.__doc__ = recursive_function.__doc__
    return wrapper
