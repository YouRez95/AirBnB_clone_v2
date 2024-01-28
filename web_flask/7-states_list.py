#!/usr/bin/python3

"""
  module that run the app server
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """
      function get the data from DB and handle the route /states_list
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def remove_session(self):
    """
      function run after every request
    """
    storage.close()


if __name__ == "__main__":
    app.run(debug=True)
