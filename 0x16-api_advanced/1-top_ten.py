#!/usr/bin/python3
''' queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit
'''

import requests


def top_ten(subreddit):
    '''get request to find and sort hot posts
    '''
    headers = {'User-agent': 'Mozilla/5.0'
               'AppleWebKit/537.36'
               'Chrome/76.0.3809.100 Safari/537.36'}

    response = requests.get('https://www.reddit.com/r/{}/hot.json'
                            .format(subreddit), headers=headers)

    if 'error' in response.json():
        print('None')
        return 0

    for i in range(10):
        print(response.json().get('data').get('children')[i]
              .get('data').get('title'))
