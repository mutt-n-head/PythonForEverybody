# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ').strip()
sCount = raw_input('Enter count: ').strip()
sPosition = raw_input('Enter positions: ').strip()

# Retrieve all of the anchor tags
tCount = int(sCount)
tPosition = int(sPosition)
count = 0
position = 0

while count <= tCount:
    print "Retreiving:  " + url
    html = urllib.urlopen(url).read()
    # html = open(url, 'r').read()
    soup = BeautifulSoup(html)

    tags = soup('a')

    # print len(tags)

    if len(tags) >= tPosition:
        tag = tags[tPosition - 1]
        url = tag.get('href', None)
        count = count + 1
    else:
        break