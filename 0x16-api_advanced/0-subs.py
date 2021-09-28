#!/usr/bin/python3
"""
	ADSFJSDIFJISDKFGJSIDKGJDSIKGJNFDSIK
"""

import requests


def number_of_subscribers(subreddit):
    """ DASFGKSOGJNMSDFIKOGJSDFGJDS """
    conn = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit),
                       headers={'User-agent': 'PIBE'})
    if conn.status_code == 200:
        try:
            return (conn.json()['data']['subscribers'])
        except KeyError:
            return 0
    return 0

