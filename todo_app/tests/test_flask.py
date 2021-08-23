import dotenv, pytest
from todo_app import app


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
