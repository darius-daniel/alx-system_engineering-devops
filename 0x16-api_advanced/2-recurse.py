#!/usr/bin/python3
"""Contains a function that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit"""
import requests


def grow_hot_list(hot_list, hot_posts):
    """Recursively append the titles of the hot posts to the hot_list. """
    if len(hot_posts) > 0:
        hot_list.append(hot_posts[0]["data"]["title"])
        hot_posts.pop(0)
        grow_hot_list(hot_list, hot_posts)


def recurse(subreddit, hot_list=[], after=None):
    """Queries the Reddit API and prints, recursively, the titles of the first
    10 hot posts listed for a given subreddit. """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
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
            grow_hot_list(hot_list, hot_posts)
    else:
        return None

    after = params["data"]["after"]
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list=hot_list, after=after)
