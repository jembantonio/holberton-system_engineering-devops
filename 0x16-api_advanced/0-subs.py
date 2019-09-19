#!/usr/bin/python3
''' queries the Reddit API and returns the number of subscribers
    for a given subreddit
'''

import requests


def number_of_subscribers(subreddit):
    '''get request for number of subscribers
    '''
    headers = {'User-agent': 'Mozilla/5.0'
               'AppleWebKit/537.36'
               'Chrome/76.0.3809.100 Safari/537.36'}

    response = requests.get('https://www.reddit.com/r/{}/about.json'
                            .format(subreddit), headers=headers)

    if 'error' in response.json():
        return 0

    subs = response.json().get('data').get('subscribers')
    return subs
