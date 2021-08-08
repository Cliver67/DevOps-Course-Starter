
from flask import Flask, render_template, redirect, url_for, request

from todo_app.flask_config import Config
from todo_app import ViewModel
from todo_app.data import trello_items as trelloItems
import os



app = Flask(__name__)
app.config.from_object(Config)

listtodo = os.environ.get('LISTTODO')
listdoing = os.environ.get('LISTDOING')
listdone = os.environ.get('LISTDONE')

@app.route('/')
def index():
    items = trelloItems.get_items()
    item_view_model = ViewModel.ViewModel(items,listtodo, listdoing, listdone)
    return render_template('index.html', view_model=item_view_model)
    
@app.route('/items/recent', methods=['POST'])
def show_recent_complete():
    items = trelloItems.get_items()
    item_view_model = ViewModel.ViewModel(items,listtodo, listdoing, listdone)
    return render_template('index.html', view_model=item_view_model)   

@app.route('/items/aged')
def show_aged_complete():
    
    items = trelloItems.get_items()
    item_view_model = ViewModel.ViewModel(items,listtodo, listdoing, listdone, limitdone = False)
    return render_template('index.html', view_model=item_view_model)  

@app.route('/items/new', methods=['POST'])
def add_item():
    title = request.form['title']
    trelloItems.add_item(title)
    return redirect(url_for('index'))


@app.route('/items/<id>/complete', methods=['POST'])
def complete_item(id):
    trelloItems.complete_item(id)
    return redirect(url_for('index'))

@app.route('/items/<id>/commence', methods=['POST'])
def commence_item(id):
    trelloItems.commence_item(id)
    return redirect(url_for('index'))

@app.route('/items/<id>/reopen', methods=['POST'])
def reopen_item(id):
    trelloItems.reopen_item(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()

###
#def create_app():
#    app = Flask(__name__)
#    # We specify the full path and remove the import for this config so
#    # it loads the env variables when the app is created, rather than when this file is imported
#    app.config.from_object('todo_app.flask_config.Config')
#    # All the routes and setup code etc
#    return app
    