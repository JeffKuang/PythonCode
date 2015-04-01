import urllib, urllib2

url = 'http://www.163.com/register.cgi'

values = {'name' : 'WHY',
            'location' : 'SDU',
            'language' : 'Python'}

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
page = response.read()
