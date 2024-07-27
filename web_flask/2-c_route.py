#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask

app = Flask(__name__)

# Set Global rule for strict_slashes to False
app.url_map.strict_slashes = False


@app.route('/')
def home():
    """Displays homepage"""
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    """Displays hbnb page"""
    return ("HBNB")


@app.route('/c/<text>')
def c_route(text):
    """Returns C is <text>"""
    return (f"C {text.replace('_', ' ')}")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
