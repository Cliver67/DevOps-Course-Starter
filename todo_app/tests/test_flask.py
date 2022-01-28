
#from selenium import webdriver


from os import environ
from urllib import request
from todo_app import app
from todo_app import ViewModel
from unittest import mock
import dotenv, pytest, json
from unittest.mock import patch 
from todo_app.data import trello_items



#class TestIntegration:



trello_board_id = environ.get('BOARDID')
mock_trello_lists_response = "[{'id': '001', 'name': 'To Do'}]"
mock_trello_cards_response = "[{'id':'id001','name':'hello i am a card','idList':'003'}]"



@pytest.fixture
def client():
#use our test integration config instead of the "real" version
    file_path = dotenv.find_dotenv('.env.test')
    dotenv.load_dotenv(file_path)


    #create the new app
    test_app = app.create_app()

    #use app to create a test client
    with test_app.test_client() as client:
        yield client


@patch('requests.get')
def test_index_page(mock_get_requests, client):
    # Replace call to requests.get(url) with our own function
    mock_get_requests.side_effect = mock_get_lists( url="https://api.trello.com/1/boards/mockboard/lists", params=None)
    response = client.get('/')
    
    
    #assertions  first the obvious
    assert 1==1
    
    #assert response.data 


@patch('requests.get')
def test_cards_pull( mock_get_cards, client):
    mock_get_cards.side_effect = mock_get_cards(url='https://api.trello.com/1/boards/mockboard/cards',params=None)
    response = client.get('/')


def mock_get_lists(url, params):
    
    if url == f'https://api.trello.com/1/boards/mockboard/lists':

        response = mock.MagicMock()

        # sample_trello_lists_response should point to some test response data
        response.json.return_value = mock_trello_lists_response
        
        return response
    return None

def mock_get_cards(url,params):

    if url == f'https://api.trello.com/1/boards/mockboard/cards':
        response = mock.MagicMock()
        #sample_trello_cards response with the requested fields
        response.json.return_value = mock_trello_cards_response
        return response
    return None
