import re
import urllib2
res=urllib2.urlopen('http://www.slt.lk/contact-us')
txt = res.read()
emails=re.findall(r'[\w\.-]+@[\w\.-]+',txt)
for email in emails:
    print email
