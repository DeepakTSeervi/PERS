import subprocess
from googlesearch import search 
import os


while True:

    try:	

        os.system('python3 '+input('Enter the name of the file: ')+' 2> ./FileResults/error_file')
        break
    except:

        print("Please enter a valid file name ")


def extract_error():
    fileHandle = open( './FileResults/error_file',"r" )
    lineList = fileHandle.readlines()
    fileHandle.close()
    # print(lineList[-1])
    if lineList == []:
        return 0
    return lineList[-1]
    

def sites_info(error_statement):
    
    if error_statement:
        j = search(error_statement, tld="com", num=10, stop=5, pause=2)
        print(x for x in j)
    else:
        print('Your program is running fine!')
        exit

sites_info(extract_error())