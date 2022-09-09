#!/usr/bin/python3

import json


if __name__ == "__main__":

    import requests
    from sys import argv

    # base
    url = 'https://jsonplaceholder.typicode.com/users/'

    # complex
    users = requests.get(url).json()

    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
        emp_json = dict()
        for user in users:
            username = user.get('username')
            todos = requests.get('{}{}/todos'.format(url, user.get('id'))).json()

            tasks = list()
            for task in todos:
                format_task = {"username": user['username'], "task": task['title'], "completed": task['completed']}
                tasks.append(format_task)
            
            emp_json[user['id']] = tasks

        file.write(json.dumps(emp_json))

