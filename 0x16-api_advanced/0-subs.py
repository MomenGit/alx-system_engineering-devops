#!/usr/bin/python3
"""Defines number_of_subscribers function"""
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    res = requests.get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), allow_redirects=False)
    if res.status_code >= 300:
        return 0
    json = res.json()
    data_dict = json.get('data')
    return (data_dict.get('subscribers'))
