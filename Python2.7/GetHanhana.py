#<a title="《论电影的七个元素》——关于我对电影的一些看法以及《后会无期》的一些消息" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102eo83.html">《论电影的七个元素》——关于我对电…</a>
#coding:utf-8
import urllib
import time
url = ['']*500
page = 1
link = 1
while page <= 7:
    con = urllib.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_'+ str(page) + '.html').read()
    title = con.find(r'<a title=')
    href = con.find(r'href=', title)
    html = con.find(r'.html', href)

    i = 0
    while title != -1 and href != -1 and html != -1 and i < 500:
        url[i] = con[href + 6: html + 5]
        print link, ' ', url[i]
        title = con.find(r'<a title=', html)
        href = con.find(r'href=', title)
        html = con.find(r'.html', href)
        i += 1
        link += 1
    else:
        print 'find end!'
    page += 1
else:
    print 'all find end!'
    
j = 0
while j < 60:
    content = urllib.urlopen(url[j]).read()
    open(r'hanhan/'+url[j][-26:], 'w+').write(content)
    print 'downloading', url[j]
    j += 1
    time.sleep(5)
else:
    print 'download article finished!'
