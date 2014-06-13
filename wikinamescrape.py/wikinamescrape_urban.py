import urllib2
from BeautifulSoup import BeautifulSoup


class WikiNameScrape:

    def grab_name(self):
        soup = BeautifulSoup(urllib2.urlopen('http://www.urbandictionary.com/random.php').read())
        wikititle = soup.find('title')
        wikistr = str(wikititle)
        wikisplit = wikistr.split(":", 1)
        wikilongname = wikisplit[1]
        wikismallername = wikilongname.split("<", 1)
        wikifirstname = wikismallername[0]
        wikionename = wikifirstname.split(" ", 1)
        wikifinalname = wikionename[1]
        wikifinal_final = wikifinalname.split(" ", 1)
        name = wikifinal_final[0]
        return name


    def dict_add(self, dict_name):
            count = 0
            while count != 10:
                name = WikiNameScrape().grab_name()
                if str.isalpha(name) and len(name) > 2:
                    dict_name['User_' + str(count)]['first'] = name
                    count = count + 1
                    print str(count) + " " + name
            count = 0
            while count != 10:
                name = WikiNameScrape().grab_name()
                if str.isalpha(name) and len(name) > 2:
                    dict_name['User_' + str(count)]['last'] = name
                    count = count + 1
                    print str(count) + " " + name


names = {
    'User_0': {'first': None, 'last': None}, 'User_1': {'first': None, 'last': None},
    'User_2': {'first': None, 'last': None}, 'User_3': {'first': None, 'last': None},
    'User_4': {'first': None, 'last': None}, 'User_5': {'first': None, 'last': None},
    'User_6': {'first': None, 'last': None}, 'User_7': {'first': None, 'last': None},
    'User_8': {'first': None, 'last': None}, 'User_9': {'first': None, 'last': None}
}

scraper = WikiNameScrape()
scraped_name = scraper.dict_add(names)
#urban_name = scraper.grab_name()
print names
print "example name: " + names['User_0']['first'] + " " + names['User_0']['last']
