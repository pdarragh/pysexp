from .functions import *

from sys import _getframe


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


@check_args_instance_of(BaseSExpression)
@optimize_tail_call
def ff(x):
    if atom(x):
        return x
    return ff(car(x))


@check_args_instance_of(BaseSExpression)
@optimize_tail_call
def subst(x, y, z):
    if not atom(y):
        raise ValueError("argument y must be an Atom: {}".format(y))
    if atom(z):
        if eq(z, y):
            return x
        else:
            return z
    else:
        return cons(subst(x, y, car(z)), subst(x, y, cdr(z)))


@check_args_instance_of(BaseSExpression)
@optimize_tail_call
def equal(x, y):
    if atom(x) and atom(y):
        return eq(x, y)
    elif not atom(x) and not atom(y):
        return equal(car(x), car(y)) and equal(cdr(x), cdr(y))
    else:
        return False
