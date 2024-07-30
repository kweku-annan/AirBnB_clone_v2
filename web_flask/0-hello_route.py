#!/usr/bin/python3
"""Starts a Flask Web Application"""
from flask import Flask

app = Flask(__name__)

# Set global rule fo strict_slashes
app.url_map.strict_slashes = False

@app.route('/', strict_slashes=False)
def home():
    '''Returns: Displays: "Hello HBNB!"'''
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
