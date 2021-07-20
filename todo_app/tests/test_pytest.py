##from data.Item import Item
from  todo_app.tests import inc_dec
from todo_app import ViewModel
from todo_app.data.Item import Item


import pytest

def test_increment():
    assert inc_dec.increment(3) == 4

def test_decrement():
    assert inc_dec.decrement(3) == 2
    

def test_view_model_can_filter_done_items():
    
    item1 = Item("1", "Done", "Do this", "")
    item2 = Item("3", "todo", "Do that", "")
    #item1 = {"id": "1","idList":"Done","name":"do this"}
    #item2 = {"id": "2","idList":"todo","name":"do that"}
    print (item1)
    print (item2)
    view_model = ViewModel.ViewModel([item1, item2],"todo","Doing","Done")
    items_done = view_model.done_items
    assert len(items_done) == 1
