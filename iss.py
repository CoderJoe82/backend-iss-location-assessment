#!/usr/bin/env python

__author__ = '???'


from pip._vendor import requests


def main():
    r = requests.get('http://api.open-notify.org/astros.json').json()
    # print(r['people'])
    people = []
    for person in r['people']:
        people.append(person['name'])
    print(f"Names: {people}")

    space = requests.get('http://api.open-notify.org/iss-now.json').json()
    print(f"Geographical location; Lat: {space['iss_position']['latitude']}, Lon: {space['iss_position']['longitude']}")
    print(f"Timestamp: {space['timestamp']}")

    

if __name__ == '__main__':
    main()
