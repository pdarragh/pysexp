class BaseSExpression:
    pass


class Atom(BaseSExpression):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return str(self.value)


class Nil(Atom):
    def __init__(self):
        super().__init__(None)

    def __repr__(self):
        return 'NIL'

    def __str__(self):
        return str(self)


class SExpression(BaseSExpression):
    def __init__(self, car, cdr=None):
        self.car = car
        if cdr is None:
            self.cdr = Nil()
        else:
            self.cdr = cdr

    @property
    def internal_repr(self):
        return repr(self.car) + ', ' + repr(self.cdr)

    @property
    def internal_str(self):
        if isinstance(self.cdr, Nil):
            return str(self.car)
        elif isinstance(self.cdr, SExpression):
            return str(self.car) + ', ' + self.cdr.internal_str
        else:
            return str(self.car) + ', ' + str(self.cdr)

    def __repr__(self):
        return '(' + self.internal_repr + ')'

    def __str__(self):
        return '(' + self.internal_str + ')'
