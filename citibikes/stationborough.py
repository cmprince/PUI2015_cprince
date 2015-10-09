'''
citibike station locator
author: christopher prince

retrieve borough names (counties) for each station in the citibike system
'''

import json
import urllib2
import csv
from geopy.geocoders import Nominatim

url = 'https://www.citibikenyc.com/stations/json'
Fname = 'stationlist.csv'
request = urllib2.urlopen(url)
stationdata = json.loads(request.read())
stations = stationdata['stationBeanList']
geolocator = Nominatim()

header = ['id','county']
with open(Fname, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)

    for station in stations:
        stationid = station['id']
        lat = station['latitude']
        lon = station['longitude']

        location = geolocator.reverse(str(lat) + ', ' + str(lon))
        county = location.raw['address']['county']
        zp = location.raw['address']['postcode']

        #correct for an occasionally dropped 'county' in the return
        if county == 'New York':
            county = 'New York County'
            print location.raw['address']

        csvwriter.writerow([stationid, county])
        print stationid, county, zp
