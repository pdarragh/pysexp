from pysexp.elements import *

import pytest


@pytest.mark.parametrize('val', [
    'a',
    1,
])
def test_atom(val):
    a = Atom(val)
    assert a.value == val
    assert repr(a) == repr(val)
    assert str(a) == str(val)


def test_nil():
    n = Nil()
    assert n.value is None
    assert repr(n) == 'NIL'
    assert str(n) == repr(n)


def test_NIL():
    n = Nil()
    assert NIL == n
    assert NIL.value is None
    assert repr(NIL) == repr(n)
    assert str(NIL) == str(n)


@pytest.mark.parametrize('car,cdr,s_repr,s_str', [
    (Atom('a'), Atom('b'), "('a', 'b')", "(a, b)"),
    (Atom(1), Atom(2), "(1, 2)", "(1, 2)"),
    (Atom(42), SExpression(Atom('a'), Atom('b')), "(42, ('a', 'b'))", "(42, (a, b))"),
    (
        SExpression(Atom('a'), Atom('b')),
        SExpression(Atom('c'), Atom('d')),
        "(('a', 'b'), ('c', 'd'))",
        "((a, b), (c, d))"
    ),
])
def test_sexpression(car, cdr, s_repr, s_str):
    s = SExpression(car, cdr)
    assert s.car == car
    assert s.cdr == cdr
    assert repr(s) == s_repr
    assert str(s) == s_str


def test_sexpression_single():
    car = Atom(1)
    s = SExpression(car)
    assert s.car == car
    assert s.cdr == NIL

