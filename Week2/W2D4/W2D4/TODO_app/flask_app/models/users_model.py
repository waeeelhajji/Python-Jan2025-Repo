from flask_app.config.connecttomysql import connect_to_mysql
from flask_app import DATABASE
from flask_app.models.todos_model import Todo
class User:
    def __init__(self,data):
        self.id=data["id"]
        self.first_name=data["first_name"]
        self.last_name=data["last_name"]
        self.email=data["email"]
        self.password=data["password"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.list_of_todos=[]

    @classmethod
    def get_my_todos(cls,data):
        query="select * from users left join todos on users.id=todos.user_id where users.id=%(id)s"
        result=connect_to_mysql(DATABASE).query_db(query,data)
        print("8"*40)
        print(result)
        print("8"*40)
        current_user=User(result[0])
        for element in result:
            todo_data={
                "id":element["todos.id"],
                "name":element["name"],
                "status":element["status"],
                "created_at":element["todos.created_at"],
                "updated_at":element["todos.updated_at"],
                "user_id":element["user_id"]
                
            }
            new_todo=Todo(todo_data)
            print(new_todo.name)
            current_user.list_of_todos.append(new_todo)
        return current_user
        
        
        