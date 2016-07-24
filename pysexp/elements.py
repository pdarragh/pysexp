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

    def __repr__(self):
        return '(' + repr(self.car) + ', ' + repr(self.cdr) + ')'

    def __str__(self):
        result = '(' + repr(self.car)
        if isinstance(self.cdr, Nil):
            result += ')'
        else:
            result += ', ' + repr(self.cdr) + ')'
        return result
