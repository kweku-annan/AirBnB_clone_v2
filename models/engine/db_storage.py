#!/usr/bin/python3
"""Database storage engine"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.place import Place
from models.city import City


class DBStorage:
    """Representing database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Instance method to initiate new DBStorage instance"""
        HBNB_MYSQL_USER = getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = "localhost"
        HBNB_MYSQL_DB = getenv("HBNB_MYSQL_DB")

        conn_str = "mysql+mysqldb://{}:{}@{}:3306/{}".format(HBNB_MYSQL_USER,
                                                             HBNB_MYSQL_PWD,
                                                             HBNB_MYSQL_HOST,
                                                             HBNB_MYSQL_DB)
        self.__engine = create_engine(conn_str, pool_pre_ping=True)

        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns all objects in the database storage in dictionsry form"""
        dict = {}
        query = self.__session.query()

        if cls:
            query = self.__session.query(cls)

        for obj in query.all():
            dict[obj.to_dict()["__class__"] + "." + obj.id] = obj
        return dict

    def new(self, obj):
        """Adds the object tp the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from the database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)

    def close(self):
        """Close Session"""
        self.__session.close()
