import urllib.request as client
import urllib.parse as parser
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    # address = raw_input('Enter location: ')
    # if len(address) < 1 :
    #     break

    address = '4243 Barn Raisers Drive'
    url = serviceurl + parser.urlencode({'sensor':'false', 'address': address})
    print('Retrieving {0}'.format(url))
    print('Retrieving {0}'.format(url))

    req_obj = client.Request(url)
    uh = client.urlopen(req_obj)

    data = uh.read()
    print('Retrieved {0} characters'.format(len(data)))

    # print data
    tree = ET.fromstring(data)
    # comments = tree.findall('.//count')
    comments = tree.findall('comments/comment')

    total = 0

    for comment in comments:
        total += int(comment.find('count').text)
        # print comment.find('count').text

    print(total)

    # results = tree.findall('result')
    # lat = results[0].find('geometry').find('location').find('lat').text
    # lng = results[0].find('geometry').find('location').find('lng').text
    # location = results[0].find('formatted_address').text
    #
    # print 'lat',lat,'lng',lng
    # print location
