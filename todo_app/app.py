from flask import Flask, render_template, request


from todo_app.flask_config import Config
from todo_app.data import session_items


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    items = session_items.get_items()
    return render_template("index.html", items = items)

@app.route('/newitem', methods=['POST'])
def create_new():

    #call add item
    data = request.form.get('newitem')
    session_items.add_item(data)
    #re render
    items = session_items.get_items()
    #line changed to use flask funtionality
    return redirect('/')
    #return render_template("index.html", items = items)


if __name__ == '__main__':
    app.run()
