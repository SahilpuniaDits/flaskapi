# from flask import Flask
from flask_restful import Resource, Api


from services.employees import add_employee,employeeget,get_employee_by_id,update_employee_by_id,delete_employee_by_id,register,login_user


def initialize_routes(app):
    api = Api(app)
    api.add_resource(add_employee, '/api/employee')
    api.add_resource(employeeget,'/api/employeeget')
    api.add_resource(get_employee_by_id, '/api/employeegetbyid')
    api.add_resource(update_employee_by_id,'/api/employeeupdatebyid')
    api.add_resource(delete_employee_by_id,'/api/employeedeletebyid')
    api.add_resource(register, '/api/register')
    api.add_resource(login_user, '/api/login')

# servies folder m employee file m apis 
# and aap.py m inizilize and routes
