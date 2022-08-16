from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from dotenv import load_dotenv
import os
load_dotenv() 
import MySQLdb
 

app = Flask(__name__)

#print (os.getenv('Password'))#}, @localhost/ {os.getenv("database")}')

app.config['SQLALCHEMY_DATABASE_URI'] =f"mysql://root:{os.getenv('password')}@localhost/{os.getenv('database')}"


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
 
db = SQLAlchemy(app)

ma = Marshmallow(app)
 
 

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


 
 
 
 
 

@app.route('/post', methods = ['POST'])
def add_post():
    EmpName = request.json['EmpName']
    email = request.json['email']
    
 
    my_posts = Employee(EmpName, email)
    db.session.add(my_posts)
    db.session.commit()
 
    return post_schema.jsonify(my_posts)




    
@app.route('/post_dept', methods = ['POST'])
def add_postDept():
    DeptName = request.json['DeptName']
    Room = request.json['Room']
    
 
    my_posts = Department(DeptName, Room)
    db.session.add(my_posts)
    db.session.commit()
 
    return post_schema.jsonify(my_posts)



 
 
 

@app.route('/get', methods = ['GET'])
def get_post():
    all_posts = Employee.query.all()
    result = posts_schema.dump(all_posts)
 
    return jsonify(result)
 
 

@app.route('/details/<id>/', methods = ['GET'])
def post_details(id):
    post = Employee.query.get(id)
    return post_schema.jsonify(post)
 
 

@app.route('/update/<id>/', methods = ['PUT'])
def post_update(id):
    post = Employee.query.get(id)
 
    EmpName = request.json['EmpName']
    email= request.json['email']
    
 
 
    post.EmpName = EmpName
    post.email = email
   
 
    db.session.commit()
    return post_schema.jsonify(post)
 
 
 

@app.route('/delete/<id>/', methods = ['DELETE'])
def post_delete(id):
    post = Employee.query.get(id)
    db.session.delete(post)
    db.session.commit()
 
    return post_schema.jsonify(post)
 
 
 
 
if __name__ == "__main__":
    app.run(debug=True)