from flask_sqlalchemy import SQLAlchemy
from settings import app

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    author = db.Column(db.Text, nullable = False)
    description = db.Column(db.Text, nullable = False)
    publication = db.Column(db.Text, nullable = False)
    isIssued = db.Column(db.Text, nullable = False)
    issuedBy = db.Column(db.Text, nullable = False)

    def json(self):
        return {'id': self.id, 'name': self.name, 'author': self.author,
        'description': self.description, 'publication': self.publication,
        'isIssued' : self.isIssued , "issuedBy" : self.issuedBy
        }

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True, nullable=False)
    hash = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text )
    role = db.Column(db.Text)

    def json(self):
        return {'id': self.id, 'name': self.name, 'email': self.email,
        'role': self.role}


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True, nullable=False)
    hash = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text )
    role = db.Column(db.Text)

class Librarian(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True, nullable=False)
    hash = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text )
    role = db.Column(db.Text)

    def json(self):
        return {'id': self.id, 'name': self.name, 'email': self.email,
        'role': self.role}