from .functions import *
from .decorators import *


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
