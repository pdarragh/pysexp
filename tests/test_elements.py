from pysexp.elements import *

import pytest


def test_atom():
    val = 'a'
    assert Atom(val).value == val


def test_nil():
    assert Nil().value is None


@pytest.mark.parametrize('car,cdr', [
    ('a', 'b'),
    (1, 2),
    (42, SExpression('a', 'b')),
])
def test_sexpression(car, cdr):
    s = SExpression(car, cdr)
    assert s.car == car
    assert s.cdr == cdr

