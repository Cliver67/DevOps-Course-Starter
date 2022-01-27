
from todo_app import ViewModel
from todo_app.data.Item import Item
from datetime import date, datetime,  timedelta


import pytest

def test_view_model_can_filter_done_items():
    
    item1 = Item("1", "Done", "Do this", "")
    item2 = Item("3", "todo", "Do that", "")
   
    view_model = ViewModel.ViewModel([item1, item2],"todo","Doing","Done")
    items_done = view_model.done_items
    assert len(items_done) == 1
    assert items_done == [item1]
    assert items_done != [item2]

def test_view_model_can_filter_doing_items():
    
    item1 = Item("1", "Done", "Do this", "")
    item2 = Item("2", "Doing", "Do that", "")
    item3 = Item("3", "todo", "Do that", "")
    
    view_model = ViewModel.ViewModel([item1, item2, item3],"todo","Doing","Done")
    items_doing = view_model.doing_items
    assert len(items_doing) == 1
    assert items_doing == [item2]
    assert items_doing != [item1]

def test_view_model_can_filter_todo_items():
    
    item1 = Item("1", "Done", "Do this", "")
    item2 = Item("2", "Doing", "Do that", "")
    item3 = Item("3", "todo", "Do that", "")
    
    view_model = ViewModel.ViewModel([item1, item2, item3],"todo","Doing","Done")
    items_todo = view_model.todo_items
    assert len(items_todo) == 1

    
def test_view_model_can_show_recent_done_items():

    #dateformat  2021-08-03T11:37:05.733Z
    #todo - change date calc in test to allow for current date
    format = "%Y-%m-%dT%H:%M:%S.%fZ"
    #date1 = datetime.today().isoformat()
    #print (date1)
    
    date1 = '2022-01-27T11:37:05.733Z'

    item1 = Item("1", "Done", "Do this", str(date1)) #"2021-08-12T11:37:05.733Z")
    item2 = Item("2", "Done", "Do that", "2021-08-02T11:37:05.733Z")    #str(date.today() - timedelta(days=1)))
    item3 = Item("3", "Done", "Do that", "2021-08-01T11:37:05.733Z")    #str(date.today() - timedelta(days=2)))
    item4 = Item("4", "Done", "Do this", "2021-07-31T11:37:05.733Z")    #str(date.today() - timedelta(days=3)))
    item5 = Item("5", "Doing", "Do that", "2021-07-30T11:37:05.733Z")   #str(date.today() - timedelta(days=4)))
    item6 = Item("6", "todo", "Do that", "2021-08-03T11:37:05.733Z")    #str(date.today()))
    
    view_model = ViewModel.ViewModel([item1, item2, item3, item4, item5, item6],"todo","Doing","Done")
    items_recent = view_model.recent_done_items
    assert len(items_recent) == 1 
    assert items_recent == [item1]
    assert items_recent != [item3]  
    assert items_recent != [item5]  
    

def test_view_model_can_show_older_done_items():
    item1 = Item("1", "Done", "Do this", "2022-01-27T11:37:05.733Z")
    item2 = Item("2", "Done", "Do that", "2021-08-04T11:37:05.733Z")    #str(date.today() - timedelta(days=1)))
    item3 = Item("3", "Done", "Do that", "2021-08-03T11:37:05.733Z")    #str(date.today() - timedelta(days=2)))
    item4 = Item("4", "Done", "Do this", "2021-08-02T11:37:05.733Z")    #str(date.today() - timedelta(days=3)))
    item5 = Item("5", "Doing", "Do that", "2021-08-01T11:37:05.733Z")   #str(date.today() - timedelta(days=4)))
    item6 = Item("6", "todo", "Do that", "2022-01-27T11:37:05.733Z")    #str(date.today()))
    
    view_model = ViewModel.ViewModel([item1, item2, item3, item4, item5, item6],"todo","Doing","Done")
    items_todo = view_model.older_done_items
    assert len(items_todo) == 3 

def test_view_model_can_limit_done_items():

    item1 = Item("1", "Done", "Do this", str(date.today() - timedelta(days=1)))
    item2 = Item("2", "Done", "Do that", str(date.today() - timedelta(days=1)))
    item3 = Item("3", "Done", "Do that", str(date.today() - timedelta(days=2)))
    item4 = Item("4", "Done", "Do this", str(date.today() - timedelta(days=3)))
    item5 = Item("5", "Done", "Do that",str(date.today() - timedelta(days=4)))
    item6 = Item("6", "Done", "Do that", str(date.today() - timedelta(days=1)))
    
    view_model = ViewModel.ViewModel([item1, item2, item3, item4, item5, item6],"todo","Doing","Done")
    items_todo = view_model.limit_done_items

    assert len(items_todo) == 5 