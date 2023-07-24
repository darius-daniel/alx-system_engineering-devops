#!/usr/bin/python3
"""Extends 0-gather_data_from_an_API and exports data to JSON file."""
import json
import requests


if __name__ == "__main__":
    users_info_url = 'https://jsonplaceholder.typicode.com/users/'
    users = json.loads(requests.get(users_info_url).content)

    with open("todo_all_employees.json", 'w') as f:
        for user in users:
            data = {'{}'.format(user.get('id')): []}

            todo_url = (
                "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                    user.get('id')
                ))
            tasks = json.loads(requests.get(todo_url).content)

            for task in tasks:
                data['{}'.format(user.get('id'))].append({
                    'task': task.get('title'),
                    'completed': task.get('completed'),
                    'username': user.get('username')
                })

                json.dump(data, f)
