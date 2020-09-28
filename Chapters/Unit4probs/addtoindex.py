# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

def add_to_index(index,keyword,url):
    l = len( index )
    keylist = []
    urllist = []
    if l == 0:
        urllist.append( url )
        keylist.append( keyword )
        keylist.append( urllist )
        index.append( keylist )
    else:
        i = 0
        while i < l:
            if index[i][0] == keyword:
                index[i][1].append( url )
                break
            i = i + 1
        if i == l:
            urllist.append( url )
            keylist.append( keyword )
            keylist.append( urllist )
            index.append( keylist )
        






add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]


