#!/usr/bin/python3
""" Flask web application to display states and cities """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def states():
    """ Display a HTML page with a list of all State objects """
    states = storage.all(State).values()
    states = sorted(states, key=lambda x: x.name)
    return render_template('9-states.html', states=states)

@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """ Display a HTML page with the cities of a State given its id """
    state = storage.get(State, id)
    if state is None:
        return render_template('9-states.html', not_found=True)
    cities = state.cities if storage.t == 'db' else state.cities()
    cities = sorted(cities, key=lambda x: x.name)
    return render_template('9-states.html', state=state, cities=cities)

@app.teardown_appcontext
def teardown_db(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
