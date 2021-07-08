
from  todo_app.tests import inc_dec
from todo_app import ViewModel

import pytest

def test_increment():
    assert inc_dec.increment(3) == 4

def test_decrement():
    assert inc_dec.decrement(3) == 2
    

