
import pytest
import dotenv
from todo_app import app
from unittest.mock import patch , MagicMock

from todo_app import app
from unittest import mock
import dotenv, pytest
from unittest.mock import patch 
import json
#methods to get test board and list_id's



@pytest.fixture
def client():
    #use our test integration config instead of the "real" version
    file_path = dotenv.find_dotenv('.env.test')
    

    #create the new app
    test_app = app.create_app()

    #use app to create a test client
    with test_app.test_client() as client:
        yield client

#def test_index_page(client):
#    response = client.get('/')

#@patch('requests.get')
#def test_index_page(mock_get_requests, client):
    # Replace call to requests.get(url) with our own function
#   mock_get_requests.side_effect = mock_get_lists
#    response = client.get('/')

#def mock_get_lists(url, params):

#    if url == f'https://api.trello.com/1/boards/{TEST_BOARD_ID}/lists':
#        response = Mock()
 #       response.json.return_value = sample_trello_lists_response
#        # sample_trello_lists_response should point to some test response data
 #       return response
 #   return None

    #mock_get_requests.side_effect = mock_get_cards

    #.side_effect = mock_get_cards('https://api.trello.com/1/boards/001/cards?fields=name,idList,dateLastActivity',1)

   #response = client.get('/')



def mock_get_cards(url,params):
    #url to match  -  'https://api.trello.com/1/boards/' + get_boardid() +'/cards?fields=name,idList,dateLastActivity'
    #if url == f'https://api.trello.com/1/boards/{TEST_BOARD_ID}/cards?fields=name,idList,dateLastActivity':
        response = mock.Mock()
        #sample_trello_cards response with the requested fields
        response.json.return_value = sample_trello_cards_response
        return response
    #return None

def sample_trello_cards_response():
    x = '{"id":"id001","name":"hello i am a card","idList":"003"}'
    y = json.loads(x)
    print(y["name"])


    return (y)
