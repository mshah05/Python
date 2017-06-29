import twitter
from twython import TwythonStreamer
from collections import Counter
import datetime
import time
import string 
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment
import json
from prettytable import PrettyTable

def removeUnicode(text):
	asciiText = ""
	for char in text:
		if(ord(char) < 128):
			asciiText = asciiText + char
			
	return asciiText
	
CONSUMER_KEY = 'your consumer key'
CONSUMER_SECRET = 'your consumer secret'
OAUTH_TOKEN = 'your access token'
OAUTH_TOKEN_SECRET = 'your access token secret'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

tw = twitter.Twitter(auth=auth)

#SEARCH
gmrPycon = tw.search.tweets(q="@pepsi", count=25) 
for status in gmrPycon['statuses']:
	text = removeUnicode(status['text']) 
	print 'Text: ', text #text
	print 'Retweets count: ' , status['retweet_count'] #retweet count
	print 'Likes: ', status['favorite_count'] #likes
	sentiment = vaderSentiment(status['text'].encode('utf-8'))
	print 'Compound Sentiment: ', sentiment['compound'] #sentiment analysis of tweet
	words = []
	for word in text.split():
		words.append(word)
	#print 'Words: ', words
	wordCount = Counter(words)
	pt = PrettyTable(field_names=['Word', 'Count'])
	sortedCount = sorted(wordCount.items(), key=lambda pair: pair[1], reverse=True)
	for kv in sortedCount:
		pt.add_row(kv)	
	print 'Pretty Table with frequency count: ' #frequency count
	print pt
	print 'Lexical Diversity: ', round((1.0*len(set(words))/len(words)), 2) #lexical analysis
	print ("\n")
