from .recursive_functions import *


class EmptyListException(Exception):
    pass


class InternalListException(ValueError):
    pass


class List(SExpression):
    def __new__(cls, *args):
        bases = (List, )
        inner_type_field = '__inner_type__'
        if len(args) == 0:
            name = 'EmptyList'
            internals = {inner_type_field: NIL}
        else:
            t = type(args[0])
            name = 'ListOf({})'.format(t.__name__)
            internals = {inner_type_field: t}
        # Black magic here. We add the type to the global namespace to prevent issues where Python would not identify
        # multiple instances of the same type as actually being the same type (because they would be different 'type'
        # instances with the same attributes -- which is "not the same" to Python).
        if name not in globals():
            globals()[name] = type(name, bases, internals)
        return super().__new__(globals()[name])

    def __init__(self, *vals):
        if len(vals) == 0:
            super().__init__(NIL, NIL)
        elif len(vals) == 1:
            super().__init__(vals[0], NIL)
        else:
            if not isinstance(vals[1], type(vals[0])):
                raise InternalListException("type {} does not match internal type {}".format(type(vals[1]), vals[0]))
            super().__init__(vals[0], List(*vals[1:]))

    def __car__(self):
        if self.is_empty:
            raise EmptyListException
        return super().__car__()

    def __cdr__(self):
        if self.is_empty:
            raise EmptyListException
        return super().__cdr__()

    @property
    def is_empty(self):
        return null(super().__car__()) and null(super().__cdr__())

    def __repr__(self):
        if self.is_empty:
            return '()'
        return super().__repr__()

    def __str__(self):
        if self.is_empty:
            return repr(self)
        return super().__str__()

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        if self.is_empty and other.is_empty:
            return True
        return super().__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)


EMPTY = List()


@check_args_instance_of(List)
def empty(lsexp):
    return lsexp.is_empty


def cons(x, y):
    return List(x, y)


@optimize_tail_call
def append(x, y):
    if null(x):
        return y
    return cons(car(x), append(cdr(x), y))


@check_args_instance_of(BaseSExpression)
@optimize_tail_call
def among(x, y):
    if not null(y) and (equal(x, car(y)) or among(x, cdr(y))):
        return True
    return False
