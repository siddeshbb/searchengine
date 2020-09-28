# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words,`in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.


def remove_tags(content):
    page = content
    page = filter(None,page)
    page = page.replace('\n','')
    start_tag = page.find('<')
    if start_tag == -1:
        return page.split()
    else:
        l = []
        if start_tag > 0:
            cur = page[:start_tag]
            cur = cur.split()
            if len(cur) == 1:
                l.append(cur[0])
            else:
                for x in cur:
                    l.append(x)
        next_tag = 0
        while True:
            start_tag = page.find('<')
            end_tag = page.find('>',start_tag)
            next_tag = page.find('<',end_tag+1)
            if next_tag == -1:
                cur = page[end_tag+1:]
                cur = cur.split()
                if len(cur) == 1:
                    l.append(page[end_tag+1:])
                else:
                    for x in cur:
                        l.append(x)
                break
            else:
                cur = page[end_tag+1:next_tag]
                cur = cur.split()
                if len(cur) == 1:
                    l.append(page[end_tag+1:next_tag])
                else:
                    for x in cur:
                        l.append(x)
                
                
            page = page[end_tag+1:]
        l = filter(None,l)
        for x in range(0,len(l)):
            l[x] = l[x].strip()
        return l
        
        
    


print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']


print remove_tags( 'This is in <i>italics</i>' )
print remove_tags('This <i>line</i> has <em>lots</em> of <b>tags</b>.')
