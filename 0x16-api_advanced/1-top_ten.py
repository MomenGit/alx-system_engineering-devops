#!/usr/bin/python3
"""Docs"""

import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    res = requests.get(url, allow_redirects=False)
    if res.status_code >= 300:
        print("None")
        return
    json = res.json()
    posts = json.get('data').get('children')
    for post in posts:
        print(post.get('data').get('title'))
