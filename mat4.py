# -*- coding: utf-8 -*-
"""
Created on Tue May 11 11:53:12 2021

@author: User
"""

import json, requests
destionations= open('dests.txt','r',encoding='utf-8')
File=destionations.readlines()

api_key = 'AIzaSyABQP77w7L9h2hYjiYR4cpioBwZ90U--BA'
url_disatance = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
url_geocode = 'https://maps.googleapis.com/maps/api/geocode/json?'

dis=dict()
longest_distance=list()
for dest in File:
    result = requests.get(url_disatance+'origins=' + 'תל%אביב' + '&destinations='+ dest +'&key=' + api_key).json() 
    km = result['rows'][0]['elements'][0]['distance']['text']
    longest_distance.append(km)
    duration= result['rows'][0]['elements'][0]['duration']['text']
    result = requests.get(url_geocode+'address=' +dest+ '&key='+api_key).json()
    lat= result['results'][0]['geometry']['location']['lat']
    lng= result['results'][0]['geometry']['location']['lng']
    dis[dest]={'distance' : km , 'duration' : duration , 'latitude' : lat , 'longitude' : lng}
    print(dest)
    dest={'distance' : km , 'duration' : duration , 'latitude' : lat , 'longitude' : lng}
    print(dest)

longest_distance.sort()

print(f'\n The three longest distances from Tel-Aviv is: ')

i=len(longest_distance)-1
while i>1:
    print(longest_distance[i])
    i=i-1