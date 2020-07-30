#!/usr/bin/env python

__author__ = 'Joseph Padgett'


from pip._vendor import requests
import turtle
import time
import urllib
import json

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
    
    space_station_longitude = float(space['iss_position']['longitude'])
    space_station_latitude = float(space['iss_position']['latitude'])

    space_coords = (space_station_longitude, space_station_latitude)
    print(space_coords)

    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('map.gif')
    screen.register_shape('iss.gif')
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.setheading(90)
    iss.penup()
    iss.goto(space_station_longitude, space_station_latitude)

    lat_indy = 39.7684
    lon_indy = 86.1581
    location_indy = turtle.Turtle()
    
    location_indy.penup()
    location_indy.color('yellow')
    location_indy.goto(lon_indy,lat_indy)
    location_indy.dot(5)
    location_indy.hideturtle()
    turtle.done()
    url_indy = 'http://api.open-notify.org/iss-pass.json?lat=39.7684&lon=86.1581&#8217'
    response_indy = urllib.request.urlopen(url_indy)
    result_indy = json.loads(response_indy.read())
    over_indy = result_indy['response'][1]['risetime']
    style = ('Arial',6,'bold')
    location_indy.write(time.ctime(over_indy),font = style)
if __name__ == '__main__':
    main()
