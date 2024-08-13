#!/usr/bin/python3
#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage, storage_type
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    if storage_type == "db":
        cities = relationship("City", backref="state")
    else:
        @property
        def cities(self):
            """Returns list of City instances where state_id == current State.id"""
            return [city for city in storage.all(City).values() if city.state_id == self.id]

'''
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
            # name = Column(String(128), nullable=False)
            cities = relationship("City", backref="state")
        else:
            name = ""

        if models.storage_type != "db":
            self.cities = ""
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
'''
