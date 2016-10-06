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
    return x.__car__()


def cdr(x):
    return x.__cdr__()


def caar(x): return car(car(x))


def cadr(x): return car(cdr(x))


def cdar(x): return cdr(car(x))


def cddr(x): return cdr(cdr(x))


@check_args_instance_of(BaseSExpression)
def cons(x, y):
    return SExpression(x, y)
