#!/usr/bin/python3
"""Starts a Flask Web Application"""
from flask import Flask, g, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


def get_data():
    """Fetches data from FileStorage of DBStorage"""
    if 'db' not in g:
        g.db = storage.all()
    return (g.db)


@app.teardown_appcontext
def close_resources(exception):
    """Tears down resources"""
    db = g.pop('db', None)
    if db is not None:
        storage.close()


@app.route('/state_list')
def state_list():
    """Displays an HTML page that lists all state objects"""
    resource = get_data()
    return (render_template('7-states_list.html', all_states=resource))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
