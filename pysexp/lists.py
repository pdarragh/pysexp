from .recursive_functions import *


class EmptyListException(Exception):
    pass


class ListOfSExpression(SExpression):
    def __car__(self):
        if self.__is_empty__():
            raise EmptyListException
        return super().__car__()

    def __cdr__(self):
        if self.__is_empty__():
            raise EmptyListException
        return super().__cdr__()

    def __is_empty__(self):
        return null(super().__car__()) and null(super().__cdr__())

    def __repr__(self):
        if self.__is_empty__():
            return '()'
        return super().__repr__()

    def __str__(self):
        if self.__is_empty__():
            return '()'
        return super().__str__()

    def __eq__(self, other):
        if not isinstance(other, ListOfSExpression):
            return False
        if self.__is_empty__() and other.__is_empty__():
            return True
        return super().__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)


EMPTY = ListOfSExpression(NIL, NIL)


@check_args_instance_of(ListOfSExpression)
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
