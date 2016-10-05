from pysexp.elements import *
from pysexp.functions import *

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


@pytest.mark.parametrize('a,b,s_repr,s_str', [
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
def test_sexpression(a, b, s_repr, s_str):
    s = SExpression(a, b)
    assert car(s) == a
    assert cdr(s) == b
    assert repr(s) == s_repr
    assert str(s) == s_str
    assert s == SExpression(a, b)
    assert s != SExpression(b, a)


def test_sexpression_single():
    x = Atom(1)
    s = SExpression(x)
    assert car(s) == x
    assert cdr(s) == NIL
    assert str(s) == '(1)'


@pytest.mark.parametrize('a,b', [
    (Atom(1), 2),
    ('a', Atom('b')),
    (1.2, 3.4),
])
def test_sexpression_error(a, b):
    with pytest.raises(ValueError):
        SExpression(a, b)

