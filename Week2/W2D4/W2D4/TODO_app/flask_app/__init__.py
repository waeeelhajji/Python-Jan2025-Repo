from flask import Flask

app=Flask(__name__)
app.secret_key="supersecretkey123"
DATABASE="todos_db"
