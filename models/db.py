from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from flask_marshmallow import Marshmallow
import pymysql
from flask_migrate import Migrate


app = Flask(__name__)
# app.config['SECRET_KEY'] = SECRET_KEY
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/employeeapi'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

ma = Marshmallow(app)