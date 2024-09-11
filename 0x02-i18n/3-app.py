#!/usr/bin/env python3
"""
Demonstrates how to use Flask-Babel in a Flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def home():
    """ 
    Returns the 3-index.html page
    """
    return render_template('3-index.html')
