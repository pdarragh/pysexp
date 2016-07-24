from .elements import *


def atom(x):
    return isinstance(x, Atom)


def eq(x, y):
    if not isinstance(x, Atom) or not isinstance(y, Atom):
        raise ValueError("eq is undefined for non-atomic values")
    return x == y


def car(x):
    if not isinstance(x, SExpression):
        raise ValueError("car is defined only for S-Expressions")
    return x.car


def cdr(x):
    if not isinstance(x, SExpression):
        raise ValueError("cdr is defined only for S-Expressions")
    return x.cdr


def cons(x, y):
    if not isinstance(x, BaseSExpression) or not isinstance(y, BaseSExpression):
        raise ValueError("cons is undefined for values that do not subclass BaseSExpression")
    return SExpression(x, y)
