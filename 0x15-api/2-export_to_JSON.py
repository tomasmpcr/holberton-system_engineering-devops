#!/usr/bin/python3
"""DFGSS GSFG SDFGDSF """


import sys

if __name__ == "__main__":
    import requests
    import json
    r_usuario = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
        ).json()
    r_lista = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
         sys.argv[1])).json()

    user = r_usuario["username"]
    lista = []
    f = open("{}.json".format(sys.argv[1]), "w+")

    for i in r_lista:
        ram = {}
        ram["task"] = i['title']
        ram['completed'] = i['completed']
        ram['username'] = user
        lista.append(ram)

    cosa = {}
    cosa[sys.argv[1]] = lista

    f.write(json.dumps(cosa))
    f.close()
