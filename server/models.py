from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# contains definitions of tables and associated schema constructs
metadata = MetaData()

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# define a model class by inheriting from db.Model.
#A model with SQLAlchemy requires he python class to have the following:
class Pet(db.Model):#inheritance from a db.Model class
    __tablename__ = 'pets'#must have __tablename__ class attribute
     #one or more class atttributes assigned to the db.column
    id = db.Column(db.Integer, primary_key=True) #one class attribute used as a primary key
    name = db.Column(db.String)
    species = db.Column(db.String)
class User(db.Model):
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True,nullable=False,index=True)
    email=db.Column(db.String(120),unique=True)
    verified=db.Column(db.Boolean,default=False)