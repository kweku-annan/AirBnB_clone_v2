#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template

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


@app.route('/python')
@app.route('/python/<text>')
def python_route(text="is cool"):
    """Returns Python page"""
    text = text.replace('_', ' ')
    return (f'Python {text}')


@app.route('/number/<int:n>')
def number_route(n):
    """Displays n is a number if n is an integer"""
    return (f'{n} is a number')


@app.route('/number_template/<int:n>')
def number_template(n):
    """Displays an HTML page only if n is an integer"""
    return (render_template('5-number.html', number=f'{n}'))


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Tells if n is odd or even"""
    if n % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    return (render_template('6-number_odd_or_even.html',
                            number=f'{n}',
                            odd_or_even=f'{odd_or_even}'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
