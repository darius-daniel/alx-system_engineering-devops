#!/usr/bin/python3
"""Extends 0-gather_data_from_an_API and exports data to JSON file."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    todo_url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos'
    user_info_url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'

    tasks = json.loads(requests.get(todo_url).content)
    uinfo = json.loads(requests.get(user_info_url).content)

    data = {'{}'.format(uinfo.get('id')): []}

    for task in tasks:
        data['{}'.format(uinfo.get('id'))].append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': uinfo.get('username')
        })

    with open("{}.json".format(uinfo.get('id')), 'w') as f:
        json.dump(data, f)
