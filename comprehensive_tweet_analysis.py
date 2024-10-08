# -*- coding: utf-8 -*-

#import libraries
import pandas as pd
from textblob import TextBlob

df = pd.read_excel("your_data.xlsx")
df.columns
df.head(4)

# Identify the polarity of tweets and further classify them in positive negative and neutral tweets
df["Tweet_body"]= df[' text'].str.split()
df["Tweet_body"]= df["Tweet_body"].astype(str)
df["Word_Count"] = df["Tweet_body"].str.len()
def getPolarity(statement):
    return TextBlob(statement).sentiment.polarity

df["Polarity"] = df["Tweet_body"].apply(getPolarity)

#Positive,Negative and Neutral
def get_score(value):
  if value > 0:
    return "Postive"
  elif value < 0:
    return "Negative"
  else:
    return "Neutral"

df["Polarity_score"] = df["Polarity"].apply(get_score)
df.head()

#Identify the top five most frequently used words
df["text_new"] = df[' text'].str.lower().str.replace('[^\w\s]','')
new_df = df["text_new"].str.split(expand=True).stack().value_counts()
new_df.columns = ['Word', 'Frequency']
new_df

#Identify the top five retweeted tweets
tweet_id_and_rt = df[["TweetID"," RetweetCount"]]
tweet_id_and_rt.sort_values(by=' RetweetCount',ascending=False).nlargest(5,' RetweetCount')

#Create subjectivity vs polarity graph
import seaborn as sns
import matplotlib.pyplot as plt
def getSubjectivity(statement):
    return TextBlob(statement).sentiment.subjectivity

df["Subjectivity"] = df["Tweet_body"].apply(getSubjectivity)

def getPolarity(statement):
    return TextBlob(statement).sentiment.polarity

df["Polarity"] = df["Tweet_body"].apply(getPolarity)

ax, fig = plt.subplots(figsize=(15,10))
ax= sns.lineplot(data=df,x="Subjectivity",y="Polarity",hue="Polarity_score",style="Polarity_score",color="green")
plt.title("Polarity vs Subjectivity of Tweets")
plt.show()
