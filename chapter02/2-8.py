html_doc ="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p >

<p class="story">Once upon a time there were three little sisters;
    and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a > and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a >;
and they lived at the bottom of a well.</p >
<p class="story">...</p >
</body>
</html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(open( 'chapter02/index.html'), features='lxml')

# print(soup.prettify())

title = soup.title

print(title.name)
print(title.attrs)

soup = BeautifulSoup('<p class="semantic ui"></p>')
print(soup.p['class'])

soup = BeautifulSoup('<p class="page">This is a test</p>', features='lxml')
tag = soup.p
print(tag.string)


tag.string.replace_with('This is another test')
print(tag)


print(soup.name)

html_doc1 = "<p><!--This is a comment--></p>"
soup = BeautifulSoup(html_doc1, 'lxml')
comment = soup.p.string
print(comment)
print(type(comment))



soup = BeautifulSoup(html_doc, 'lxml')

tag = soup.body
print(tag)
print('+++++++++++++++++')
print(tag.contents)
print(len(tag.contents))
print(tag.contents[5])

print('+++++++++++')
for ele in tag.children:
    print(ele)
    
    
print('++++++++++++++++')
for string in tag.strings:
    print(string)
    
    
print('++++++++++++++++')
for string in soup.strings:
    print(string)
    
    
title_tag = soup.title
print(title_tag)
print(title_tag.parent)


for parent in title_tag.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
        
print('-----------------')
print(soup.a)  
print(soup.a.next_sibling)
print(soup.a.next_sibling.next_sibling)
print(soup.a.previous_sibling.previous_sibling)


for next in soup.a.next_siblings:
    print(next)
    
    
print(soup.find_all('b'))

import re 
for tag in soup.find_all(re.compile(r"^b")):
    print(tag.name)
    
    
for tag in soup.findAll(["a", "b"]):
    print(tag)
    
    
for tag in soup.find_all(True):
    print(tag.name)
    

def has_class_and_id(tag):
    return tag.has_attr("class") and tag.has_attr("id")

for tag in soup.find_all(has_class_and_id):
    print(tag)
    
    
print(soup.find_all(id="link1"))

print(soup.find_all(href=re.compile(r'elsie')))