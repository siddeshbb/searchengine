Python 2.7.5 (default, May 15 2013, 22:44:16) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def crazy(a, b, c):
	return not type(a) == type(b) and type(b) == type(b+c)

>>> 'abc' + 2

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    'abc' + 2
TypeError: cannot concatenate 'str' and 'int' objects
>>> type(2 + '3')

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    type(2 + '3')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> [] + '2'

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    [] + '2'
TypeError: can only concatenate list (not "str") to list
>>> crazy([], 2, [])

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    crazy([], 2, [])
  File "<pyshell#2>", line 2, in crazy
    return not type(a) == type(b) and type(b) == type(b+c)
TypeError: unsupported operand type(s) for +: 'int' and 'list'
>>> crazy(2, [], [])
True
>>> def crazy(a, b, c):
	return not type(a) == type(b) and type(a) == type(b+c)

>>> crazy(2, [] [])
SyntaxError: invalid syntax
>>> crazy(2, [], [])
False
>>> crazy(2.0, 0, 2.0)
True
>>> help(assert)
SyntaxError: invalid syntax
>>> help()

Welcome to Python 2.7!  This is the online help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/2.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

help> asert
no Python documentation found for 'asert'

help> assert
The ``assert`` statement
************************

Assert statements are a convenient way to insert debugging assertions
into a program:

   assert_stmt ::= "assert" expression ["," expression]

The simple form, ``assert expression``, is equivalent to

   if __debug__:
      if not expression: raise AssertionError

The extended form, ``assert expression1, expression2``, is equivalent
to

   if __debug__:
      if not expression1: raise AssertionError(expression2)

These equivalences assume that ``__debug__`` and ``AssertionError``
refer to the built-in variables with those names.  In the current
implementation, the built-in variable ``__debug__`` is ``True`` under
normal circumstances, ``False`` when optimization is requested
(command line option -O).  The current code generator emits no code
for an assert statement when optimization is requested at compile
time.  Note that it is unnecessary to include the source code for the
expression that failed in the error message; it will be displayed as
part of the stack trace.

Assignments to ``__debug__`` are illegal.  The value for the built-in
variable is determined when the interpreter starts.

help> q

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> def real_get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""

cache = {
   'http://udacity.com/cs101x/urank/index.html': """<html>
<body>
<h1>Dave's Cooking Algorithms</h1>
<p>
Here are my favorite recipies:
<ul>
<li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
<li> <a href="http://udacity.com/cs101x/urank/arsenic.html">World's Best Hummus</a>
<li> <a href="http://udacity.com/cs101x/urank/kathleen.html">Kathleen's Hummus Recipe</a>
</ul>

For more expert opinions, check out the 
<a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a> 
and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/zinc.html': """<html>
<body>
<h1>The Zinc Chef</h1>
<p>
I learned everything I know from 
<a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
</p>
<p>
For great hummus, try 
<a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.

</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/nickel.html': """<html>
<body>
<h1>The Nickel Chef</h1>
<p>
This is the
<a href="http://udacity.com/cs101x/urank/kathleen.html">
best Hummus recipe!
</a>

</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/kathleen.html': """<html>
<body>
<h1>
Kathleen's Hummus Recipe
</h1>
<p>

<ol>
<li> Open a can of garbonzo beans.
<li> Crush them in a blender.
<li> Add 3 tablesppons of tahini sauce.
<li> Squeeze in one lemon.
<li> Add salt, pepper, and buttercream frosting to taste.
</ol>

</body>
</html>

""", 
   'http://udacity.com/cs101x/urank/arsenic.html': """<html>
<body>
<h1>
The Arsenic Chef's World Famous Hummus Recipe
</h1>
<p>

<ol>
<li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>.
<li> Force her to make hummus for you.
</ol>

</body>
</html>

""", 
   'http://udacity.com/cs101x/urank/hummus.html': """<html>
<body>
<h1>
Hummus Recipe
</h1>
<p>

<ol>
<li> Go to the store and buy a container of hummus.
<li> Open it.
</ol>

</body>
</html>




""", 
}

def get_page(url):
    if url in cache:
        return cache[url]
    else:
        print "Page not in cache: " + url
        return None
    
def make_cache(seed):
    from uoogle import add_page_to_index

    tocrawl = [seed]
    crawled = []
    graph = {seed: []}
    index = {}
    print "cache = {"
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            ## print "Crawing: " + page
            content = real_get_page(page)
            print "   '" + page + "'" + ': """' + content + '""", '
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            for link in outlinks:
                if link in graph: # already found one link to it
                    graph[link].append(page)
                else:
                    graph[link] = [page]
            union(tocrawl, outlinks)
            crawled.append(page)
    print "}"


    
