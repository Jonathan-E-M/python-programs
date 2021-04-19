# insomniac_crawler.py
# by Jonathan M.
# Date: April 14, 2021
# Description: My first web crawler.
# URL data: https://www.insomniac.com/events/festivals/
# BeautifulSoup documents: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Imports:
import requests
from bs4 import BeautifulSoup

URL = 'https://www.insomniac.com/events/festivals/'
page = requests.get(URL)

# Create a Beautiful Soup object. Will take HTML content from page as a input. 
# You must also tell it which parser to use. In this example it is 'html.parser'.
soup = BeautifulSoup(page.content,'html.parser')

# Use '.prettify() to format the results to make reading easier.
soup.prettify()

# We will use the tag title but most other tags can be used.
# The following will return the first tag you choose:
print(soup.title).strip() # Here '.strip()' will remove whitespace
print(soup.a)
print(soup.p)

# The Following will return title tag name:
print(soup.title.name)

# The following will return just the text inside the title tag.
print(soup.title.string)

# The following will return the parent tag:
print(soup.title.parent.name)

# The following will find and return the first instance:
#   Below we use 'class_' to find by class name.
print(soup.find(class_= "card__detail"))
#   Below we search for tag 'a':
print(soup.find('a'))


# The following will find and return all instances:
#   Below we use 'class_' to find by class name.
print(soup.find_all(class_= "card__detail"))
#   Below we search for tag 'a': commented because will print all a tags
#print(soup.find_all('a'))

# The following will  find and return the first instance of
# a class in the given tag:
print(soup.find('div', class_ = "card__detail"))

# The following will extract all URLS found withing the page:
for link in soup.find_all('a'):
    print(link.get('href'))

# The following will return all the text from the page
print(soup.get_text())







#print(soup.p['class'])

# To find a specific item inside. you 
festival_title = soup.find_all('div', class_="card__detail")
results= soup.find(class_= "card__title")

#print(results)

def export_to_txt():
    f = open("data.txt", "a")
    f.write(str(soup.prettify()))
    f.close


#print(results)