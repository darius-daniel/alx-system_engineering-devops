#!/usr/bin/python3
"""Contains a function that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Queries the Reddit API and prints, recursively, the titles of the first
    10 hot posts listed for a given subreddit. """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Chrome'}
    parameters = {'after': after}
    response = requests.get(
        url, headers=headers, params=parameters, allow_redirects=False
    )

    if response.status_code == 200:
        params = response.json()
        try:
            hot_posts = params["data"]["children"]
        except KeyError:
            return None
        else:
            for post in hot_posts:
                hot_list.append(post["data"]['title'])

    after = params["data"]["after"]
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list=hot_list, after=after)