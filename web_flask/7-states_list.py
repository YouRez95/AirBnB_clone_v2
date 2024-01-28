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
    data = storage.all(State).values()
    return render_template('7-states_list.html', states=data)


@app.teardown_appcontext
def remove_session(exception):
    storage.close()


if __name__ == "__main__":
    app.run(debug=True)
