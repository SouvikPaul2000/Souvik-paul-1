from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from Src import app
import pymysql
from dotenv import load_dotenv
import os
load_dotenv() 
import MySQLdb
 
# app = Flask(__name__)
# print(os.getenv('password')) 
# print(f"mysql://root:{os.getenv('password')}@localhost/{os.getenv('database')}")

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{os.getenv('password')}@localhost/{os.getenv('database')}"
#app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{os.getenv('password')}@localhost/database3"
#print(app.config['SQLALCHEMY_DATABASE_URI'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
 
 
db = SQLAlchemy(app)
ma = Marshmallow(app)
 
 






class Department(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    DeptName = db.Column(db.String(100))
    Room = db.Column(db.String(200))
    
 
 
    def __init__(self, DeptName, Room):
        self.EmpName = DeptName
        self.email = Room
       
 
 
class PostSchema(ma.Schema):
    class Meta:
        fields = ("DeptName", "Room")
 
 
post_schema = PostSchema()
posts_schema = PostSchema(many=True)






class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    EmpName = db.Column(db.String(100))
    email = db.Column(db.String(200))
    
 
 
    def __init__(self, EmpName, email):
        self.EmpName = EmpName
        self.email = email
       
 
 
class PostSchema(ma.Schema):
    class Meta:
        fields = ("EmpName", "email")
 
 
post_schema = PostSchema()
posts_schema = PostSchema(many=True)
 