#!/usr/bin/python3
''' returns information about his/her TODO list progress given a rest api
'''

import requests
import sys


def get_emp_name(emp_id):
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(emp_id))

    name = user.json().get('name')

    return (name)


def get_total_tasks(emp_id):
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(emp_id)).json()

    total = 0
    for data in todos:
        total += 1

    return total


def get_compl_tasks(emp_id):
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(emp_id)).json()

    complete = 0
    for data in todos:
        if data.get('completed'):
            complete += 1

    return complete


def get_titles(emp_id):
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(emp_id)).json()

    title_list = []
    for data in todos:
        if data.get('completed'):
            title_list.append(data.get('title'))

    return title_list


if __name__ == '__main__':
    emp_id = sys.argv[1]
    print("Employee {} is done with tasks({}/{}):"
          .format(get_emp_name(emp_id),
                  get_compl_tasks(emp_id),
                  get_total_tasks(emp_id)))

    titles = get_titles(emp_id)

    for title in titles:
        print("\t {}".format(title))
