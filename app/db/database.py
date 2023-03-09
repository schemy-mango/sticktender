#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Define the SQLALCHEMY_DATABASE_URL as a constant
SQLALCHEMY_DATABASE_URL = settings.database_url

# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a SessionLocal class that can be used to create database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define a base class for SQLAlchemy models
Base = declarative_base()
"""
This example does the following:

Defines a constant SQLALCHEMY_DATABASE_URL that contains the URL for the Postgres database. This URL should be 
defined in the application's configuration file, such as a .env file.

Creates a SQLAlchemy engine using create_engine(), which takes the database URL as an argument.

Creates a SessionLocal class using sessionmaker(), which can be used to create new sessions that are bound to the 
database engine. The autocommit, autoflush, and bind arguments are used to configure the behavior of the sessions.

Defines a Base class using declarative_base(), which can be used as the base class for all SQLAlchemy models in the 
application.

These components are used throughout the application to interact with the database. For example, the get_db() 
dependency function that I showed earlier might use the SessionLocal


class to create a new database session for each request.Similarly, SQLAlchemy models would inherit from the Base class and use the engine to communicate with the database.
"""
