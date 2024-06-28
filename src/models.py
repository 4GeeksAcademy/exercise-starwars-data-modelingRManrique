import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    sub_date = Column(String(250), nullable=False)
    


class Character(Base):
    __tablename__ = 'Character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False)


class Planet(Base):
    __tablename__ = 'Planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)


    
class Vehicles(Base):
    __tablename__ = 'Vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Vehicles = Column(String(250), nullable=False)


class Fav_Character(Base):
    __tablename__ = 'Fav_Character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Character_id = Column(Integer, ForeignKey('Character.id'))
    User_id = Column(Integer, ForeignKey('User.id'))



class Fav_Planet (Base):
    __tablename__ = 'fav_Planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Plante_id = Column(Integer, ForeignKey('Planet.id'))
    User_id = Column(Integer, ForeignKey('User.id'))


class Fav_Vehicles(Base):
    __tablename__ = 'Fav_Vehicles'
    id = Column(Integer, primary_key=True)
    Fav_Vehicles = Column(Integer, ForeignKey('Vehicles.id'))
    User_id = Column(Integer, ForeignKey('User.id'))
    
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
