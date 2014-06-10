#WikiNameScrape gathers names for use in testing from Wikipedia

import urllib2
from BeautifulSoup import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://en.wikipedia.org/wiki/Special:Random').read())
thetd = soup.find('title')

print thetd