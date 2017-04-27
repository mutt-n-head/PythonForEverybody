# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
count = 0

for tag in tags:
    # Look at the parts of a tag
    # print 'TAG:',tag
    # print 'URL:',tag.get('href', None)
    # print 'Contents:',tag.contents[0]
    # print 'Attrs:',tag.attrs
    try:
        count = count + int(tag.contents[0])
    except:
        print "There was a non-number in the span"

print count

