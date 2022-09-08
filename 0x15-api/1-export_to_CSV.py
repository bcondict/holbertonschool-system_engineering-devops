#!/usr/bin/python3
""" export data in the CSV format """


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

    filename = '{}.csv'.format(emp_id)

    with open(filename, 'w') as f:
        writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)

        for single in todos:
            row = [users.get('id'), users.get('username'),
                   single.get('completed'), single.get('title')]
            writer.writerow(row)
