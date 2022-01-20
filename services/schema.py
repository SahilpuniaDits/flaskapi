from flask_marshmallow import Marshmallow
# from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from flask import Flask
import models.employee as schma
from models.db import db,ma


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/flask'
# db = SQLAlchemy(app)
# # migrate = Migrate(app, db)
# ma = Marshmallow(app)


class employeeSchema(ma.Schema):
   class Meta(ma.Schema.Meta):
       model = schma.Employee
       sqla_session = db.session
   id = fields.Number(dump_only=True)
   name = fields.String(required=True)
   email = fields.String(required=True)
   mobile = fields.Integer(required=True)
   department = fields.String(required=True)
   joining_date = fields.Date(required=True)
   designation = fields.String(required=True)
   experience = fields.String(required=True)
   level = fields.Integer(required=True)
   left_date = fields.Date(required=True)
   dob = fields.Date(required=True)