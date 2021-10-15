import dotenv, pytest
from todo_app import app
from unittest.mock import patch

#methods to get test board and list_id's



@pytest.fixture
def client():
    #use our test integration config instead f the "real" version
    file_path = dotenv.find_dotenv('.env_test')

    #create the new app
    test_app = app.create_app()

    #use app to create a test client
    with test_app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')

@patch('requests.get')
def test_index_page(mock_get_requests, client):
    # Replace call to requests.get(url) with our own function
    mock_get_requests.side_effect = mock_get_cards
    response = client.get('/')

#def mock_get_lists(url, params):
#    if url == f'https://api.trello.com/1/boards/{TEST_BOARD_ID}/lists':
#        response = Mock()
#        # sample_trello_lists_response should point to some test response data
#        response.json.return_value = sample_trello_lists_response
#        return response
#   return None

def mock_get_cards(url,params):
    #url to match  -  'https://api.trello.com/1/boards/' + get_boardid) +'/cards?fields=name,idList,dateLastActivity'
    if url == f'https://api.trello.com/1/boards/{TEST_BOARD_ID}/cards?fields=name,idlist,dateLastActivity':
        response = Mock()
        #sample_trello_cards response with the requested fields
        response.json.return_value = sample_trello_cards_response
        return response
    return None

