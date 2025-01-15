from flask import render_template,session,redirect,request
from flask_app import  app

from flask_app.models.todos_model import Todo

@app.route("/")
def get_todos():
    session["user_id"]=2
    
    potato =Todo.get_all()
    return render_template("todos.html", list_of_todos=potato)

@app.route("/todo/form")
def go_to_add_todo():
    return render_template("todo_form.html")

@app.route("/todo/add",methods=["POST"])
def add_todo():
    new_todo={
        "name":request.form["todo_name"],
        "status":request.form["todo_status"],
        "user_id":session["user_id"]
    }
    result=Todo.create_one(new_todo)
    return redirect("/")
    