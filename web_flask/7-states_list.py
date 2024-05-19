#!/usr/bin/python3
''' Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
After each request you must remove the current SQLAlchemy Session:
Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()
Routes:
/states_list: display a HTML page: (inside the tag BODY)
H1 tag: “States”
UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
LI tag: description of one State: <state.id>: <B><state.name></B>
Import this 7-dump to have some data
You must use the option strict_slashes=False in your route definition
'''
from flask import Flask
from models import storage
from flask import g
from flask import render_template

app = Flask(__name__)

def create_app():
    ''' request the content from the storage engines'''
    with app.app_context():
        storage.all()

@app.route('/states_list', strict_slashes=False)
def statesList():
    ''' display a HTML page inside the tag BODY '''
    return render_template('7-states_list.html')

def get_db():
    ''' ensure the database is db '''
    if 'db' not in g:
        g.db = connect_to_database()

        return g.db

@app.teardown_appcontext
def tearDown(exception):
    ''' reset after session '''
    db = g.pop('db', None)

    if db is not None:
        storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
