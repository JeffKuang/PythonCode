import urllib2

req = urllib2.Request('http://www.baidu.com')
response = urllib2.urlopen(req)
page = response.read()
print page
