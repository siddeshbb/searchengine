import urllib

def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""
page = get_page( "http://www.google.com" )
print page
