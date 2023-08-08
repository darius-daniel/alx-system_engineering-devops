#!/usr/bin/python3
"""
A script containing a function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers) for a given
subreddit. If an invalid subreddit is given, the function returns 0.
"""
import requests
import json


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and returns the total number of
    subscribers for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Chrome'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    params = json.loads(response.content.decode('utf-8'))

    if response.status_code == 200:
        try:
            total_subs = params["data"]["subscribers"]
        except KeyError:
            pass
        else:
            return total_subs
    else:
        return 0
