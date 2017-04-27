from typing import List


class SExp:
    def to_list(self, ...):  # -> List[SExp]
        return [SExp()]

    def is_list(self) -> bool:
        ...


class SInt(SExp):
    def __init__(self, val: int):
        self.val = val


class SSymbol(SExp):
    def __init__(self, val: str):
        self.id = val


class STrue(SExp):
    def __init__(self):
        pass


class SFalse(SExp):
    def __init__(self):
        pass


class SCons(SExp):
    def __init__(self, car: SExp, cdr: SExp):
        self.car = car
        self.cdr = cdr


class SNil(SExp):
    def __init__(self):
        pass


def SList(sexp: SExp):
    if sexp.is_list():
        return sexp.to_list()
    else:
        return None


class SExpLexerState:
    def process(self, c: str):
        pass

    def process_eof(self):
        pass


class DONE(SExpLexerState): pass
class INCOMMENT(SExpLexerState): pass
class INID(SExpLexerState): pass
class INHASH(SExpLexerState): pass
class INNUM(SExpLexerState): pass
class INWHITESPACE(SExpLexerState): pass


class SExpLexer:
    def __init__(self, s: str):
        self.input = s
        self.state = SExpLexerState()

    def peek(self):
        pass

    def next(self):
        pass

    def eat_lpar(self):
        pass

    def eat_rpar(self):
        pass


class SExpToken: pass

class LPAR(SExpToken): pass
class RPAR(SExpToken): pass
class EOS(SExpToken): pass

class INT(SExpToken):
    def __init__(self, val: int):
        self.val = val


class HASH(SExpToken):
    def __init__(self, val: str):
        self.val = val


class ID(SExpToken):
    def __init__(self, val: str):
        self.val = val


class ParseException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return '{}: {}'.format(type(self), self.message)


class SExpParser:
    def __init__(self, s: str):
        self.input = s
        self.lex = SExpLexer(self.input)

    def next_file(self) -> List[SExp]:
        p = self.lex.peek()

        if isinstance(p, EOS):
            return []
        else:
            head = self.next_sexp()
            tail = self.next_file()
            return [head, tail]

    def next_sexp(self) -> SExp:
        p = self.lex.peek()

        if isinstance(p, EOS):
            raise ParseException("expected s-exp; got end of input")
        if isinstance(p, LPAR):
            self.lex.eat_lpar()
            sexp = self.next_sexp()
            self.lex.eat_rpar()
            return sexp
        if isinstance(p, INT):
            return SInt(p.val)
        if isinstance(p, ID):
            return SSymbol(p.val)
        if isinstance(p, HASH):
            if p.val == 't':
                return STrue
            if p.val == 'f':
                return SFalse
            raise ParseException("invalid hash: {}".format(p.val))

    def next_sexplist(self) -> SExp:
        p = self.lex.peek()

        if isinstance(p, RPAR):
            return SNil
        else:
            head = self.next_sexp()
            tail = self.next_sexplist()
            return SCons(head, tail)


class Exp:
    def exp_from(self, sexp: SExp):
        if isinstance(sexp, SSymbol):
            return RefExp(sexp.id)
        if isinstance(sexp, SList)


class RefExp(Exp):
    def __init__(self, val: str):
        self.id = val


class LambdaExp(Exp):
    def __init__(self, params: List[str], body: Exp):
        self.params = params
        self.body = body


class AppExp(Exp):
    def __init__(self, fun: Exp, args: List[Exp]):
        self.fun = fun
        self.args = args


class BoolExp(Exp):
    def __init__(self, value: bool):
        self.value = value


class IfExp(Exp):
    def __init__(self, cond: Exp, if_true: Exp, if_false: Exp):
        self.cond = cond
        self.if_true = if_true
        self.if_false = if_false


class AndExp(Exp):
    def __init__(self, cond1: Exp, cond2: Exp):
        self.cond1 = cond1
        self.cond2 = cond2


class OrExp(Exp):
    def __init__(self, cond1: Exp, cond2: Exp):
        self.cond1 = cond1
        self.cond2 = cond2


class IntExp(Exp):
    def __init__(self, value: int):
        self.value = value


class ZeroPExp(Exp):
    def __init__(self, test: Exp):
        self.test = test


class SubExp(Exp):
    def __init__(self, exp1: Exp, exp2: Exp):
        self.exp1 = exp1
        self.exp2 = exp2


class EqExp(Exp):
    def __init__(self, exp1: Exp, exp2: Exp):
        self.exp1 = exp1
        self.exp2 = exp2


class PlusExp(Exp):
    def __init__(self, exp1: Exp, exp2: Exp):
        self.exp1 = exp1
        self.exp2 = exp2


class TimesExp(Exp):
    def __init__(self, exp1: Exp, exp2: Exp):
        self.exp1 = exp1
        self.exp2 = exp2


class LetExp(Exp):
    def __init__(self, vars: List[str], exps: List[Exp], body: Exp):
        self.vars = vars
        self.exps = exps
        self.body = body


class LetRecExp(Exp):
    def __init__(self, fun: str, lmb: Exp, body: Exp):
        self.fun = fun
        self.lmb = lmb
        self.body = body


class ConsExp(Exp):
    def __init__(self, car: Exp, cdr: Exp):
        self.car = car
        self.cdr = cdr


class CarExp(Exp):
    def __init__(self, arg: Exp):
        self.arg = arg


class CdrExp(Exp):
    def __init__(self, arg: Exp):
        self.arg = arg


class PairPExp(Exp):
    def __init__(self, arg: Exp):
        self.arg = arg


class NullPExp(Exp):
    def __init__(self, arg: Exp):
        self.arg = arg


class NullExp(Exp): pass
