"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
import app

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)

@api.route('/user', methods=['GET'] )
def user():
    respuesta = app.user()
    print("VALOR retornado de APP", respuesta)
    return jsonify(respuesta),200

@api.route('/user/<int:id>', methods=['GET'] )
def oneUser(id):
    respuesta = app.oneUser(id)
    print("VALOR retornado de APP", respuesta)
    return jsonify(respuesta),200

@api.route('/people', methods=['POST'] )
def addpeople():
    data = request.json
    respuesta = app.addpeople(data)
    print(respuesta)
    return jsonify(respuesta),200

@api.route('/people', methods=['GET'] )
def people():
    respuesta = app.people()
    print("VALOR retornado de APP", respuesta)
    return jsonify(respuesta),200

@api.route('/people/<int:id>', methods=['GET'] )
def onePeople(id):
    respuesta = app.onePeople(id)
    print("VALOR retornado de APP", respuesta)
    return jsonify(respuesta),200

@api.route('/planets', methods=['POST'] )
def addplanets():
    data = request.json
    respuesta = app.addplanets(data)
    print(respuesta)
    return jsonify(respuesta),200

@api.route('/planets', methods=['GET'] )
def planets():
    respuesta = app.planets()
    print("VALOR retornado de APP", respuesta)
    return jsonify(respuesta),200

@api.route('/planets/<int:id>', methods=['GET'] )
def oneplanet(id):
    respuesta = app.oneplanet(id)
    print("VALOR retornado de APP", respuesta)
    return jsonify(respuesta),200

# Favorites

@api.route('/users/favorites/<int:user_id>', methods=['GET'] )
def getFavUser(user_id):
    respuesta = app.getFavUser(user_id)
    print("VALOR retornado de APP", respuesta)
    return jsonify(respuesta),200

@api.route('/favorite/planet/<int:planet_id>', methods=['POST'] )
def addFavPlanet(planet_id):
    data = request.json
    respuesta = app.addFavPlanet(data, planet_id)
    print(respuesta)
    return jsonify(respuesta),200

@api.route('/favorite/people/<int:people_id>', methods=['POST'] )
def addfavPeople(people_id):
    data = request.json
    respuesta = app.addfavPeople(data, people_id)
    print(respuesta)
    return jsonify(respuesta),200

@api.route('/favorite/planet/<int:planet_id>', methods=['DELETE'] )
def delFavPlanet(planet_id):
    data = request.json
    respuesta = app.delFavPlanet(data, planet_id)
    print(respuesta)
    return jsonify(respuesta),200

@api.route('/favorite/people/<int:people_id>', methods=['DELETE'] )
def delfavPeople(people_id):
    data = request.json
    respuesta = app.delfavPeople(data, people_id)
    print(respuesta)
    return jsonify(respuesta),200



@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200
