from flask import render_template,session,redirect,request
from flask_app import  app
from flask_app.models.users_model import User

@app.route("/todo/my_todos",methods=["GET"])
def show_my_todos():
    data={
        "id":session["user_id"]
    }
    current_user=User.get_my_todos(data)
    return render_template("my_todos.html",current_user=current_user)
    