# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
frst_quote = page.find('"' , start_link )
second_quote = page.find( '"' , frst_quote+1 )
url = page[ frst_quote+1 : second_quote ]
print (url)

