from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
            # do not serialize the password, its a security breach
        }
    
class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column (db.Integer, primary_key=True)
    id_user = db.Column (db.Integer, ForeignKey('user.id'))
    id_people = db.Column (db.Integer, ForeignKey('people.id_people'))
    id_planet = db.Column (db.Integer, ForeignKey('planet.id_planet'))
   

    def __repr__(self):
        return f'<Favorite {self.id}>'
    
    def serialize(self):
        return {
            "id" : self.id,
            "id_user" : self.id_user,
            "id_people" : self.id_people,
            "id_planet" : self.id_planet
        }


class People(db.Model):
    __tablename__ = 'people'
    id_people = db.Column (db.Integer, primary_key=True)
    Name = db.Column (db.String(50), nullable=False)
    Gender = db.Column (db.String(10))
    Birth_year = db.Column (db.String(50))
    Eye_color = db.Column (db.String(50))
    Hair_color = db.Column (db.String(50))
    id_planet = db.Column (db.Integer, ForeignKey('planet.id_planet'))

    def __repr__(self):
        return f'<People {self.id_people}>'

    def serialize(self):
        return {
            "id_people" : self.id_people,
            "Name" : self.Name,
            "Gender" : self.Gender,
            "Birth_year" : self.Birth_year, 
            "Eye_color" : self.Eye_color,
            "Hair_color" : self.Hair_color,
            "id_planet" : self.id_planet,
            "id_starship" : self.id_starship
        }

class Planet(db.Model):
    __tablename__ = 'planet'
    id_planet = db.Column (db.Integer, primary_key=True)
    Name = db.Column (db.String(50), nullable=False, unique=True)
    Diameter = db.Column (db.Integer)
    Rotation_period = db.Column (db.Integer)
    Population = db.Column (db.Integer)
    Climate = db.Column (db.String(50))
    Terrain = db.Column (db.String(50))
    id_people = db.Column (db.Integer)
    def __repr__(self):
        return f'<Planet {self.id_planet}>'

    def serialize(self):
        return {
            "id_planet" : self.id_planet,
            "Name" : self.Name,
            "Diameter" : self.Diameter,
            "Rotation_period" : self.Rotation_period,
            "Population" : self.Population,
            "Climate" : self.Climate,
            "Terrain" : self.Terrain,
            "id_people" : self.id_people
        }

