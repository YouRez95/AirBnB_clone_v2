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

    states = {}
    for item in data:
        states[item.id] = item.name
    states = dict(sorted(states.items(), key=lambda item: item[1]))
    print(states)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def remove_session(exception):
    storage.close()


if __name__ == "__main__":
    app.run(debug=True)
