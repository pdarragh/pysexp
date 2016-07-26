from .recursive_functions import *


class EmptyListException(Exception):
    pass


class ListOfSExpression(SExpression):
    def __init__(self, *vals):
        if len(vals) == 0:
            super().__init__(NIL, NIL)
        elif len(vals) == 1:
            super().__init__(vals[0], NIL)
        else:
            super().__init__(vals[0], ListOfSExpression(*vals[1:]))

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
            return '()'
        return super().__str__()

    def __eq__(self, other):
        if not isinstance(other, ListOfSExpression):
            return False
        if self.is_empty and other.is_empty:
            return True
        return super().__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)


EMPTY = ListOfSExpression()

@check_args_instance_of(ListOfSExpression)
def empty(lsexp):
    return lsexp.is_empty


def cons(x, y):
    return ListOfSExpression(x, y)


# @check_args_instance_of(ListOfSExpression)
@optimize_tail_call
def append(x, y):
    if null(x):
        return y
    return cons(car(x), append(cdr(x), y))


@check_args_instance_of(ListOfSExpression)
@optimize_tail_call
def among(x, y):
    if not null(y) and (equal(x, car(y)) or among(x, cdr(y))):
        return True
    return False
