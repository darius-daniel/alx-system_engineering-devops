#!/usr/bin/python3
"""A script that returns a list of tasks for an employee id from an API."""
from sys import argv
import json
import requests


def count_completed(task_list):
    """Counts the number of completed tasks on the TODO list."""
    count = 0
    for t in task_list:
        if t.get('completed') is True:
            count += 1

    return count


if __name__ == "__main__":
    todo_url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos'
    user_info_url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'

    tasks = json.loads(requests.get(todo_url).content)
    user_info = json.loads(requests.get(user_info_url).content)

    print("Employee {} is done with tasks({}/{}):".format(
            user_info.get('name'), count_completed(tasks), len(tasks)))
    for task in tasks:
        if task.get('completed') is True:
            print("\t {}".format(task.get('title')))
