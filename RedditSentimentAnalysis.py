import numpy as np
import pandas as pd
import praw
import matplotlib.pyplot as plt
from textblob import TextBlob
from TwitterSentimentFunct import remove_all_values

#Authentical with OAuth and Reddit API
reddit = praw.Reddit(client_id='Your_Reddit_Personal_Script',
                     client_secret='Your_Reddit_Secret',
                     user_agent='Your_Reddit_App_Name',
                     username='Your_Reddit_Username',
                     password='Your_Reddit_Password')                   

#Get user input for Sentiment analysis text
keyword = input("Enter keyword for subreddit: ")

subreddit = reddit.subreddit(keyword) 

top_subreddit = subreddit.top(limit=1000)

polarity = []
subjectivity = []

for submission in top_subreddit:
    print(submission.selftext)
    analysis = TextBlob(submission.selftext)

    #Create list of polarity & subjectivity for mean
    polarity.append(analysis.sentiment.polarity)
    subjectivity.append(analysis.sentiment.subjectivity) 

#Remove 0.0 (neutral) polarity & subjectivity
polarity = remove_all_values(polarity, 0.0) 
subjectivity = remove_all_values(subjectivity, 0.0) 

#Output
print("Sentiment average Polarity: " + str(np.mean(polarity)))
print("Sentiment average Subjectivity: " + str(np.mean(subjectivity)))

#Generate histograms
polarityDf = pd.DataFrame(polarity, columns=["Polarity"])
subjectivityDf = pd.DataFrame(subjectivity, columns=["Subjectivity"])

showHistograms = input("Show Historgrams? Y or N ")

if(showHistograms.lower() == ("y" or "yes")):
    polarityDf.hist(color="blue")
    subjectivityDf.hist(color= "orange")
    plt.show()  
else:
    exit()