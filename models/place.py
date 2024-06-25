#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60),
                     nullable=False,
                     ForeignKey('cities.id'))
    user_id = Column(String(60),
                     nullable=False,
                     ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, server_default='0', nullable=False)
    number_bathrooms = Column(Integer, server_default='0', nullable=False)
    max_guest = Column(Integer, server_default='0', nullable=False)
    price_by_night = Column(Integer, server_default='0', nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
