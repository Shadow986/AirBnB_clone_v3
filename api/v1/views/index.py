#!/usr/bin/python3
"""
This is the 'index' module.

This module provides a Flask application instance with a '/status' route.
"""

from flask import Flask, jsonify
from api.v1.views import app_views

# Create a variable app, instance of Flask
app = Flask(__name__)

# Register the blueprint app_views to your Flask instance app
app.register_blueprint(app_views)

@app_views.route('/status', methods=['GET'])
def status():
    """
    Returns a JSON: "status": "OK"
    """
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app.run()
