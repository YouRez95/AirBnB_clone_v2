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


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
      function run when we hit the url 0.0.0.0:5000/hbnb
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hbnb_c(text):
    """
      function run when we hit the url 0.0.0.0:5000/c/anything
      and return the string "C anything"
      and if anything have _ should replace by empty string
    """
    new_text = text.replace('_', ' ')
    return "C {}".format(new_text)


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def hbnb_python(text="is cool"):
    """
      function run when we hit the url 0.0.0.0:5000/c/anything
      and return the string "C anything"
      and if anything have _ should replace by empty string
      if the text not passed is cool is the default text
    """
    new_text = text.replace('_', ' ')
    return "Pyhton {}".format(new_text)


if __name__ == "__main__":
    app.run(debug=True)
