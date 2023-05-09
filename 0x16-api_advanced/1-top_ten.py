#!/usr/bin/python3
"""Module to request top 10 hot posts in a subreddit"""
import sys
import requests


def top_ten(subreddit):
    """Function to request top 10 hot posts in a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        for post in response.json().get('data').get('children'):
            print(post.get('data').get('title'))
    else:
        print("None")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: {} <subreddit>".format(sys.argv[0]))
        sys.exit(1)
    subreddit = sys.argv[1]
    top_ten(subreddit)
