#!/usr/bin/python3

import json
import requests
import sys


def get_username(e_id):
    uname = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(e_id))

    username = uname.json().get('username')

    return username


def get_tasks_status(e_id, username):
    todos = requests.get('https://jsonplaceholder.typicode.com/todos/').json()

    todos_dict = {'{}'.format(e_id): []}

    for items in todos:
        if items.get('userId') == int(e_id):
            todos_dict['{}'.format(e_id)].append({
                                'task': items.get('title'),
                                'completed': items.get('completed'),
                                'username': username})

    return todos_dict


if __name__ == '__main__':
    e_id = sys.argv[1]
    uname = get_username(e_id)
    json_dict = get_tasks_status(e_id, uname)

    with open('{}.json'.format(e_id), 'w') as file:
        json.dump(json_dict, file)
