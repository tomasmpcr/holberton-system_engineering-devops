#!/usr/bin/python3
"""DFGSS GSFG SDFGDSF """


if __name__ == "__main__":
    import requests
    import sys
    r_usuario = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
        ).json()
    r_lista = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
         sys.argv[1])).json()

    lista = []
    number_of_done_task = 0
    total_number_of_task = 0

    for i in r_lista:
        total_number_of_task += 1
        if i["completed"] is True:
            number_of_done_task += 1
            lista.append(i["title"])

    print("Employee {} is done with tasks({}/{}):".format(
        r_usuario['name'],
        number_of_done_task,
        total_number_of_task))

    for lis in lista:
        print("\t {}".format(lis))
