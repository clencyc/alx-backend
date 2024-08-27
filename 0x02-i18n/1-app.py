 #!/usr/bin/env python3
"""
This module creates the Flask app instance
"""


from flask import Flask
from flask_babel import Babel
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
