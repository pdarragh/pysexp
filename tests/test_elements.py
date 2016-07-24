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
    assert a == Atom(val)
    assert a != Atom('blah')
    assert a != 42


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
    with pytest.raises(AttributeError):
        n.x = 42


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
    assert s == SExpression(car, cdr)
    assert s != SExpression(cdr, car)


def test_sexpression_single():
    car = Atom(1)
    s = SExpression(car)
    assert s.car == car
    assert s.cdr == NIL
    assert str(s) == '(1)'


@pytest.mark.parametrize('car,cdr', [
    (Atom(1), 2),
    ('a', Atom('b')),
    (1.2, 3.4),
])
def test_sexpression_error(car, cdr):
    with pytest.raises(ValueError):
        SExpression(car, cdr)

