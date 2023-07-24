#!/usr/bin/python3
"""Extends 0-gather_data_from_an_API and exports data as csv"""
import csv
import json
import requests
from sys import argv


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
    uinfo = json.loads(requests.get(user_info_url).content)

    with open('{}.csv'.format(argv[1]), 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        data = []
        for task in tasks:
            # "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
            csvwriter.writerow(
                [
                    uinfo.get('id'),
                    uinfo.get('username'),
                    task.get('completed'),
                    task.get('title')]
            )
