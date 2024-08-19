# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob

# Import files in Google Colab
from google.colab import files
files.upload()  # Upload the Excel file containing your tweets data

# Read the Excel file into a DataFrame
data = pd.read_excel("your_tweets_data.xlsx")
data  # Display the DataFrame

# Display the first 5 rows of the DataFrame
data.head()

# Display the last 5 rows of the DataFrame
data.tail()

# Display information about the DataFrame, including data types and non-null counts
data.info()

# Generate descriptive statistics for numerical columns in the DataFrame
data.describe()

# Display the column names of the DataFrame
data.columns

# Sort the DataFrame by the 'RetweetCount' column in descending order and display the top 5 rows
data.sort_values(by=' RetweetCount', ascending=False).head(5)

# Sort the DataFrame by the 'RetweetCount' column in descending order and display the last 5 rows
data.sort_values(by=' RetweetCount', ascending=False).tail(5)

# Display the shape of the DataFrame (number of rows and columns)
data.shape

# Find the maximum value in the 'Reach' column
data[' Reach'].max()

# Find the maximum value in the 'Likes' column
data[' Likes'].max()

# Sort the DataFrame by the 'RetweetCount' column in ascending order
data.sort_values(by=' RetweetCount')

# Define a function to calculate the polarity of the text
def getPolarity(text):
    return TextBlob(text).sentiment.polarity

# Preprocess the text data: split the text into words and convert to string type
data["Text"] = data[' text'].str.split()
data["Text"] = data["Text"].astype(str)

# Apply the polarity function to the text data and create a new column 'polarity'
data["polarity"] = data["Text"].apply(getPolarity)
data  # Display the updated DataFrame

# Define a function to calculate the subjectivity of the text
def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

# Preprocess the text data again (split and convert to string)
data["Text"] = data[' text'].str.split()
data["Text"] = data["Text"].astype(str)

# Apply the subjectivity function to the text data and create a new column 'subjectivity'
data["subjectivity"] = data["Text"].apply(getSubjectivity)
data  # Display the updated DataFrame

# Re-apply the polarity function to the text data after converting the text to a string format
data["Text"] = data[' text'].to_string()
data["polarity"] = data["Text"].apply(getPolarity)
data  # Display the updated DataFrame

# Select and display specific rows and columns from the DataFrame
data.loc[23:50, ['Text', 'polarity', 'subjectivity']]

# Re-apply the subjectivity function to the text data after converting the text to a string format
data["Text"] = data[' text'].to_string()
data["subjectivity"] = data[' text'].apply(getSubjectivity)
data  # Display the updated DataFrame

# Define a function to categorize the polarity score into 'Positive', 'Negative', or 'Neutral'
def get_score(val):
    if val > 0:
        return 'Positive'
    elif val < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Apply the score categorization function to the 'polarity' column and create a new column 'pol_score'
data['pol_score'] = data['polarity'].apply(get_score)

# Export the updated DataFrame to an Excel file
data.to_excel('Twitter+data+in+sheets.xlsx')

# Generate descriptive statistics for the updated DataFrame
data.describe()
