from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask!"

@app.route("/greeting")
def greeting():
    return "<h1>Hello user from flask</h1>"

@app.route("/greeting/<username>")
def greeting_username(username):
    return render_template("greeting.html", username=username)

@app.route("/greeting/<username>/<int:times>")
def greeting_username_multiple_time(username, times):
    return render_template("times.html", username=username, times=times)

@app.route("/float/<float:num>")
def float(num):
    return render_template("float.html", num=num)
@app.route("/users")
def all_users():
    app_name="Flask app"
    users=[
        {"id":1, "name": "Joe"},
        {"id":2, "name": "Jane"},
        {"id":3, "name": "Bob"},
    ]
    return render_template("index.html", all_users_from_python= users, app_name=app_name)

if __name__ == "__main__":
    app.run(debug=True, port = 5001)