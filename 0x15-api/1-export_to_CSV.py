#!/usr/bin/python3
"""DFGSS GSFG SDFGDSF """


import sys

if __name__ == "__main__":
    import requests
    r_usuario = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
        ).json()
    r_lista = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
         sys.argv[1])).json()

    user = r_usuario["username"]
    f = open("{}.csv".format(sys.argv[1]), "w+")

    for i in r_lista:
        f.write("\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
            sys.argv[1], user, i["completed"], i["title"]))
    f.close()
