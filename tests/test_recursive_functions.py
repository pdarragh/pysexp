from pysexp.recursive_functions import *

import pytest


@pytest.mark.parametrize('sexp,val', [
    (Atom('a'), Atom('a')),
    (SExpression(Atom('a'), Atom('b')), Atom('a')),
])
def test_ff(sexp, val):
    assert ff(sexp) == val


def test_ff_exception():
    with pytest.raises(ValueError):
        ff(42)


@pytest.mark.parametrize('x,y,z,val', [
    (Atom('a'), Atom('b'), Atom('c'), Atom('c')),
    (Atom('a'), Atom('b'), Atom('b'), Atom('a')),
    (Atom('a'), Atom('b'), SExpression(Atom('b'), Atom('c')), SExpression(Atom('a'), Atom('c'))),
    (
        SExpression(Atom('x'), Atom('a')),
        Atom('b'),
        SExpression(SExpression(Atom('a'), Atom('b')), Atom('c')),
        SExpression(SExpression(Atom('a'), SExpression(Atom('x'), Atom('a'))), Atom('c')),
    )
])
def test_subst(x, y, z, val):
    assert subst(x, y, z) == val


def test_subst_exception():
    with pytest.raises(ValueError):
        subst(Atom('a'), SExpression(Atom('b'), Atom('c')), Atom('z'))


@pytest.mark.parametrize('x,y,val', [
    (Atom('a'), Atom('b'), False),
    (Atom('a'), Atom('a'), True),
    (Atom('a'), SExpression(Atom('b'), Atom('c')), False),
    (SExpression(Atom('a'), Atom('b')), SExpression(Atom('c'), Atom('d')), False),
    (SExpression(Atom('a'), Atom('b')), SExpression(Atom('a'), Atom('b')), True),
])
def test_equal(x, y, val):
    assert equal(x, y) == val
