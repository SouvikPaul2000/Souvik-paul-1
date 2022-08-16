from flask import Flask, request, jsonify
from Src import app
from Src.models import Employee
from Src.models import Department
from  Src.models import db, post_schema,posts_schema



@app.route('/post', methods = ['POST'])
def add_post():
    EmpName = request.json['EmpName']
    email = request.json['email']
   
 
    my_posts = Employee(EmpName, email)
    db.session.add(my_posts)
    db.session.commit()
 
    return post_schema.jsonify(my_posts)





    
@app.route('/postD', methods = ['POST'])
def add_postD():
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
 
 

@app.route('/post_details/<id>/', methods = ['GET'])
def post_details(id):
    post = Employee.query.get(id)
    return post_schema.jsonify(post)
 

@app.route('/post_update/<id>/', methods = ['PUT'])
def post_update(id):
    post = Employee.query.get(id)
 
    EmpName = request.json['Empname']
    email = request.json['email']
    
 
 
    post.title = EmpName
    post.description = email
    
 
    db.session.commit()
    return post_schema.jsonify(post)
 
 
 

@app.route('/post_delete/<id>/', methods = ['DELETE'])
def post_delete(id):
    post = Employee.query.get(id)
    db.session.delete(post)
    db.session.commit()
 
    return post_schema.jsonify(post)
 
 
 