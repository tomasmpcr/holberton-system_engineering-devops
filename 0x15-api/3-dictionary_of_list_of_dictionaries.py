#!/usr/bin/python3
"""DFGSS GSFG SDFGDSF """


import sys

if __name__ == "__main__":
    import requests
    import json
    r_usuario = requests.get(
        "https://jsonplaceholder.typicode.com/users"
        ).json()

    f = open("todo_all_employees.json", "w+")
    todo = {}

    for i in r_usuario:
        r_lista = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                i["id"])).json()
        user = i["username"]
        lista = []
        for j in r_lista:
            ram = {}
            ram["username"] = user
            ram["task"] = j["title"]
            ram["completed"] = j["completed"]
            lista.append(ram)
        todo[i["id"]] = lista

    f.write(json.dumps(todo))
    f.close()
