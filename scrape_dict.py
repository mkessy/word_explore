#Script to download all entries in the Online Etymology Dictionary

from bs4 import BeautifulSoup, SoupStrainer
import re
import urllib2
import pickle
import simplejson as json
import string
import pprint

#Base URL
BASE_URL = 'http://www.etymonline.com'

HEADER = {'User-Agent':
          "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)"}


#URLs have a letter and page number query
#http://www.etymonline.com/index.php?l=c&p=23
#in the above url the letter = c and p=23 (24 on the page since index is 0 based)


def open_url(url):
    request = urllib2.Request(url, None, HEADER)
    try:
        html = urllib2.urlopen(request)
    except urllib2.URLError as e:
        if e.code == 404:
            print("Page wasn't found!")
        raise
    return html

def build_url(letter, page=None):
    if page:
        url = BASE_URL+'/index.php?' + \
                'l='+letter+'&p='+page+'&allowed_in_frame=0'
    else:
        url = BASE_URL+'/index.php?' + \
                'l='+letter+'&allowed_in_frame=0'
    return url


def count_pages(soup):

    paging = soup.find('div', class_='paging')

    if paging:
        return len(paging.ul('li'))
    return 0


#Begin main page scraping
alphabet = string.lowercase

all_words = []
all_foreigns = []
all_crossrefs = []

for letter in alphabet:
    #for letter in alphabet:

    html = open_url(build_url(letter))
    letter_soup = BeautifulSoup(html,'html5lib')

    page_count = count_pages(letter_soup)

    for page in range(page_count):
#    for page in range(page_count):

        letter_soup = BeautifulSoup(open_url(build_url(letter, str(page))), 'html5lib')

        word_text = letter_soup.find('div', attrs={'id':'dictionary'})

        words = word_text.dl('dt')
        words = [''.join(list(tag.stripped_strings)) for tag in words]

        defs = word_text.dl('dd')
        defs = [''.join(list(tag.strings)) for tag in defs]

        foreigns = word_text.dl('span', class_='foreign')
        foreigns  = [''.join(list(tag.strings)) for tag in foreigns]

        crossrefs = word_text.dl('a', class_='crossreference')
        crossrefs = [''.join(list(tag.strings)) for tag in crossrefs]


        all_words = all_words + zip(words, defs)
        all_foreigns = all_foreigns + foreigns
        all_crossrefs = all_crossrefs + crossrefs

        print 'Current letter: %s\t\t Current page: %s' %(letter, page)



#with open('word_files/p_words.txt', 'w') as aw:
#    pickle.dump(dict(all_words), aw)
#
#with open('word_files/p_foreigns.txt', 'w') as af:
#    pickle.dump(set(all_foreigns), af)
#
#with open('word_files/p_crossrefs.txt', 'w') as ac:
#    pickle.dump(set(all_crossrefs), ac)
#


with open('word_files/j_words.txt', 'w') as aw:
    json.dump(dict(all_words), aw, ensure_ascii = False)

with open('word_files/j_foreigns.txt', 'w') as af:
    json.dump(list(set(all_foreigns)), af, ensure_ascii = False)

with open('word_files/j_crossrefs.txt', 'w') as ac:
    json.dump(list(set(all_crossrefs)), ac, ensure_ascii = False)



def main():
    #pprint.pprint(foreigns)
    print 'executing..'
    #pprint.pprint(words)
    #print
    #pprint.pprint(crossrefs)
    #print
    #pprint.pprint(defs)


if __name__ == '__main__':
    main()
