#!/usr/bin/python3
"""This module handles all default RESTFul API actions for City objects"""

from flask import Flask, jsonify, request, abort
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)

@app.route('/api/v1/states/<state_id>/cities', methods=['GET'])
def get_cities(state_id):
    """Retrieves the list of all City objects of a State"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities)

@app.route('/api/v1/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """Retrieves a City object"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())

# Add the remaining routes here

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
