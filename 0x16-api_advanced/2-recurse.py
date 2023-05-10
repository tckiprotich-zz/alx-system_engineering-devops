#!/usr/bin/python3
"""Module to recursively get all hot articles in a subreddit.

This module provides a function that recursively retrieves all the "hot" articles
in a given subreddit. The function takes a subreddit name as an argument and returns
a list of article titles. The function uses the Reddit API to make HTTP GET requests
and parse JSON responses.

Example:
    To get all the hot articles in the "Python" subreddit, run:
    python recurse.py python

Note:
    The Reddit API has rate limits. If you make too many requests in a short period
    of time, you may receive a "429 Too Many Requests" response. To avoid this, you
    can use a library like `praw` that handles rate limits automatically.

"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.

    - If not a valid subreddit, return None.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            hot_list.append(title)
        after = req.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
