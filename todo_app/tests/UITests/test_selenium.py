from ast import Delete
import os
from threading import Thread
from tkinter import Variable
from todo_app import app
import pytest
import requests
from selenium import webdriver


@pytest.fixture(scope='module')
def app_with_temp_board():
    # create the new board & update the board id environment variable
    board_id = create_trello_board()
    os.environ['TRELLO_BOARD_ID'] = board_id

    # construct the new application
    application = app.create_app()

    # start the app in its own thread.
    thread = Thread(target=lambda:application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application

    # tear down
    thread.join(1)
    delete_trello_board(board_id)



@pytest.fixture(scope="module")
def driver():
    with webdriver.Firefox() as driver:
            yield driver





#get trello ket and token plus methods for board creation and deletion below


def get_trello_key():

    return os.environ.get('TRELLO_KEY')

def get_trello_token():

    return os.environ.get('TRELLO_TOKEN')


def create_trello_board(boardname):
    #create a trello board and return the baoard id

    # This code sample uses the 'requests' library:
    # http://docs.python-requests.org

    url = "https://api.trello.com/1/boards/?"

    query = {
        'name': '{boardname}',
        'key': str(get_trello_key),
        'token': str(get_trello_token)
    }

    responseJson = requests.request(
    "POST",
    url,
    params=query
    )

    #find the board id returned in the response and pass back
    boardid = [(itemJson['id']) for itemJson in responseJson]

    return boardid


def delete_trello_board(board_id):

    # This code sample uses the 'requests' library:
    # http://docs.python-requests.org

    url = "https://api.trello.com/1/boards/{board_id}"

    query = {
        'key': str(get_trello_key),
        'token': str(get_trello_token)
            }

    response = requests.request(
    "DELETE",
    url,
    params=query)

    print(response.text)

    return

