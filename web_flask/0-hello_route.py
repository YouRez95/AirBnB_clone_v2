#!/usr/bin/python3

"""
  module that run the app server
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
      function run when we hit the url 0.0.0.0:5000
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(debug=True)
