#####################################################################################
##### Taken code from tutorial : https://rushter.com/blog/python-fast-html-parser/
#####################################################################################
from bs4 import BeautifulSoup
import warc
import lxml
from time import time
import wget

2


#url = 'https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2019-13/segments/1552912202299.16/warc/CC-MAIN-20190320044358-20190320070358-00417.warc.gz'
url = 'https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2019-13/segments/1552912201922.85/robotstxt/CC-MAIN-20190319073140-20190319095029-00063.warc.gz'
filename = wget.download(url)

urls=[]
docs=[]

def read_doc(record):
    url = record.url
    urls.append(url)
    print(url)
    text = 'start'
    return url, text

def process_warc(file_name, limit=100000):
    warc_file =warc.open(file_name, 'rb')
    t0 = time()
    n_documents = 0
    with open("commonCrawlAllUrls.txt", "a") as myfile:
        for i, record in enumerate(warc_file):
            url, doc = read_doc(record)

            n_documents += 1

            if i > limit:
                break

        warc_file.close()
        print('Parsing took %s seconds and produced %s documents\n' % (time() - t0, n_documents))

file_name = "CC-MAIN-20190319073140-20190319095029-00063.warc.gz"
process_warc(file_name, 100000)

for i in docs:
    i.encode('UTF-8')
    print(i)


len(urls)
urls[0]='start'
keywords=['basketball', 'nba', 'NBA', 'NCAA Championship','NCAA',
             'Tennis','ATP', 'WTA', 'Nadal'
             'golf',  'PGA Tour', 'pgatour', 
             'cricket', 'ipl','IPL', 'iplt20', 
             'UFC',
             'NFL']

with open("commonCrawlFilteredUrls.txt", "a") as myfile:
    for i in urls:
        if any(x in i for x in keywords):
            myfile.write('\n'+i)
