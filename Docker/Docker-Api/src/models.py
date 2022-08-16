from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from src import app
import pymysql
from dotenv import load_dotenv
import os
load_dotenv() 
import MySQLdb
 
# app = Flask(__name__)
# print(os.getenv('password')) 
#print(f"mysql://root:{os.getenv('MYSQL_ROOT_PASSWORD')}@localhost/{os.getenv('database')}")

#var1=f"mysql+pymysql://root:{os.getenv('password')}@localhost:3307/{os.getenv('database')}"
   
#app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{os.getenv('MYSQL_ROOT_PASSWORD')}@{os.getenv('name')}/{os.getenv('database')}"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{}:{}@{}:{}/{}".format(os.getenv('MYSQL_ROOT_USERNAME'),os.getenv('MYSQL_ROOT_PASSWORD'),os.getenv('HOST_NAME'), os.getenv('PORT'), os.getenv('DBNAME'))
print(app.config['SQLALCHEMY_DATABASE_URI'])
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:{}@{}/{}".format(os.getenv('MYSQL_ROOT_PASSWORD'),os.getenv('HOST_NAME'), os.getenv('DBNAME'))
#print("mysql+pymysql://root:{}@{}:{}/{}".format(os.getenv('MYSQL_ROOT_PASSWORD'),os.getenv('HOST_NAME'), os.getenv('PORT'), os.getenv('DBNAME')))
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Souvik@souviksql:3306/database4"
#print(app.config['SQLALCHEMY_DATABASE_URI'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
 
 
db = SQLAlchemy(app)
ma = Marshmallow(app)
 
 






class Department(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    DeptName = db.Column(db.String(100))
    Room = db.Column(db.String(200))
    
 
 
    def __init__(self, DeptName, Room):
        self.DeptName = DeptName
        self.Room = Room
       
 
 
class PostSchema(ma.Schema):
    class Meta:
        fields = ("DeptName", "Room")
 
 
post_schema = PostSchema()
posts_schema = PostSchema(many=True)






class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    EmpName = db.Column(db.String(100))
    email = db.Column(db.String(200))
    
 
 
    def __init__(self, EmpName,department_id, email):
        self.EmpName = EmpName
        self.department_id  = department_id 
        self.email = email
        
       
 
 
class PostSchema(ma.Schema):
    class Meta:
        fields = ("EmpName", "department_id " ,"email")
 
 
post_schema = PostSchema()
posts_schema = PostSchema(many=True)
 



'''results = db.session.query(Employee, Department).join(Department).all()

for employee, department in results:
    print(employee.EmpName, department.DeptName)

for result in results:
    print(result)'''