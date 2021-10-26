#!/usr/bin/python3
''' SDFGHNSDFJUHSDFN ADSFSUDJF SDFSD fsdf DSFDSFSDF '''
import requests


def recurse(subreddit, hot_list=[], times=0):
    ''' DFSUDFJHSDs DF DSIF JSDFJ SDJF DS FsdFSDFDS '''
    url = "https://reddit.com/r/"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)\
                              Gecko/20100101 Firefox/15.0.1"}
    response = requests.get(url + subreddit + "/hot.json?limit=10",
                            headers=headers)
    if times == 10:
        return
    try:
        ret = response.json()['data']
        title = ret['children'][times]['data']['title']
        hot_list = recurse(subreddit, hot_list, times+1)
        hot_list.append(title)
        return (hot_list)
    except:
        return(None)
