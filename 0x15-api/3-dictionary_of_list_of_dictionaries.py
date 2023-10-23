#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com/ REST API
For a given employee ID, returns information about his/her TODO list progress
"""

if __name__ == "__main__":
    import json
    import requests

    usr_url = "https://jsonplaceholder.typicode.com/users"
    file_name = "todo_all_employees.json"
    try:
        users = requests.get(usr_url).json()
        users_todos = {}
        for user in users:
            todos = requests.get(
                "{url}/{id}/todos".format(url=usr_url,
                                          id=user.get('id'))).json()
            user_todos = []
            for todo in todos:
                user_todos.append({
                    "username": user.get('username'),
                    "task": todo.get('title'),
                    "completed": todo.get('completed')
                })
            users_todos[user.get('id')] = user_todos

        with open(file_name, 'w') as file:
            json.dump(users_todos, fp=file)
    except Exception as e:
        pass
