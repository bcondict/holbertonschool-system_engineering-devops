#!/usr/bin/python3
"""
export data in the JSON format.
    - Format: { "USER_ID": [{"task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
    {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"}, ... ]}
    - File name: USER_ID.json
"""

import json


if __name__ == "__main__":

    import requests
    from sys import argv
    import csv

    # base
    url = 'https://jsonplaceholder.typicode.com/users/'
    emp_id = argv[1]

    # complex
    users = requests.get('{}{}'.format(url, emp_id)).json()
    todos = requests.get('{}{}/todos'.format(url, emp_id)).json()

    filename = '{}.json'.format(emp_id)
    with open(filename, 'w') as file:
        my_list = []
        for task in todos:
            format_task = {
                "task": task['title'], "completed": task['completed'],
                "username": users['username']}

            my_list.append(format_task)
        dict_to_print = {users['id']: my_list}
        file.write(json.dumps(dict_to_print))
