# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

for trello integration 
the following variables/section  are required in the projects .env file

#Trello Keys
boardid = ID of the Trello board being used
trello_key = valid api key
trello_token = valid api token
listtodo = list id for the "Todo" list
listdoing = listid for the "Doing" list
listdone = listid for the "Done" List

## Testing
Using Pytest for automated testing.


## Test Notes
Pytest  - 3 tests to ensure viewmodel property methods to filter items by 
state or list_id are self contained. no key information is required as s default
state is included within the test
for each test a dictionary is built of string values to simulate a returned list of items from Trello
dictionary should contain 1 item in it with a listId that evaluates to the status ou are wanting to test (Done , todo, doing)
test asserts that the return dictionary contains a single item

These are :-
    id: 
    idList: 
    name: 
    dateLastActivity:

dateLastActivity is not needed for the following tests and an empty string can be passed

#test_view_model_can_filter_done_items
#test_view_model_can_filter_doing_items
#test_view_model_can_filter_todo_items

#test_view_model_can_limit_done_items will use the displaylimt property on done items defaulted to 5 but can be overridden

#datelastactivity is referenced in the following tests
#for tests to complete where datelast activity is needed date format needs to be (2021-08-03T11:37:05.733Z)
#test_view_model_can_show_recent_done_items - will filter items that are done where the datelastactivity matches current date
#test_view_model_can _show_older_done_items - will filter done items where datelastactivity is prior to todays date


