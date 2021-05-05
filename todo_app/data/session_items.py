from flask import session
import requests

boardid = "608a91fd8a30ef4966d68da1"
trello_key = '0471642aefef5fa1fa76530ce1ba4c85'
trello_token = '9eb76d9a9d02b8dd40c2f3e5df18556c831d4d1fadbe2c45f8310e6c93b5c548'

def get_items():

    """
    Module 2 - amend get_items to use response and Trello api
    Returns: response json() containing trello card names / id's and lists id's
    """

    url = 'https://api.trello.com/1/boards/' + str(boardid) + '/cards?fields=name,idList'

    query = {
        'key': '0471642aefef5fa1fa76530ce1ba4c85',
        'token': '9eb76d9a9d02b8dd40c2f3e5df18556c831d4d1fadbe2c45f8310e6c93b5c548'
            }

    #response = requests.request(
    #        "GET",
    #        url,
    #        params=query
    #        )

    return make_get_request(url, query)

def get_item(id):
    """                                                                 
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    items = get_items()

    # Determine the ID for the item based on that of the previously added item
    id = items[-1]['id'] + 1 if items else 0

    item = { 'id': id, 'title': title, 'status': 'Not Started' }

    # Add the item to the list
    items.append(item)
    session['items'] = items

    return item


def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item

def complete_item(id):
    item = get_item(id)

    if item != None:
        item['status'] = 'Completed'
        save_item(item)

    return item


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

