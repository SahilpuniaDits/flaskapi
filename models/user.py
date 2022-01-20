from models.db import app,db,migrate,ma
from flask import Flask
from passlib.apps import custom_app_context as pwd_context
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    _tablename_ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(52), index=True)
    password_hash = db.Column(db.String(128))
    
    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

db.create_all()