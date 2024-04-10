#!/usr/bin/env python3
"""
0. Basic Flask app
"""


from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    """
    First you will setup a basic Flask app in 0-app.py.
    Create a single / route and an index.html template
    that simply outputs “Welcome to Holberton” as page title (<title>)
    and
    “Hello world” as header (<h1>).
    """
    template = render_template('index.html',
                               title='Welcome to Holberton',
                               header='Hello world')
    return template


if __name__ == '__main__':
    app.run(debug=True)
