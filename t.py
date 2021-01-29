import streamlit as st
import tweepy
import matplotlib.pyplot as plt
from  textblob import TextBlob 
import time
import pandas as pd
import numpy as np
st.title("Project : Twiiter sentiment analysis")
st.sidebar.header('Enter the search keyword')

consumer_key="fR1Y9FZEUeLmk1FIl00Wo4pRb"
consumer_secret="g3isqAlSJs6N2yjv6MEZh6n7NMJ6yKkxwroLw0VHyziOeQXGcU"

access_token="584670834-SU1umK1Ib4Vye5plwTvTNHVwa0cZcYhvUAyqGMnM"
access_token_secret="Hdij0oO1pMEvh9yOAuL7rIpoWj4eysYAiKby9IkcKJ9Xo"

dir(tweepy)
# connected to jump server of twitter
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api_connect=tweepy.API(auth)

# search any topic on twitter
tweet_data=api_connect.search(st.sidebar.text_input('search word'),count=st.sidebar.slider('No of tweets to be analysed', 1, 40, 1 ))

pos=0
neg=0
neu=0
c=0

for tweet in tweet_data:
   #print(tweet.text)
   analysis=TextBlob(tweet.text) # here it will apply NLP\
   #print(analysis.sentiment)
   # now checking polarity only
   st.text(tweet.text)
   c=c+1
   print(c)
   if analysis.sentiment.polarity > 0:
      print("positive")
      pos=pos+1
   elif analysis.sentiment.polarity == 0 :
      print("Neutral")
      neu=neu+1
   else :
      print("Negative")
      neg=neg+1
      
# ploting graphs
plt.xlabel("tags")
plt.ylabel("polarity")
#plt.bar(['pos','neg','neu'],[pos,neg,neu])
#plt.pie([pos,neg,neu],labels=['pos','neg','neu'],autopct="%1.1f%%")
#plt.show()
#chart_data = tweet_data(columns=[pos,neg,neu])
lis=[pos,neu,neg]
print(lis)
#st.line_chart(chart_data)
# If the authentication was successful, you should
# see the name of the account print out
api = tweepy.API(auth)
print(api.me().name)
st.text(api.me().name)

chart_data = pd.DataFrame(lis)
st.bar_chart(chart_data)
st.sidebar.markdown("""# Group memebers:
1 Yash

2 sarthak

3 Shubham

4 Saumya """)


