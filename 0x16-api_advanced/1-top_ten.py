#!/usr/bin/python3
"""Contains a function that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Chrome'}
    parameters = {"limit": 10}
    response = requests.get(
        url, headers=headers, params=parameters, allow_redirects=False
    )

    if response.status_code == 200:
        params = response.json()
        try:
            hot_posts = params["data"]["children"]
        except KeyError:
            print(None)
        else:
            for k in hot_posts:
                print("{}".format(k["data"]["title"]))
    else:
        print(None)
