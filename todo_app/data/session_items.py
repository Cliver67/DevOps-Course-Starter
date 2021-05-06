from flask import session
import requests
import json

boardid = '608a91fd8a30ef4966d68da1'
trello_key = 'ec35814e6002ff80fb49014a7a6f4ab9'
trello_token = '064fb4e3f20e3417bef4a1525a7b6342fbffc2ee90f0b0ab1658a8a0bce906b3'

def get_items():

    """
    Module 2 - amend get_items to use response and Trello api
    Returns: response json() containing trello card names / id's and lists id's
    """

    url = 'https://api.trello.com/1/boards/' + boardid +'/cards?fields=name,idList'

    query = {
        'key': trello_key,
        'token': trello_token
            }

    response = requests.request(
            "GET",
            url,
            params=query
            )

    return make_get_request(url, query)

def add_item(title):
    """
    Makes Trello POST call to create a new card 
    list predefined as todo hard coded for now
    Args:
        title: The title/name of the item.

    Returns:
        item: The saved item.
    """

    url = "https://api.trello.com/1/cards"

    query = {
        'key': trello_key,
        'token': trello_token,
        'idList': '608a9210a25e65624f49806b',
        'name': title
        }

    response = requests.request(
        "POST",
        url,
        params=query
        )

    
    return response.json()

def commence_item(id):
    """
        makes call to move_card with list id for "doing" list
    Args:
        id = card id    
    """
    return move_card(id,str('6092d58e13aa190b1d32ce19'))    

def get_lists():
    
    url = "https://api.trello.com/1/boards/" + str(boardid) + "/lists"

    query = {
    'key': trello_key,
    'token': trello_token
    }

    lists = make_get_request(url, query)
    
    #iterate through response to build lists object for comparison
    return lists

def make_get_request(url, query):

    geturl = url

    response = requests.request(
            "GET",
            geturl,
            params=query
            )

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
    'key': trello_key,
    'token': trello_token,
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

    move_card(id,str('608aa95fbe10572bf446d3cf'))

def reopen_item(id):
    """
        makes call to move_card with list id for "doing" list
    Args:
        id = card id    
    """
    return move_card(id,str('608a9210a25e65624f49806b'))  

