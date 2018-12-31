# Calling a JSON API
#
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The
# program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data,
# and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as
# within Google Maps.
# API End Points
#
# To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
#
# http://py4e-data.dr-chuck.net/json?
# This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as
# often as you like. If you visit the URL with no parameters, you get "No address..." response.
# To call the API, you need to provide address that you are requesting as the address= parameter that is properly URL
# encoded using the urllib.urlencode() fuction as shown in http://www.py4e.com/code3/geojson.py
#
# Test Data / Sample Execution
#
# You can test to see if your program is working with a location of "South Federal University" which will have a place_
# id of "ChIJD6jp03IsDogRGm_7Gmbky5E".
#
# $ python3 solution.py
# Enter location: South Federal University
# Retrieving http://...
# Retrieved 2268 characters
# Place id ChIJD6jp03IsDogRGm_7Gmbky5E
# Turn In
#
# Please run your program to find the place_id for this location:
#
# Beloit College
# Make sure to enter the name and case exactly as above and enter the place_id and your Python code below. Hint: The
# first seven characters of the place_id are "ChIJBch ..."
# Make sure to retrieve the data from the URL specified above and not the normal Google API. Your program should work
# with the Google API - but the place_id may not match for this assignment.

import urllib.request, urllib.parse, urllib.error
import json

baseURL = 'http://py4e-data.dr-chuck.net/json?'
key = '42'

# Get location for lookup from user
address = input('Enter location: ')

# add address parameter to url
parms = dict()
parms['address'] = address
parms['key'] = key
url = baseURL + urllib.parse.urlencode(parms)

# fetch data, decode
raw = urllib.request.urlopen(url).read().decode()
data = json.loads(raw)
place_id = data['results'][0]['place_id']
print('Place ID: ', place_id)

