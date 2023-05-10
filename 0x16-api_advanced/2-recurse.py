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
import sys


def recurse(subreddit, hot_list=[], after=None):
    """Function to recursively get all hot articles in a subreddit
    the subreeddit is passed during runtime"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json().get('data')
        children = data.get('children')
        if not children:
            return hot_list
        hot_list.extend([child.get('data').get('title') for child in children])
        after = data.get('after')
        if not after:
            return hot_list
        return recurse(subreddit, hot_list, after=after)
    else:
        return None


if __name__ == "__main__":
    subreddit = sys.argv[1]
    hot_list = recurse(subreddit)
    if hot_list:
        for i, title in enumerate(hot_list, start=1):
            print(f"{i}. {title}")
    else:
        print("No results found.")
