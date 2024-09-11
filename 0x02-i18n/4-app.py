#!/usr/bin/env python3
"""
Demonstrates how to use Flask-Babel in a Flask app
"""

from flask import Flask, request, render_template
from flask_babel import Babel

def get_locale():
    """
    This function determines the user's preferred locale based on their browser's
    accept language header. It checks for languages in SUPPORTED_LOCALES and
    returns the best match.
    """
    return request.accept_languages.best_match(SUPPORTED_LOCALES)

app = Flask(__name__)

# Configure Flask-Babel
app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Default locale if no match is found
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'  # Directory containing translations
babel = Babel(app)

# Supported locales (list of language codes)
SUPPORTED_LOCALES = ['en', 'fr']

# Removed the duplicate @babel.localeselector decorator

@app.route('/')
def home():
    return render_template('4-index.html')

if __name__ == "__main__":
    app.run()