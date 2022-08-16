import MySQLdb
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
load_dotenv() 

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{os.getenv('password')}@localhost/{os.getenv('database')}"
#app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:Souvik@localhost/database5"
app.config['SQLALCHEMY_TRACK_MODIFICATION']= False


db = SQLAlchemy(app)

class Department(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    DeptName = db.Column(db.String(100))
    Room = db.Column(db.String(200))
    
 
 
    def __init__(self, DeptName, Room):
        self.DeptName = DeptName
        self.Room = Room

class Employee (db.Model):
    id=db.Column(db.Integer,primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    Emp=db.Column(db.String(80),nullable=False)
    email=db.Column(db.String(80),nullable=False)


    def __init__(self,Emp,department_id,email):
        self.Emp=Emp
        self.email=email
        self.department_id=department_id