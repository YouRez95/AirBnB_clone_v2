#!/usr/bin/python3

"""
  module that run the app server
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states/<id>", strict_slashes=False)
@app.route("/states/", strict_slashes=False)
def state_list(id=None):
    """
      function get the data from DB and handle the route /states_list
    """
    states = storage.all(State)
    if id is None:
        return render_template('9-states.html', states=states, id=None)
    else:
        for state in states.values():
            if state.id == id:
                return render_template('9-states.html', states=state, id=id)
        return render_template('9-states.html', id=id)


@app.teardown_appcontext
def remove_session(self):
    """
      function run after every request
    """
    storage.close()


if __name__ == "__main__":
    app.run(debug=True)
