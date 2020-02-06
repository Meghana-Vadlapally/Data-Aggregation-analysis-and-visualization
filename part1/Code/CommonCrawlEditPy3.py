import requests
from bs4 import BeautifulSoup
import sys

records=[]

i=0
with open('commonCrawlFilteredUrls.txt') as file: #cc_url2.txt
    for line in file:
        content = ""
        try:
            r = requests.get(line)
        except:
            pass
        soup = BeautifulSoup(r.text, 'html.parser')
        results = soup.findAll('p')
        for i in range(0,len(results)):
            content+=results[i].text
        records.append(content)

with open("commonCrawlData.txt", "w",encoding='utf-8') as myfile:
       for i in records:
            myfile.write('\n'+i)

