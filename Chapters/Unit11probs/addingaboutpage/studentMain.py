# This is the file you should make your changes (not server.py)
# Modify this file to make sure that it behaves as asked in the video:
#     if the request is '/about', the server should respond with:
#          'This is my udacious project!'
#     for all other requests, the server should respond with a normal
#     search response.
# 
# Hint: you will need to add two strings to the tuple of inputs for
#    web.application(...) as well as define a new class.
#
# To test your code locally you have to install web.py and all of
# these files locally as well.

from search import lucky_search
from crawler import crawl_web, compute_ranks

corpus, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
ranks = compute_ranks(graph)

class LuckySearch(object):        
    def GET(self, query):
        result = lucky_search(corpus, ranks, query)
        return result

class About(object):
    def GET(self, query):
        return 'This is my udacious project!'
# This will be executed only if you run this code locally
# using a command: python studentMain.py

if __name__ == "__main__":
    import web
    # This should be on one line or it will not be graded correctly.  To solve
    # this problem, you'll need to add two strings to the tuple that is the first
    # input below.
    app = web.application(('/about', 'About', '/(.*)',  'LuckySearch'), globals())
    corpus, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
    app.run()
