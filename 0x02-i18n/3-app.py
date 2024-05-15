#!/usr/bin/env python3
"""
1. Basic Babel setup
"""


from flask import Flask
from flask import render_template
from flask_babel import Babel
from flask import request
from flask import _


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
@app.route('/index')
def index():
    """
    First you will setup a basic Flask app in 1-app.py.
    Create a single / route and an index.html template
    that simply outputs “Welcome to Holberton” as page title (<title>)
    and
    “Hello world” as header (<h1>).
    """
    template = render_template('1-index.html',
                               title="Welcome to Holberton",
                               header="Hello world")
    return template


class Config:
    """
    Config class that has a LANGUAGES class attribute equal to ["en", "fr"].
    Config to set Babel’s default locale ("en") and timezone ("UTC").
    Use that class as config for Flask app
    """
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@babel.localeselector
def get_locale():
    """
    get locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def gettext():
    """
    the _ or gettext function to parametrize templates.
    the message IDs home_title and home_header.
    """
    return _('Welcome to Holberton'), _('Hello world')


if __name__ == '__main__':
    app.run(debug=True)
