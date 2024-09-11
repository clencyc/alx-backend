#!/usr/bin/env python3
"""
Build flask app that prints hello world
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')


def index():
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
