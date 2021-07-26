##from data.Item import Item
from  todo_app.tests import inc_dec
from todo_app import ViewModel
from todo_app.data.Item import Item
from datetime import date,  timedelta


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

def test_view_model_can_filter_doing_items():
    
    item1 = Item("1", "Done", "Do this", "")
    item2 = Item("2", "Doing", "Do that", "")
    item3 = Item("3", "todo", "Do that", "")
    print (item1)
    print (item2)
    print (item3)
    view_model = ViewModel.ViewModel([item1, item2, item3],"todo","Doing","Done")
    items_doing = view_model.doing_items
    assert len(items_doing) == 1

def test_view_model_can_filter_todo_items():
    
    item1 = Item("1", "Done", "Do this", "")
    item2 = Item("2", "Doing", "Do that", "")
    item3 = Item("3", "todo", "Do that", "")
    print (item1)
    print (item2)
    print (item3)
    view_model = ViewModel.ViewModel([item1, item2, item3],"todo","Doing","Done")
    items_todo = view_model.todo_items
    assert len(items_todo) == 1

def test_view_model_can_show_all_done_items():

    item1 = Item("1", "Done", "Do this", str(date.today()))
    item2 = Item("2", "Done", "Do that", str(date.today() - timedelta(days=1)))
    item3 = Item("3", "Done", "Do that", str(date.today() - timedelta(days=2)))
    item4 = Item("4", "Done", "Do this", str(date.today() - timedelta(days=3)))
    item5 = Item("5", "Doing", "Do that",str(date.today() - timedelta(days=4)))
    item6 = Item("6", "todo", "Do that", str(date.today()))
    
    view_model = ViewModel.ViewModel([item1, item2, item3, item4, item5, item6],"todo","Doing","Done")
    items_todo = view_model.should_show_all_done_items
    assert len(items_todo) == 4 
    
def test_view_model_can_show_recent_done_items():
    item1 = Item("1", "Done", "Do this", str(date.today()))
    item2 = Item("2", "Done", "Do that", str(date.today() - timedelta(days=1)))
    item3 = Item("3", "Done", "Do that", str(date.today() - timedelta(days=2)))
    item4 = Item("4", "Done", "Do this", str(date.today() - timedelta(days=3)))
    item5 = Item("5", "Doing", "Do that", str(date.today() - timedelta(days=4)))
    item6 = Item("6", "todo", "Do that", str(date.today()))
    
    view_model = ViewModel.ViewModel([item1, item2, item3, item4, item5, item6],"todo","Doing","Done")
    items_todo = view_model.recent_done_items
    assert len(items_todo) == 1 
    
def test_view_model_can_show_older_done_items():
    item1 = Item("1", "Done", "Do this", str(date.today()))
    item2 = Item("2", "Done", "Do that", str(date.today() - timedelta(days=1)))
    item3 = Item("3", "Done", "Do that", str(date.today() - timedelta(days=2)))
    item4 = Item("4", "Done", "Do this", str(date.today() - timedelta(days=3)))
    item5 = Item("5", "Doing","Do that", str(date.today() - timedelta(days=4)))
    item6 = Item("6", "todo", "Do that", str(date.today()))
    
    view_model = ViewModel.ViewModel([item1, item2, item3, item4, item5, item6],"todo","Doing","Done")
    items_todo = view_model.older_done_items
    assert len(items_todo) == 3 