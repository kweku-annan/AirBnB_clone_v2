#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if "models.storage_type" in locals():
        from models import storage_type
        if storage_type == "db":
            #name = Column(String(128), nullable=False)
            cities = relationship("City", backref="state")
        else:
            name = ""

        @property
        def cities(self):
            """Returns list of City instances
            where state_id == the current State.id"""
            from models import storage
            related_cities = []
            
            for city in storage.all(City):
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
