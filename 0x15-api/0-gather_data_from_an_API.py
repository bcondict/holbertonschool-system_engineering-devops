#!/usr/bin/python3
"""
using this REST API, for a given employee ID
returns information about his/her list progress.
"""

if __name__ == "__main__":

    import requests
    from sys import argv

    # base
    url = 'https://jsonplaceholder.typicode.com/users/'
    emp_id = argv[1]

    # complex
    users = requests.get('{}{}'.format(url, emp_id)).json()
    todos = requests.get('{}{}/todos'.format(url, emp_id)).json()

    # to print
    done_task = []
    for task in todos:
        if task['completed'] is True:
            done_task.append(task['title'])

    print('Employee {} is done with tasks ({}/{}):'.format(
        users['name'], len(done_task), len(todos)))

    for task_title in done_task:
        print('\t {}'.format(task_title))
