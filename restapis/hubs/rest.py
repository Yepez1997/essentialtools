import urllib
import sys
import pprint
import json
import argparse
import base64
import requests
import datetime

from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode


API_KEY = "c49f16a19f2dddc00e9156008cdb"

# how many people can attend a particular date 


def request():
    URL = 'https://candidate.hubteam.com/candidateTest/v3/problem/dataset'
    PARAMS = {'userKey' : API_KEY}
    print(u'Querying {0} ...'.format(URL))
    response = requests.get(url=URL, params=PARAMS)
    return response.json()

def get_partners():
    partners = request()['partners']
    #pprint.pprint(partners, indent=2)
    return partners

def structure_data():
    ## use map to keep track of country + dates + name 
    attending = {} # {name : {country : {date: [dates]}} ? 
    # get first n people - in this case get 100 
    for i in range(50):
        if i != None:
            objects = get_partners()[i]
            email = objects['email']
            country = objects['country']
            dates = objects['availableDates']
            attending[email] = {}
            attending[email][country] = dates #list
    return attending


def get_attending():
    attending = structure_data()
    #pprint.pprint(attending, indent=2)
    return attending




def most_available():
    # data 
    dates = get_attending()
    # country with total count 
    country_count = {}
    for i in dates:
        new_dict = dates[i]
        for j in new_dict:
            if j not in country_count:
                country_count[j] = 1
            else:
                country_count[j] += 1
    # countries with dates
    print(country_count)
    countries = {}
    for i in dates: 
        if i not in countries:
            new_dict = dates[i]
            for j in new_dict:
                countries[j] = new_dict[j]
        else:
            new_dict = dates[i]
            for j in new_dict:
                countries[j] += new_dict[j]
    print(countries)
    # find min time 
    # take greedy alg appraoch
    for i in countries:
        times = countries[i]
        print(times)

most_available()
