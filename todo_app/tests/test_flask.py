
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



#trello_board_id = environ.get('BOARDID')
mock_trello_lists_response = [{'id': '001', 'name': 'To Do'}]
mock_trello_cards_response = [{'id':'id001','name':'hello i am a card','idList':'003' , 'dateLastActivity': None}]



@pytest.fixture
def client():
#use our test integration config instead of the "real" version
    file_path = dotenv.find_dotenv('.env.test')
    dotenv.load_dotenv(file_path, override=True)


    #create the new app
    test_app = app.create_app()

    #use app to create a test client
    with test_app.test_client() as client:
        yield client



@patch('requests.get')
def test_cards_pull( mock_get_cards, client):
    mock_get_cards.side_effect = get_cards
    response = client.get('/')

    assert 1==1
    assert b'hello i am a card' in  response.data



def get_cards(url,params):

    if url == f'https://api.trello.com/1/boards/mockboard/cards?fields=name,idList,dateLastActivity':
        response = mock.MagicMock()
        #sample_trello_cards response with the requested fields
        response.json.return_value = mock_trello_cards_response
        return response
    return None
