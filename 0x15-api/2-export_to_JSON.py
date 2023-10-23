#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com/ REST API
For a given employee ID, returns information about his/her TODO list progress
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    usr_url = "https://jsonplaceholder.typicode.com/users"
    file_name = "{}.json".format(sys.argv[1])
    try:
        user = requests.get(
            "{url}/{id}".format(url=usr_url, id=sys.argv[1])).json()
        tasks = requests.get(
            "{url}/{id}/todos".format(url=usr_url, id=sys.argv[1])).json()
        tasks_list = []
        for task in tasks:
            tasks_list.append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user.get('username')
            })
        user_tasks = {user.get('id'): tasks_list}
        with open(file_name, 'w') as file:
            json.dump(user_tasks, fp=file)
    except Exception as e:
        pass
