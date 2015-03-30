import urllib2, urllib

mmurl = 'http://mm.taobao.com/json/request_top_list.htm?type=0&page=1'
i = 0
ph = -1
pj = 0
j= 0
temp = '<img src="'
while i < 1:
    url = mmurl + str(i)
    up = urllib2.urlopen(url)
    cont = up.read()
    print '--------------------------------------'
    #print cont
    '''
    head = "<img src="
    tail = ".jpg"
    ph = cont.find(head)
    pj = cont.find(tail, ph + 1)
    print cont[ph + len(temp): pj + len(tail)]
    '''
    print '--------------------------------------'
    ahref = "<a href"
    target = "target"
    pa = cont.find(ahref)
    pt = cont.find(target, pa)
    #print cont[pa + len(ahref) + 2 : pt-2]
    modelurl = cont[pa + len(ahref) + 2 : pt-2]
    mup = urllib2.urlopen(modelurl)
    mcont = mup.read()
    #print mcont
    print '--------------------------------------'
    imgh = "<img style="
    imge = ".jpg"
    temp1 = mcont
    jph = 0
    while True:
        jph = temp1.find(imgh)
        if jph == -1:
            break
        jpe = temp1.find(imge, jph)
        mpic = temp1[jph : jpe + len(imge)]
        jps = mpic.find("src")
        urlpic = mpic[jps + 5 : jpe + len(imge)]
        print urlpic
        temp1 = temp1[jpe+len(imge):-1]
        print temp1
        urllib.urlretrieve(urlpic, "pic\\aa_%s.jpg" % j)
        j += 1
    print '--------------------------------------'
    i += 1
