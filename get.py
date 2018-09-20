import os
import json
import urllib2


os.system('cls')
url = 'http://dweet.io:443/get/latest/dweet/for/test'    
req = urllib2.Request(url)
response = urllib2.urlopen(req)
x = response.read()
x =json.loads(x)
print response

