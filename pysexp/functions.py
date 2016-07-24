from .elements import *


def check_args_instance_of(base_class):
    def wrap(base_function):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, base_class):
                    raise ValueError("{} is defined only for instances of {}".format(
                        base_function.__name__, base_class.__name__))
            return base_function(*args, **kwargs)
        return wrapper
    return wrap


@check_args_instance_of(BaseSExpression)
def atom(x):
    return isinstance(x, Atom)


@check_args_instance_of(BaseSExpression)
@check_args_instance_of(Atom)
def eq(x, y):
    return x == y


@check_args_instance_of(BaseSExpression)
@check_args_instance_of(SExpression)
def car(x):
    return x.car


@check_args_instance_of(BaseSExpression)
@check_args_instance_of(SExpression)
def cdr(x):
    return x.cdr


@check_args_instance_of(BaseSExpression)
def cons(x, y):
    return SExpression(x, y)
