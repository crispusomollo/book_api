from flask import Flask
from flask_pymongo import PyMongo
from config.settings import Config

app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)

# User Model
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def to_dict(self):
        return {"username": self.username, "email": self.email}

# Book Model
class Book:
    def __init__(self, title, author, user_id):
        self.title = title
        self.author = author
        self.user_id = user_id

    def to_dict(self):
        return {"title": self.title, "author": self.author, "user_id": self.user_id}

