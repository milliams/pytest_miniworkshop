from hypothesis import given
from hypothesis.strategies import lists, integers

from my_lib import add_elements

@given(lists(integers()), lists(integers()))
def test_add(a, b):
    add_elements(a, b)

