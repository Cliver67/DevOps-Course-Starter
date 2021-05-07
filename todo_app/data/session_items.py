from flask import session
import requests
import json

import os

boardid = os.environ.get('boardid')
trello_key = os.environ.get('trello_key')
trello_token = os.environ.get('trello_token')


listtodo = os.environ.get('listtodo')
listdoing = os.environ.get('listdoing')
listdone = os.environ.get('listdone')


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
        'idList': listtodo,
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
    return move_card(id,listdoing)    

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

    move_card(id,listdone)

def reopen_item(id):
    """
        makes call to move_card with list id for "doing" list
    Args:
        id = card id    
    """
    return move_card(id,listtodo)  

