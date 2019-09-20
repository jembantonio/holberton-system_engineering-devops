#!/usr/bin/python3
''' recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit
'''

import requests


def recurse(subreddit, hot_list=[], name=None):
    '''get request to find and sort hot posts recursively
    '''
    headers = {'User-agent': 'Mozilla/5.0'
               'AppleWebKit/537.36'
               'Chrome/76.0.3809.100 Safari/537.36'}

    checknopost = requests.get('https://reddit.com/api/search_reddit_names.json',
                               headers=headers).json()

    if 'error' in checknopost.keys()
        return None    
    
    response = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'
                            .format(subreddit, name), headers=headers).json()
    name = response.get('data', {}).get('after', None)
    top = response.get('data', {}).get('children', [])

    if not top:
        return hot_list

    for titles in top:
        hot_list.append(titles.get('data').get('title'))

    if not name:
        return hot_list

    return recurse(subreddit, hot_list, name)
