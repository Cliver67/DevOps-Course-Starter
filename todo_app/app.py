###
#from flask import Flask, render_template, request
#from todo_app.flask_config import Config
#from todo_app.data import session_items

#app = Flask(__name__)
#app.config.from_object(Config)

#@app.route('/')
#def index():
#    items = session_items.get_items()
#    return render_template("index.html", items = items)

#@app.route('/newitem', methods=['POST'])
#def create_new():
    #call add item
#    data = request.form.get('newitem')
#    session_items.add_item(data)
#    #re render
#    items = session_items.get_items()
#    #line changed to use flask funtionality
#    #return redirect('/')
#    return render_template("index.html", items = items)

#if __name__ == '__main__':
#    app.run()
###
from flask import Flask, render_template, redirect, url_for, request

from todo_app.flask_config import Config
from todo_app.data import session_items as session
import os


app = Flask(__name__)
app.config.from_object(Config)

listtodo = os.environ.get('listtodo')
listdoing = os.environ.get('listdoing')
listdone = os.environ.get('listdone')

@app.route('/')
def index():
    items = session.get_items()
    return render_template('index.html', items = items, todo = listtodo , doing =listdoing, done = listdone)


@app.route('/items/new', methods=['POST'])
def add_item():
    title = request.form['title']
    session.add_item(title)
    return redirect(url_for('index'))


@app.route('/items/<id>/complete')
def complete_item(id):
    session.complete_item(id)
    return redirect(url_for('index'))

@app.route('/items/<id>/commence')
def commence_item(id):
    session.commence_item(id)
    return redirect(url_for('index'))

@app.route('/items/<id>/reopen')
def reopen_item(id):
    session.reopen_item(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()