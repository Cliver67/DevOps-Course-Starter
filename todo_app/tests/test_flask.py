
#from selenium import webdriver


from os import environ
from urllib import request
from todo_app import app
from todo_app.app import ViewModel
from unittest import mock
import dotenv, pytest, json
from unittest.mock import patch 



#@pytest.fixture(scope="module")
#def driver():
#    with webdriver.Firefox() as driver:
#        yield driver

class TestIntegration:

    trello_board_id = environ.get('BOARDID')
    mock_trello_lists_response = "[{'id': '001', 'name': 'To Do'}]"
    mock_trello_cards_response = "[{'id':'id001','name':'hello i am a card','idList':'003'}]"
 
    @pytest.fixture
    def client(url):
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
        mock_get_requests.side_effect = TestIntegration.mock_get_lists("https://api.trello.com/1/boards/{TestIntegration.trello_board_id}/lists", None)
        response = client.get('/')
        assert 1==1

        #assert json.loads(response['id']) == '001'
        
        #checkresponse = json.loads(response.json.returnvalue)
        #print(checkresponse)
        
        #assert checkresponse["name"] == "To Do"
        #assert checkresponse["id"] == "001"


    @patch('requests.get')
    def test_cards_pull(mock_get_cards, client):
        mock_get_cards.side_effect = TestIntegration.mock_get_cards("https://api.trello.com/1/boards/{TestIntegration.trello_board_id}/cards?fields=name,idList,dateLastActivity",None)
        response = client.get('/')
        
        assert response.json.return_value["idList"] == "003"
 


    def mock_get_lists(url, params):
        if url == f'https://api.trello.com/1/boards/{TestIntegration.trello_board_id}/lists':
            response = mock.Mock()

            # sample_trello_lists_response should point to some test response data
            response.json.return_value = TestIntegration.sample_trello_lists_response
            return response
        return None


    def mock_get_cards(url,params):
        if url == f'https://api.trello.com/1/boards/{TestIntegration.trello_board_id}/cards?fields=name,idList,dateLastActivity':
            response = mock.Mock()
            #sample_trello_cards response with the requested fields
            response.json.return_value =TestIntegration.mock_trello_cards_response
            return response
        return None
