#!/usr/bin/python3

import csv
import requests
import sys


def get_username(e_id):
    uname = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(e_id))

    username = uname.json().get('username')

    return username


def get_tasks_status(e_id, username):
    todos = requests.get('https://jsonplaceholder.typicode.com/todos/').json()

    todos_list = []

    for items in todos:
        if items.get('userId') == int(e_id):
            todos_list.append(['{}'.format(e_id),
                               '{}'.format(username),
                               '{}'.format(items.get('completed')),
                               '{}'.format(items.get('title'))])

    return todos_list


if __name__ == '__main__':
    e_id = sys.argv[1]
    uname = get_username(e_id)
    csvlist = get_tasks_status(e_id, uname)

    with open('{}.csv'.format(e_id), 'w') as file:
        fileWrite = csv.writer(file, quoting=csv.QUOTE_ALL)
        fileWrite.writerows(csvlist)
