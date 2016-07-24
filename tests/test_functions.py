from pysexp.functions import *

import pytest


@pytest.mark.parametrize('val', [
    'a',
    1,
    True,
    SExpression(Atom('a'), Atom(2)),
])
def test_atom(val):
    a = Atom(val)
    assert atom(a) == True
    if isinstance(val, BaseSExpression):
        assert atom(val) == False
    else:
        with pytest.raises(ValueError):
            atom(val)


def test_null():
    assert null(NIL)


def test_eq():
    assert eq(Atom('a'), Atom('a'))
    assert not eq(Atom('a'), Atom('b'))
    with pytest.raises(ValueError):
        eq(Atom('a'), 'a')


def test_car():
    with pytest.raises(ValueError):
        car(Atom('a'))
    assert car(SExpression(Atom('a'), Atom('b'))) == Atom('a')


def test_cdr():
    with pytest.raises(ValueError):
        cdr(Atom('a'))
    assert cdr(SExpression(Atom('a'), Atom('b'))) == Atom('b')


def test_composites():
    s = SExpression(SExpression(Atom('a'), Atom('b')), SExpression(Atom('c'), Atom('d')))
    assert caar(s) == Atom('a')
    assert cadr(s) == Atom('c')
    assert cdar(s) == Atom('b')
    assert cddr(s) == Atom('d')


def test_cons():
    with pytest.raises(ValueError):
        cons(Atom('a'), 4)
        cons(3, Atom('b'))
    assert cons(Atom('a'), Atom('b')) == SExpression(Atom('a'), Atom('b'))


@pytest.mark.parametrize('x,y', [
    (SExpression(Atom('a'), Atom('b')), SExpression(Atom('c'), Atom('d'))),
])
def test_relations(x, y):
    assert car(cons(x, y)) == x
    assert cdr(cons(x, y)) == y
    assert cons(car(x), cdr(x)) == x
    assert cons(car(y), cdr(y)) == y
