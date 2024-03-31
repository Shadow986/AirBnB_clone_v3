#!/usr/bin/python3
"""
This is the 'app' module.

This module provides a Flask application instance.
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
import os

# Create a variable app, instance of Flask
app = Flask(__name__)

# Register the blueprint app_views to your Flask instance app
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_db(error):
    """
    Closes the storage on teardown
    """
    storage.close()

if __name__ == "__main__":
    # Run your Flask server (variable app) with:
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
