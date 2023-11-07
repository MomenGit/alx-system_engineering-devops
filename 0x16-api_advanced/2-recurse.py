#!/usr/bin/python3
"""Defines recurse function"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    a recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    res = requests.get(f"{url}?after={after}", allow_redirects=False)

    if res.status_code != 200:
        return None

    data = res.json().get('data')
    posts = data.get('children')

    for post in posts:
        hot_list.append(post.get('data').get('title'))
    print(hot_list)

    if data.get('after') is None:
        return hot_list
    return recurse(subreddit, hot_list, data.get('after'))
