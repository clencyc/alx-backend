#!/usr/bin/env python3
"""
Demonstrates how to use Flask-Babel in a Flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@babel.localeselector
def get_locale() -> str:
    """This function returns the locale from the request"""
    return request.accept_languages.best_match(Config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def home():
    """ 
    Returns the 2-index.html page
    """
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
