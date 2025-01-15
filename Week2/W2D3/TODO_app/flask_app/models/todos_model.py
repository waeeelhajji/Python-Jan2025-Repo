from flask_app.config.connecttomysql import connect_to_mysql

class Todo:
    def __init__(self,data):
        self.id=data["id"]
        self.name=data["name"]
        self.status=data["status"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.user_id=data["user_id"]
        
    @classmethod
    def get_all(cls):
        query="select * from todos"
        result=connect_to_mysql("todos_db").query_db(query)
        # print(result)
        
        # print(new_todo.name)
        # print(new_todo.user_id)
        list_of_todos=[]
        for element in result:
            # print(element)
            new_todo=Todo(element)
            print(new_todo.name)
            list_of_todos.append(new_todo)
        return list_of_todos
    
    @classmethod
    def create_one(cls,data):
        query="insert into todos(name,status,user_id) values (%(name)s,%(status)s,%(user_id)s)"
        result=connect_to_mysql("todos_db").query_db(query,data)
        return result
        
        