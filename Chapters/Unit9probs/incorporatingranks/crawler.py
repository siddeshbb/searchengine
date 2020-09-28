###
### crawler.py
###
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

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)
        
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]
    
# modify crawl_web to return a WebCorpus object that includes ranks
def crawl_web(seed): # returns index, graph of inlinks
    tocrawl = set([seed])
    crawled = []
    wcorpus = WebCorpus()
    wcorpus.ranks = {}
    while tocrawl: 
        url = tocrawl.pop() # changed page to url - clearer name
        if url not in crawled:
            content = get_page(url)
            add_page_to_index(wcorpus.index, url, content)
            outlinks = get_all_links(content)
            wcorpus.graph[url] = outlinks
            tocrawl.update(outlinks)
            crawled.append(url)
    compute_ranks(wcorpus)
    return wcorpus

# Modify this in the following way:
# - Instead of taking a graph as input, it should take a WebCorpus object.
# - Instead of returning a list, it should store the ranks in a ranks attribute of the WebCorpus object.
def compute_ranks(wcorpus):
    d = 0.8 # damping factor
    numloops = 10
    
    ranks = {}
    npages = len(wcorpus.graph)
    for page in wcorpus.graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {}
        for page in wcorpus.graph:
            newrank = (1 - d) / npages
            for node in wcorpus.graph:
                if page in wcorpus.graph[node]:
                    newrank = newrank + d * (ranks[node] / len(wcorpus.graph[node]))
            newranks[page] = newrank
        ranks = newranks
    wcorpus.ranks = ranks

    


