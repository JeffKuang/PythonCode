import urllib2

req = urllib2.Request('http://bbs.csdn.net/callmewhy')

def test(x):
	return x * 2
	
try:
    urllib2.urlopen(req)
except urllib2.URLError, e:
    print e.code