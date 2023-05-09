#!/usr/bin/python3
"""
Recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a
sorted count of given keywords
"""
import sys
import requests
import json

def count_words(subreddit, word_list, after=None, count_dict={}):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json().get('data')
        children = data.get('children')
        if not children:
            sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
            return
        for child in children:
            title = child.get('data').get('title').lower()
            for word in word_list:
                if title.count(f" {word.lower()} ") > 0:
                    if word.lower() in count_dict:
                        count_dict[word.lower()] += title.count(f" {word.lower()} ")
                    else:
                        count_dict[word.lower()] = title.count(f" {word.lower()} ")
        after = data.get('after')
        if not after:
            sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
            return
        return count_words(subreddit, word_list, after=after, count_dict=count_dict)
    else:
        print("None")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 count.py <subreddit> <word_list>")
        sys.exit()
    subreddit = sys.argv[1]
    word_list = sys.argv[2:]
    count_words(subreddit, word_list)
