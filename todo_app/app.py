
from flask import Flask, render_template, redirect, url_for, request

from todo_app.flask_config import Config
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
    return render_template('index.html', items = items, todo = listtodo , doing =listdoing, done = listdone)


@app.route('/items/new', methods=['POST'])
def add_item():
    title = request.form['title']
    trelloItems.add_item(title)
    return redirect(url_for('index'))


@app.route('/items/<id>/complete')
def complete_item(id):
    trelloItems.complete_item(id)
    return redirect(url_for('index'))

@app.route('/items/<id>/commence')
def commence_item(id):
    trelloItems.commence_item(id)
    return redirect(url_for('index'))

@app.route('/items/<id>/reopen')
def reopen_item(id):
    trelloItems.reopen_item(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()