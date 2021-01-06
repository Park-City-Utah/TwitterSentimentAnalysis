import tweepy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

#Authentical with tweepy OAuth and Twitter API
apiKey= 'CONSUMER_KEY_HERE'
apiSecret= 'CONSUMER_SECRET_HERE'
accessToken='ACCESS_TOKEN_HERE'
accessTokenSecret='ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(apiKey, apiSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

#Pull Tweets on keyword
tweets = api.search('#datadriven',count=1000)

polarity = []
subjectivity = []

#Perform analysis and create lists for manipulation (polarity/subjectivity)
for tweet in tweets:
    analysis = TextBlob(tweet.text)

    #Create list of polarity & subjectivity for mean
    polarity.append(analysis.sentiment.polarity)
    subjectivity.append(analysis.sentiment.subjectivity)  

#Remove 0.0 (nutral) polarity
while(0 in polarity):
    polarity.remove(0.0)

##Remove 0.0 (nutral) polarity
while(0 in subjectivity):
    subjectivity.remove(0.0)

#Generate histogram
polarityDf = pd.DataFrame(polarity, columns=["Polarity"])
subjectivityDf = pd.DataFrame(subjectivity, columns=["Subjectivity"])

polarityDf.hist(color="blue")
subjectivityDf.hist(color= "orange")
plt.show()      