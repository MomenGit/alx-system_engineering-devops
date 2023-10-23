#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com/ REST API
For a given employee ID, returns information about his/her TODO list progress
"""

if __name__ == "__main__":
    import requests
    import sys

    usr_url = "https://jsonplaceholder.typicode.com/users"
    file_name = "{}.csv".format(sys.argv[1])
    try:
        user = requests.get(
            "{url}/{id}".format(url=usr_url, id=sys.argv[1])).json()

        tasks = requests.get(
            "{url}/{id}/todos".format(url=usr_url, id=sys.argv[1])).json()

        with open(file_name, 'w') as file:
            for task in tasks:
                file.write('"{}","{}","{}","{}"\n'.format(
                    user.get('id'),
                    user.get('username'),
                    task.get('completed'),
                    task.get('title')))
    except Exception as e:
        pass
