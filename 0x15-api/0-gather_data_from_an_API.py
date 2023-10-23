#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com/ REST API
For a given employee ID, returns information about his/her TODO list progress
"""

if __name__ == "__main__":
    import requests
    import sys
    usr_url = "https://jsonplaceholder.typicode.com/users"
    try:
        user = requests.get(
            "{url}/{id}".format(url=usr_url, id=sys.argv[1])).json()

        tasks = requests.get(
            "{url}/{id}/todos".format(url=usr_url, id=sys.argv[1])).json()

        done_tasks = requests.get("{url}/{id}/todos?completed=true".format(
            url=usr_url, id=sys.argv[1])).json()

        print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
              len(done_tasks), len(tasks)))
        for task in done_tasks:
            print("\t {}".format(task.get('title')))
    except Exception as e:
        pass
