"""
Change the code here to use the new WebCorpus type.
"""

###
### crawler.py
###

from webcorpus import WebCorpus
from getpage import get_page
from bs4 import BeautifulSoup

def get_all_links(page):
    soup = BeautifulSoup(page)
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

def crawl_web(seed): # returns index, graph of inlinks
    tocrawl = set([seed])
    crawled = []
    wcorpus = WebCorpus()
    while tocrawl: 
        url = tocrawl.pop() # changed page to url - clearer name
        if url not in crawled:
            content = get_page(url)
            outlinks = get_all_links(content)
            for outlink in outlinks:
                wcorpus.add_link(url, outlink) 
            for word in content.split():
                wcorpus.add_word_occurrence(url, word)
            tocrawl.update(outlinks)
            crawled.append(url)
    return wcorpus


    


"""
Change the code here to use the new WebCorpus type.
"""

###
### crawler.py
###

from webcorpus import WebCorpus
from getpage import get_page
from bs4 import BeautifulSoup

def get_all_links(page):
    soup = BeautifulSoup(page)
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

def crawl_web(seed): # returns index, graph of inlinks
    tocrawl = set([seed])
    crawled = []
    wcorpus = WebCorpus()
    while tocrawl: 
        url = tocrawl.pop() # changed page to url - clearer name
        if url not in crawled:
            content = get_page(url)
            outlinks = get_all_links(content)
            for outlink in outlinks:
                wcorpus.add_link(url, outlink) 
            for word in content.split():
                wcorpus.add_word_occurrence(url, word)
            tocrawl.update(outlinks)
            crawled.append(url)
    return wcorpus


    


