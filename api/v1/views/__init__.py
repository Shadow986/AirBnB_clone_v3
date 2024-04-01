#!/usr/bin/python3
"""
This is the '__init__' module.

This module provides a Flask Blueprint instance with a '/api/v1' prefix.
"""

from flask import Blueprint
from api.v1.views.index import *
from api.v1.views.state import *

# Create a variable app_views which is an instance of Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
