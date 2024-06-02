#!/usr/bin/python3

"""
This is a script that starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function returns Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function returns HBNB with route /hbnb
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    This function returns C followed by the value of the text variable
    """
    return "C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    returns Python followed by the value of the text variable
    The default value of text is “is cool”
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """returns number if its an integer"""
    return "{} is a number".format(n)


@app.errorhandler(404)
def page_not_found(error):
    """Error handler"""
    return "Not Found", 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
