from flask import Flask, request, jsonify, make_response,url_for,abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
# from marshmallow_sqlalchemy import ModelSchema
import datetime
from flask_marshmallow import Marshmallow
from passlib.apps import custom_app_context as pwd_context
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, Api
# from routes import initialize_routes
auth = HTTPBasicAuth()

from models.db import db,ma
import models.employee as foo
import models.user as reg
import services.schema as s
# from .routes import initialize_routes

# from models.user import User

app = Flask(__name__)
# api = Api(app)
db = SQLAlchemy(app)
# initialize_db(app)
# initialize_routes(api)
# @app.route('/api/employee', methods=['POST'])
class add_employee(Resource):
    def post(self):
    # get data from request
        name = request.json['name']
        email = request.json['email']
        mobile = request.json['mobile']
        department = request.json['department']
        joining_date = request.json['joining_date']
        designation = request.json['designation']
        experience = request.json['experience']
        level = request.json['level']
        left_date = request.json['left_date']
        dob = request.json['dob']



        #Instantiate new user
        employee = foo.Employee(name, email, mobile, department,
                            joining_date, designation, experience, level, left_date, dob)
        #add new user
        db.session.add(employee)
        db.session.commit()
        return s.employeeSchema.jsonify(employee)


# @app.route('/api/employee', methods=['GET'])
class employeeget(Resource):
    def get():
        get_employee = foo.Employee.query.all()
        employee_schema =s.employeeSchema(many=True)
        employee = employee_schema.dump(get_employee)
        return make_response(jsonify({"employee": employee}))


# @app.route('/api/employee/<id>', methods=['GET'])
class get_employee_by_id(Resource):
    def get(id):
        get_employee = foo.Employee.query.get(id)
        todo_schema = s.employeeSchema()
        employee = todo_schema.dump(get_employee)
        return make_response(jsonify({"employee": employee}))


# @app.route('/api/employee/<id>', methods=['PUT'])
class update_employee_by_id(Resource):
    def put(id):
        data = request.get_json()
        get_employee = foo.Employee.query.get(id)
        if data.get('name'):
            get_employee.name = data['name']
        if data.get('mobile'):
            get_employee.mobile = data['mobile']
            
        if data.get('department'):
            get_employee.department = data['department']
        if data.get('joining_date'):
            get_employee.joining_date = data['joining_date']
        if data.get('designation'):
            get_employee.designation = data['designation']
        if data.get('experience'):
            get_employee.experience = data['experience']
        if data.get('level'):
            get_employee.level = data['level']
        if data.get('left_date'):
            get_employee.left_date = data['left_date']
        if data.get('dob'):
            get_employee.dob = data['dob']
            
            
        db.session.add(get_employee)
        db.session.commit()
        employee_schema = s.employeeSchema(
            only=['id', 'name', 'mobile', 'department', 'joining_date', 'designation', 'experience', 'level', 'left_date', 'dob'])
        employee = employee_schema.dump(get_employee)

        return make_response(jsonify({"employee": employee}))


# @app.route('/api/employee/<id>', methods=['DELETE'])
class delete_employee_by_id(Resource):
    def delete(id):
        get_employee = foo.Employee.query.get(id)
        db.session.delete(get_employee)
        db.session.commit()
        return make_response("", 204)


# @app.route('/api/users', methods=['POST'])
class register(Resource):
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')
        print(email,password,"<<<<<<<<<<<<<<<<<")
        if email is None or password is None:
            abort(400)  # missing arguments
            print(email,"**************")
        if reg.User.query.filter_by(email=email).first() is not None:
            abort(400)  # existing user
        user = reg.User(email=email)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'email': user.email}), 201


# @app.route('/api/login', methods=['POST'])    
class login_user(Resource):
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')
        
        user = reg.User.query.filter_by(email=email).first()
        
        passs = (pwd_context.verify(password, user.password_hash))
        
        if passs == True:
            
            
            
            return jsonify({'User': user.email, 'status':'successfully logged In'}), 201, 
        else:
            return jsonify({'status': 'Incorrect email or password'})


