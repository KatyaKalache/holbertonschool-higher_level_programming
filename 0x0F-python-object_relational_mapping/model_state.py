#!/usr/bin/python3
# class definition of a State and an instance Base
import sqlalchemy
import sys
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           unique=True, nullable=False,
                           autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(128))
