'''
Created on Sep 21, 2015

@author: cmp
'''

import sys
import urllib2
import json
from datetime import datetime as dt

if __name__ == '__main__':
    for dataID in sys.argv[1:]:
        url = 'https://nycopendata.socrata.com/views/%s' % (dataID)
        request = urllib2.urlopen(url)
        metadata = json.loads(request.read())
        print dataID, dt.fromtimestamp(metadata['createdAt'])
