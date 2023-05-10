#!/usr/bin/python3
"""This module provides a function to query the Reddit API and return the number of subscribers of a given subreddit.

Usage:
    python 0-subs.py subreddit

Example:
    To get the number of subscribers of the "Python" subreddit, run:
    python 0-subs.py python
"""

"""Module to query the Reddit API and returns the number of subscribers	"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Function to return the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        try:
            return response.json().get("data").get("subscribers")
        except AttributeError:
            # Handle the case when the JSON response doesn't
            # contain the expected field
            return 0
    else:
        # Handle the case when the subreddit is invalid or not found
        return 0


if __name__ == "__main__":
    if len(sys.argv) == 2:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(f"{subreddit} has {subscribers} subscribers.")
    else:
        print("Usage: python 0-subs.py subreddit")
