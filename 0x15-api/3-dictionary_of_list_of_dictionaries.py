#!/usr/bin/python3

import json
import requests


def get_tasks_status():
    todos = requests.get('https://jsonplaceholder.typicode.com/todos/').json()

    todos_dict = {}
    u_id = 0

    for items in todos:
        if items.get('userId') != u_id:
            u_id = items.get('userId')

        users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(u_id))

        name = users.json().get('username')

        if u_id not in todos_dict.keys():
            todos_dict[u_id] = []

        if items.get('userId') == int(u_id):
            todos_dict[u_id].append({'username': name,
                                     'task': items.get('title'),
                                     'completed': items.get('completed')})

    return todos_dict


if __name__ == '__main__':
    json_dict = get_tasks_status()

    with open('todo_all_employees.json', 'w') as file:
        json.dump(json_dict, file)
