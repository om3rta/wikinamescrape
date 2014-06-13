import urllib2
from BeautifulSoup import BeautifulSoup


class WikiNameScrape:

    def __init__(self):
        self.names = {}
        self.count = 0


    def grab_names(self, flag, run_times):
        while self.count < run_times:
            name_number = 0
            finalname_last = ""
            while name_number != 2:
                if flag == "urban":
                    soup = BeautifulSoup(urllib2.urlopen('http://www.urbandictionary.com/random.php').read())
                else:
                    soup = BeautifulSoup(urllib2.urlopen('http://en.wikipedia.org/wiki/Special:Random').read())
                wikititle = soup.find('title')
                wikistr = str(wikititle)
                if flag == "urban":
                    wikisplit = wikistr.split(":", 1)
                else:
                    wikisplit = wikistr.split(" ", 1)
                wikilongname = wikisplit[1]
                if flag == "urban":
                    wikismallername = wikilongname.split("<", 1)
                    wikifirstname = wikismallername[0]
                    wikionename = wikifirstname.split(" ", 1)
                    wikifinalname = wikionename[1]
                    wikifinal_final = wikifinalname.split(" ", 1)
                    finalname = wikifinal_final[0]
                else:
                    wikisplitlong = wikilongname.split(" ", 1)
                    finalname = wikisplitlong[0]
                if name_number % 2 == 0:
                    finalname_first = finalname
                else:
                    finalname_last = finalname
                name_number = name_number + 1
            self.dict_add(finalname_first, finalname_last)
        return self.names

    def dict_add(self, new_first, new_last):
            if str.isalpha(new_first) and str.isalpha(new_last):
                self.names['User_%s' % self.count] = {'first': new_first, 'last': new_last}
                self.count = self.count + 1

scraper = WikiNameScrape()
scraped_name = scraper.grab_names("urban", 10)

print scraped_name
