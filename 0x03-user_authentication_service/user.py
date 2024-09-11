#!/usr/bin/env python3
""" object relational mapping module
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer

Base = declarative_base()


class User(Base):
    """ class User that maps to the database table users
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)

    def __repr__(self):
        """ string representation of the object
        """
        return (f"<User(id={self.id}, email='{self.email}')>")
