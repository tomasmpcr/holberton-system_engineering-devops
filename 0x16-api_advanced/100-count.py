#!/usr/bin/python3
''' SDFGHNSDFJUHSDFN ADSFSUDJF SDFSD fsdf DSFDSFSDF '''
import operator
import requests

def count_words(subreddit, word_list, json = None, word_list_count = 0, json_count = 0, list_p = {}, title_sep = None, title_count = 0, list_p_count = 0):
    ''' DFSUDFJHSDs DF DSIF JSDFJ SDJF DS FsdFSDFDS '''

    if (json is None):
        if len(word_list) <= 0:
            return(None)

        url = "https://reddit.com/r/{}/hot.json?limit=10".format(subreddit)
        headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)\
                                  Gecko/20100101 Firefox/15.0.1"}
        response = requests.get(url, headers=headers)
        json = response.json()['data']['children']

    if word_list_count >= len(word_list):
        word_list_count = 0
        json_count += 1
        title_sep = None
        title_count = 0
    else:
        try:
            if title_sep is None:
                title_sep = json[json_count]['data']['title'].split()
            elif (title_count >= len(title_sep)):
                word_list_count += 1
                title_count = 0
            
            if word_list_count < len(word_list):
                if word_list[word_list_count].lower() in title_sep[title_count].lower():
                    if (word_list[word_list_count] in list_p):
                        list_p[word_list[word_list_count]] += 1
                    else:
                        list_p[word_list[word_list_count]] = 1
                title_count += 1
        except:
            word_list_count += 1
            title_count = 0

    if json_count >= len(json):
        if (title_sep is None):
            title_sep = "ASDASD"
            list_p = sorted(list_p.items(), key=operator.itemgetter(1))
            list_p_count = len(list_p) - 1

        if list_p_count < 0:
            return(None)
        else:
            print("{}: {}".format(list_p[list_p_count][0], list_p[list_p_count][1]))
            list_p_count -= 1

    count_words(subreddit, word_list, json, word_list_count, json_count, list_p, title_sep, title_count, list_p_count)
