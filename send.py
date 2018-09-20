import urllib
import urllib2
import random
import string

for i in range(100):
    x = random.randint(0, 1000)
    y = str(x)
    url = 'https://dweet.io:443/dweet/for/test'
    data = urllib.urlencode({'Random' : y})
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    re = response.read()
    print re
