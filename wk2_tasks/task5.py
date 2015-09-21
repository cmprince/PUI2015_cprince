'''
Created on Sep 21, 2015

@author: cmp
'''

import sys
import csv
import urllib2
import json

if __name__ == '__main__':
    jsonFile = open(sys.argv[1],'r')
    data = json.load(jsonFile)
    stations = data['stationBeanList']

    csvFname = sys.argv[2]
    with open(csvFname, 'w') as csvfile:
        stwriter = csv.writer(csvfile)    
        stwriter.writerow(['Station Name','Latitude','Longitude'])
        for s in stations:
            if s['statusKey']!=1 and s['stationName'].startswith('Coming soon'):
                stationName = s['stationName'][13:]
                stationLat = s['latitude']
                stationLon = s['longitude']
                stwriter.writerow([stationName, stationLat, stationLon])
