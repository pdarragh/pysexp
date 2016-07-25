from .elements import *
from .decorators import *


@check_args_instance_of(BaseSExpression)
def atom(x):
    return isinstance(x, Atom)


@check_args_instance_of(BaseSExpression)
def null(x):
    return atom(x) and x == NIL


@check_args_instance_of(BaseSExpression)
@check_args_instance_of(Atom)
def eq(x, y):
    return x == y


def car(x):
    if hasattr(x, '__car__'):
        return x.__car__()
    raise AttributeError("type {} does not implement __car__".format(x.__class__.__name__))


def cdr(x):
    if hasattr(x, '__cdr__'):
        return x.__cdr__()
    raise AttributeError("type {} does not implement __cdr__".format(x.__class__.__name__))


def caar(x): return car(car(x))


def cadr(x): return car(cdr(x))


def cdar(x): return cdr(car(x))


def cddr(x): return cdr(cdr(x))


@check_args_instance_of(BaseSExpression)
def cons(x, y):
    return SExpression(x, y)
