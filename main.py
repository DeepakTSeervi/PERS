import os
import re
# trying to import few modules
# if not found, then they are installed using pip
try:
    import requests
except:
    os.system('pip install requests')

try:
    from bs4 import BeautifulSoup
except:
    os.system('pip install bs4')

try:
    from googlesearch import search
except:
    os.system('pip install google')

def scrap_stackoverflow(url):
    # search for answer section in a particular id of a tag
    page = requests.get(url, headers=headers, timeout=3)
    soup = BeautifulSoup(page.content, 'html.parser')
    upvote = soup.find(attrs={'class': 'votecell post-layout--left'}).get_text()
    answer = soup.find(attrs ={'class': 'answercell post-layout--right'}).get_text()
    return upvote, answer

os.system('python3 script.py 2> ./FileResults/error_file')
fileHandle = open( './FileResults/error_file',"r" )
lineList = fileHandle.readlines()
fileHandle.close()
if len(lineList) == 0:
    exit(0)

query = lineList[-1]
# to be given by the user
headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0"}

answers = []
for url in search(query, tld='com', num=10, stop=5, pause=3):
    if re.search(r'(.*)https://stackoverflow.com/(.*)', url):
        # all the answers are stored in answers list
        answers.append(scrap_stackoverflow(url))
else:
    print("Sorry! \nWe didn't find answers for your problem")

for u,a in answers:
    print('upvotes: ', u)
    print('answer: ', a)
