import json

import urllib

commCt = 0;

while True:
    commCt = 0
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    print 'Retrieving', address
    uh = urllib.urlopen(address)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    # print data
    info = json.loads(data)

    for item in info['comments']:
        commCt += item['count']

    print 'Count: ', commCt

