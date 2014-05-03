scrapeMail
==========

Scrape or extract email addresses from webpage
This code is written to extract or scrape email addresses from webpage.
eg:
This code will extract email addreses from example.com webpage not from all of the webpages of example.com
and it will list the email addresses found from that webpage.

res=urllib2.urlopen('http://www.slt.lk/contact-us')
txt = res.read()
emails=re.findall(r'[\w\.-]+@[\w\.-]+',txt)
for email in emails:
    print email


