# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:20:22 2019

@author: vinee
"""

import pandas as pd
import re
import mysql.connector
import preprocessor as p

from nltk.corpus import stopwords

s = set(stopwords.words('english')) 

#https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/
def clean_tweet(tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())
    
cnx = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='twitter')

if cnx.is_connected():
    print("Connected")
    
query = 'SELECT text FROM twitter.twitter_stream_collect;'

tweetsDf = pd.read_sql(query, con=cnx)
tweetsDf = tweetsDf.drop_duplicates()

for i, row in tweetsDf.iterrows():
    a = p.clean(row[0])
    a = clean_tweet(a)
    tweetsDf.at[i, 'text'] = a

topicsDict = {}
topicsDict['basketball'] = []
topicsDict['golf'] = []
topicsDict['cricket'] = []
topicsDict['football'] = []

def GetTopicWiseTweetsDict(topicName, keyWords, tweetsDf, topicsDict):
    for i, row in tweetsDf.iterrows():
        a = row[0]
        found = False
        for b1 in keyWords:
            found = found or b1 in a
        
        if(found):
            topicsDict[topicName].append(a)


b = ['nba', 'basketball', 'ncaa', 'NCAAChampionship']
GetTopicWiseTweetsDict('basketball', b, tweetsDf, topicsDict)
GetTopicWiseTweetsDict('golf', ['golf', 'pgatour'], tweetsDf, topicsDict)
GetTopicWiseTweetsDict('cricket',['cricket', 'ipl','iplt20'], tweetsDf, topicsDict)
GetTopicWiseTweetsDict('football', ['nfl', 'nfldraft', 'EPL', 'LaLiga', 'premier league', 'bundesliga'], tweetsDf, topicsDict)
    
tweetsDf.to_csv('cleanedtweets.csv', sep='\t', encoding='utf-8')
    

