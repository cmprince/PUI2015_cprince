'''
Created on Sep 21, 2015

@author: cmp
'''

import sys
import json
from datetime import datetime as dt

if __name__ == '__main__':
    jsonFile = open(sys.argv[1],'r')
    metadata = json.load(jsonFile)
    print dt.fromtimestamp(metadata['createdAt'])