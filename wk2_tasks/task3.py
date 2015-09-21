'''
Created on Sep 21, 2015

@author: cmp
'''

import sys
import urllib2
import json
from datetime import datetime as dt

if __name__ == '__main__':
    url = 'https://nycopendata.socrata.com/views/%s' % (sys.argv[1])
    request = urllib2.urlopen(url)
    metadata = json.loads(request.read())
    print dt.fromtimestamp(metadata['createdAt'])
