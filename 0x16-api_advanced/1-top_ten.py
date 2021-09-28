#!/usr/bin/python3
"""
    ADSFJSDIFJISDKFGJSIDKGJDSIKGJNFDSIK
"""

import requests


def top_ten(subreddit):
    """ DASFGKSOGJNMSDFIKOGJSDFGJDS """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-agent': 'PIBE'}
    conn = requests.get(url, headers=headers, allow_redirects=False)
    if conn.status_code == 200:
        try:
            for i in range(10):
                print(conn.json()['data']['children'][i]['data']['title'])
            return
        except IndexError:
            print(None)
    print(None)
