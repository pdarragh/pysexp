class BaseSExpression:
    pass


class Atom(BaseSExpression):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if not isinstance(other, Atom):
            return False
        return self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)


class Nil(Atom):
    __is_frozen = False

    def __init__(self):
        super().__init__(None)
        self.__is_frozen = True

    def __repr__(self):
        return 'NIL'

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        return isinstance(other, Nil)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __setattr__(self, key, value):
        if self.__is_frozen:
            raise AttributeError("NIL values cannot be modified")
        else:
            super().__setattr__(key, value)


NIL = Nil()


class SExpression(BaseSExpression):
    def __init__(self, car, cdr=None):
        if cdr is None:
            cdr = NIL
        if not (isinstance(car, BaseSExpression) and isinstance(cdr, BaseSExpression)):
            raise ValueError("S-Expressions may only be composed of other S-Expressions")
        if isinstance(cdr, Atom) and cdr != NIL:
            pass
        self.car = car
        self.cdr = cdr

    @property
    def internal_repr(self):
        return repr(self.car) + ', ' + repr(self.cdr)

    @property
    def internal_str(self):
        if self.cdr == NIL:
            return str(self.car)
        else:
            return str(self.car) + ', ' + str(self.cdr)

    def __repr__(self):
        return '(' + self.internal_repr + ')'

    def __str__(self):
        return '(' + self.internal_str + ')'

    def __eq__(self, other):
        if not isinstance(other, SExpression):
            return False
        return (self.car == other.car) and (self.cdr == other.cdr)

    def __ne__(self, other):
        return not self.__eq__(other)
