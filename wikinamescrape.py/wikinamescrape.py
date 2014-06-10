#WikiNameScrape gathers names for use in testing from Wikipedia

import urllib2
from BeautifulSoup import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://en.wikipedia.org/wiki/Special:Random').read())
wikititle = soup.find('title')
wikistr = str(wikititle)
wikisplit = wikistr.split(" ", 1)
wikilongname = wikisplit[1]
wikisplitlong = wikilongname.split(" ", 1)
finalname = wikisplitlong[0]

#print type(wikititle)
#print wikistr
print wikisplitlong
print finalname

#finalname will end up being the first word in the title of a wiki article. This will sometimes end up being a character
#that is not alphanumeric. Need to run a check to make sure the string only contains letters and numbers

#need to add finalname to a dictionary. Need to end up with 20 first names and 20 last names