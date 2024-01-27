#!/usr/bin/python3

"""
  module that run the app server
"""

from flask import Flask, render_template

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
    return "Python {}".format(new_text)


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """
      function run if the subpath n integer
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def render_number(n):
    """
      function run if the subpath n integer
      and return a template
    """
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def render_number_odd_or_even(n):
    """
      function run if the subpath n integer
      and return a template
    """
    decimal_part = int(str(n/2).split('.')[1])
    if decimal_part == 0:
        text = "even"
    else:
        text = "odd"

    return render_template('6-number_odd_or_even.html',
                           number=n, odd_or_even=text)


if __name__ == "__main__":
    app.run(debug=True)
