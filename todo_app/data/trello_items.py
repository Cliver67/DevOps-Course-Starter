from todo_app.data.Item import Item
import requests
import json

import os


#trello_key = os.environ.get('TRELLO_KEY')
#trello_token = os.environ.get('TRELLO_TOKEN')

#boardid = os.environ.get('BOARDID')
#listtodo = os.environ.get('LISTTODO')
#listdoing = os.environ.get('LISTDOING')
#listdone = os.environ.get('LISTDONE')

def get_trello_key():

    return os.environ.get('TRELLO_KEY')

def get_trello_token():

    return os.environ.get('TRELLO_TOKEN')

def get_boardid():

    return os.environ.get('BOARDID')

def get_list_todo():

    return os.environ.get('LISTTODO')

def get_list_doing():

    return os.environ.get('LISTDOING')

def get_list_done():

    return os.environ.get('LISTDONE')


def get_items():

    """
    Module 2 - amend get_items to use response and Trello api
    Returns: response json() containing trello card names / id's and lists id's
    """

    url = 'https://api.trello.com/1/boards/' + get_boardid() +'/cards?fields=name,idList,dateLastActivity'

    query = {
        'key': get_trello_key(),
        'token': get_trello_token()
            }

    responseJson = make_get_request(url, query)

    
    return [Item(itemJson['id'],  itemJson['idList'], itemJson['name'],itemJson['dateLastActivity']) for itemJson in responseJson]

    
def add_item(title):
    """
    Makes Trello POST call to create a new card 
    list predefined as todo hard coded for now
    Args:
        title: The title/name of the item.

    Returns:
        item: The saved item.
    """

    item = Item.createItemInTrello(title)

    return item

def commence_item(id):
    """
        makes call to move_card with list id for "doing" list
    Args:
        id = card id    
    """
    return move_card(id,str(get_list_doing))    


def make_get_request(url, query):

    geturl = url


    response = requests.get(geturl,params=query)
    #response = requests.request(
    #        "GET",
    #        geturl,
    #        params=query
    #        )

    return response.json()

def move_card(id, listid):

    """
    
        make PUT request to update the list a card belongs to 
        
    Args:
        id = card id    
        listid = destination list id
    """
    
    url = "https://api.trello.com/1/cards/"+ str(id)

    headers = {
        "Accept": "application/json"
            }   

    query = {
    'key': str(get_trello_key),
    'token': str(get_trello_token),
    'idList': listid
    }

    response = requests.request(
    "PUT",
    url,
    headers=headers,
    params=query
    )

    return " Item moved "

def complete_item(id):
    """
        makes call to move_card with list id for "Done" list
    Args:
        id = card id    
    """

    move_card(id,str(get_list_done))

def reopen_item(id):
    """
        makes call to move_card with list id for "doing" list
    Args:
        id = card id    
    """
    return move_card(id,str(get_list_todo))  

