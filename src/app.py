"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, send_from_directory
from flask_migrate import Migrate
from flask_swagger import swagger
from api.utils import APIException, generate_sitemap
from api.models import db, Favorite, People, Planet, User
from api.routes import api
from api.admin import setup_admin
from api.commands import setup_commands
from sqlalchemy import and_, or_
# from models import Person

ENV = "development" if os.getenv("FLASK_DEBUG") == "1" else "production"
static_file_dir = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), '../public/')
app = Flask(__name__)
app.url_map.strict_slashes = False

# database condiguration
db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace(
        "postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db, compare_type=True)
db.init_app(app)

# add the admin
setup_admin(app)

# add the admin
setup_commands(app)

# Add all endpoints form the API with a "api" prefix
app.register_blueprint(api, url_prefix='/api')

# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    if ENV == "development":
        return generate_sitemap(app)
    return send_from_directory(static_file_dir, 'index.html')

# any other endpoint will try to serve it like a static file


@app.route('/<path:path>', methods=['GET'])
def serve_any_other_file(path):
    if not os.path.isfile(os.path.join(static_file_dir, path)):
        path = 'index.html'
    response = send_from_directory(static_file_dir, path)
    response.cache_control.max_age = 0  # avoid cache memory
    return response

#User
def user():
    result = User.query.all()
    userList = []
    for user in result:
        userList.append(user.serialize())
    return userList

def oneUser(id):
    result = User.query.get(id)
    return result.serialize()

# People
def addpeople(data):
    newpeople = People()
    newpeople.id_people = int(data.get("uid"))
    newpeople.Name = data.get("Name")
    newpeople.Gender = data.get("Gender")
    newpeople.Birth_year = data.get("Birth_year") 
    newpeople.Eye_color = data.get("Eye_color")
    newpeople.Hair_color = data.get("Hair_color")
    db.session.add(newpeople)
    db.session.commit()
    response_body = {"message": "People created successfully"}
    return response_body

def people():
    result = People.query.all()
    peopleList = []
    for people in result:
        peopleList.append(people.serialize())
    return peopleList

def onePeople(id):
    result = People.query.get(id)
    return result.serialize()

# Planets

def addplanets(data):
    
    newplanet = Planet()
    newplanet.id_planet = int(data.get("id_planet"))
    newplanet.Name = data.get("Name")
    newplanet.Diameter = data.get("Diameter")
    newplanet.Rotation_period = data.get("Rotation_period") 
    newplanet.Population = data.get("Population")
    newplanet.Climate = data.get("Climate")
    newplanet.Terrain =  data.get("Terrain")
    db.session.add(newplanet)
    db.session.commit()
    response_body = {"message": "Planet created successfully"}
    return response_body

def planets():
    result = Planet.query.all()
    planetList = []
    for planet in result:
        planetList.append(planet.serialize())
    return planetList

def oneplanet(id):
    result = Planet.query.get(id)
    return result.serialize()

# Favorites

def addFavPlanet(data,planet_id):
    
    newFavPlanet = Favorite()
    newFavPlanet.id_user = int(data.get("id_user"))
    # newFavPlanet.id_people = data.get("id_people")
    newFavPlanet.id_planet = planet_id


    db.session.add(newFavPlanet)
    db.session.commit()
    response_body = {"message": "Planet add a favorites successfully"}
    return response_body

def addfavPeople(data,people_id):
    
    newFavPeople = Favorite()
    newFavPeople.id_user = int(data.get("id_user"))
    newFavPeople.id_people = people_id
    
    db.session.add(newFavPeople)
    db.session.commit()
    response_body = {"message": "people add a favorites successfully"}
    return response_body


def getFavUser(user_id):
    
    result = Favorite.query.filter_by(id_user=user_id).all()
    planetList = []
    for planet in result:
        planetList.append(planet.serialize())
    return planetList

def delFavPlanet(data,planet_id):
     id_user = int(data.get("id_user"))
     delnit = db.session.execute(db.delete(Favorite).where(and_ (Favorite.id_planet == planet_id), (Favorite.id_user == id_user)))
     db.session.commit()
     print("delnit",delnit, type(delnit))
     response_body = {"message": "Planet ", "nit": planet_id}
     return response_body

def delfavPeople(data,people_id):
     id_user = int(data.get("id_user"))
     result = db.session.execute(db.delete(Favorite).where(and_ (Favorite.id_people == people_id), (Favorite.id_user == id_user)))
     
     if result != None:
        
        db.session.commit()
        response_body = {"message": "people successfully removed from favorites "}
        return response_body
     else:
         response_body = {"message": "people doesn't exists in favorites "}
         return response_body
     


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3001))
    app.run(host='0.0.0.0', port=PORT, debug=True)
