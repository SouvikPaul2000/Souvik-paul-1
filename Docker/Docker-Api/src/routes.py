from flask import Flask, request, jsonify
from src import app
from src.models import Employee
from src.models import Department
from src.models import db, post_schema, posts_schema
import os


@app.route('/')
def index():

    return "Docker Api"



@app.route('/postD', methods = ['POST'])
def add_postd():
    DeptName = request.json['DeptName']
    Room = request.json['Room']
   
 
    my_posts = Department(DeptName, Room)
    db.session.add(my_posts)
    db.session.commit()
 
    return post_schema.jsonify(my_posts)

@app.route('/post', methods = ['POST'])
def add_post():
    EmpName = request.json['EmpName']
    department_id  = request.json['department_id']
    email = request.json['email']
   
 
    my_posts = Employee(EmpName, department_id, email)
    db.session.add(my_posts)
    db.session.commit()
 
    return post_schema.jsonify(my_posts)

@app.route('/geta', methods = ['GET'])
def get_posta():
    all_posts = Employee.query.all()
    result = posts_schema.dump(all_posts)
 
    return jsonify(result)    


@app.route('/get', methods = ['GET'])
def get_postg():
    print("Hi")
    all_posts = db.session.query(Employee.id,Employee.EmpName,Department.DeptName).join(Department,Department.id==Employee.department_id,isouter=False).all()
    val=[]
    print(all_posts)
    for ans in all_posts:
        dic={}
        id=ans.id
        name=ans.EmpName
        dept=ans.DeptName
        dic=id,name,dept
        val.append(dic)
    return jsonify(val)    


@app.route('/getd', methods = ['GET'])
def get_postgd():
    all_posts = db.session.query(Employee.id,Employee.EmpName,Department.DeptName,Department.Room).filter(Department.id==Employee.department_id)
    val=[]
    for ans in all_posts:
        print(ans)
        dic={}
        id=ans.id
        name=ans.EmpName
        dept=ans.DeptName
        room=ans.Room
        dic=id,name,dept,room
        # E_Name= "E_Name: " + str (ans.id)
        # D_id= "D_id: " + str (ans.department_id)
        # D_Name= "D_Name: " + str (ans.DeptName)
        # D_Room= "D_Room: " + str (ans.Room)
        
        
        # dic=E_Name,D_id,D_Name,D_Room
        val.append(dic)
    return jsonify(val)   

app.route('/post_delete/<id>/', methods = ['DELETE'])
def post_delete(id):
    post = Employee.query.get(id)
    db.session.delete(post)
    db.session.commit()
 
    return post_schema.jsonify(post)
    
 
    
 


   

    
    
#@app.route('/getd', methods = ['GET'])
# def get_postd():
    

#     all_posts = db.session.query(Employee, Department).filter(Department.id == Employee.department_id).all()
    
'''
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
 
    return post_schema.jsonify(post)'''
 
 
 