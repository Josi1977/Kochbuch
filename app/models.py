from datetime import datetime
from app import db

class User(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(64), index=True, unique=True)
    email= db.Column(db.String(120), index=True, unique=True)
    password_hash= db.Column(db.String(128))

    def toDict(self):
        return dict(id=self.id, username=self.username, email=self.email)

class Recipe(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    recipename= db.Column(db.String(20), nullable=False)
    ingredients= db.Column(db.String(300), nullable=False)
    cookingistructions= db.Column(db.String(400),nullable=False)
    user_id= db.Column(db.Integer, db.ForeignKey(User.id))

    def toDict(self):
        return dict(recipename=self.recipename, ingredients=self.ingredients, cookingistrucions=self.cookingistructions)