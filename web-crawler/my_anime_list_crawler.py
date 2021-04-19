# my_anime_list_crawler.py
# by Jonathan M.
# Date: April 15, 2021
# Description: One of my first web crawler. Will take take top 50 animes by popularity 
#   from myanimelist.net and export it to csv file.
# BeautifulSoup documents: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# URL: https://myanimelist.net/topanime.php?type=bypopularity

# Imports:
import requests
from bs4 import BeautifulSoup
import csv
import re

URL = 'https://myanimelist.net/topanime.php?type=bypopularity'
page = requests.get(URL)

# Create a Beautiful Soup object. Will take HTML content from page as a input. 
# You must also tell it which parser to use. In this example it is 'html.parser'.
soup = BeautifulSoup(page.content,'html.parser')

# Use '.prettify() to format the results to make reading easier.
soup.prettify()

# Variable holders:

list_title = soup.find('title').text.strip()
headerss = soup.find(class_='table-header').get_text(separator = ',')
title = []
episodes = []
details = []
original_release = []
member_count = []
score = []
rows = []

# We only need the information inside tags with class = 'ranking-list'
anime = soup.find_all(class_ = 'ranking-list')
# here
for anime in anime:
    title.append(anime.find('h3', class_= 'anime_ranking_h3').text.strip())
    # Since this tag contain more than piece of information we will remove and separate the text.
    #   using ".get_text(separator = ',', strip=True)".
    # ".get_text()" will only return text inside the tags.
    # "seperator = ',' " will add a seperator between the text. Here the seperator is a ','.
    # "strip = True" will strip whitespace from the beggining and end of each text.
    # Since the member number contain commas we might have to deal with the later but for now we will 
    #   leave it as it is.
    details.append(anime.find('div', class_= 'information').get_text(separator = ',', strip=True))
    score.append(anime.find('div', class_= 'js-top-ranking-score-col').get_text())

# The following will separate the anime details into episodes, original release dates, and number of members.
for x in range(len(details)):
    # Below we are spliting the details with '.split(',', 2)
    # The separator is ',' and the maxsplit is 2 since we only have 3 different details.
    # This also stops the split from spliting the member count since the numbers have commas.
    temp = details[x].split(',', 2)
    episodes.append(temp[0])
    original_release.append(temp[1])
    member_count.append(temp[2])

# Now we must remove any of the extra text. Using RegEx we remove anything that is not a number.
for x in range(len(episodes)):
    episodes[x] = re.sub('[^0-9]', '', episodes[x])
    member_count[x] = re.sub('[^0-9]', '', member_count[x])



# Now we create a header list:
headers = ['Rank', 'Title', 'Episodes', 'Original Release', 'Member Count', 'Score']


# Setting up rows:
for x in range(len(title)):
    rows.append([x,title[x],episodes[x],original_release[x],member_count[x],score[x]])

# Now to write to csv file
filename = 'top_50_anime.csv'

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(headers)
    csvwriter.writerows(rows)


