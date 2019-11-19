import requests
from bs4 import BeautifulSoup
import os
from googlesearch import search
import re

def scrap_stackoverflow(url):
    # search for answer section in a particular section
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
#   temp =soup.find('p', attrs={'class': r'answer-*'}).get_text()
    upvote = soup.find(attrs={'class': 'votecell post-layout--left'}).get_text()
    answer = soup.find(attrs ={'class': 'answercell post-layout--right'}).get_text()
    return upvote, answer
    # print(answers)

os.system('python3 ' + input('Enter the name of the file: ') + ' 2> ./FileResults/error_file')
fileHandle = open( './FileResults/error_file',"r" )
lineList = fileHandle.readlines()
fileHandle.close()
if len(lineList) == 0:
    exit(0)

query = lineList[-1]
# to be given by the user
headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0"}

results_for_the_search = search(query, tld='com', num=10, stop=5, pause=2)
print(list(results_for_the_search))
answers = list()
for url in results_for_the_search:
    if re.search(r'(.*)https://stackoverflow.com/(.*)', url):
        # all the answers are stored in answers list
        answers.append(scrap_stackoverflow(url))
    else:
        # not able to scrape these sites
        print('some other site which is not available')

for u,a in answers:
    print('upvotes: ', u)
    print('answer: ', a)
