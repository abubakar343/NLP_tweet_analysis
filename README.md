# Sentiment Analysis of Tweets

This project contains two scripts that focus on performing sentiment analysis on a dataset of tweets using the TextBlob library. Both scripts process tweet data, calculate polarity and subjectivity scores, and categorize sentiments as Positive, Negative, or Neutral.

## Features

### 1. Basic Tweet Analysis (`main.py`)

- **Data Import**: Allows users to upload an Excel file containing tweet data.
- **Data Preprocessing**: Preprocesses the text data by splitting it into words and converting it to string format.
- **Sentiment Analysis**:
  - **Polarity Calculation**: Determines the polarity of each tweet, indicating how positive or negative the text is.
  - **Subjectivity Calculation**: Measures the subjectivity of each tweet, indicating how subjective or objective the text is.
- **Sentiment Categorization**: Categorizes the sentiment of each tweet as Positive, Negative, or Neutral based on the polarity score.
- **Export Results**: Exports the processed data, including sentiment scores and categories, to a new Excel file.

### 2. Comprehensive Tweet Analysis (`comprehensive_tweet_analysis.py`)

- **Polarity and Subjectivity Calculation**: Like `main.py`, this script calculates the polarity and subjectivity of tweets.
- **Sentiment Categorization**: Classifies tweets into Positive, Negative, or Neutral categories.
- **Word Frequency Analysis**: Identifies the top five most frequently used words in the tweet dataset.
- **Top Retweeted Tweets**: Identifies the top five most retweeted tweets in the dataset.
- **Polarity vs. Subjectivity Visualization**: Creates a graph to visualize the relationship between polarity and subjectivity of tweets.

## Installation

1. Ensure you have Python installed on your system.
2. Install the required libraries by running:
   ```bash
   pip install pandas numpy matplotlib textblob seaborn
   ```
3. If you are using Google Colab, the `google.colab` library will be available by default.

## Usage

1. **Upload Data**: The scripts are designed to be run in Google Colab, where you can upload your Excel file containing the tweets using the file upload interface.
2. **Run the Script**: Execute either script in your environment. The code will process the data, calculate sentiment scores, and export the results to a new Excel file.

## Dependencies

- `pandas`: For data manipulation and analysis.
- `numpy`: For numerical operations.
- `matplotlib`: For plotting data.
- `seaborn`: For advanced visualizations.
- `textblob`: For performing sentiment analysis on the text data.
- `google.colab`: To handle file uploads within Google Colab.

## Notes

- The code was developed and tested in a Google Colab environment.
- Ensure your dataset is in the correct format, with the text data stored in a column named `text` and numerical data like `RetweetCount`, `Reach`, and `Likes` appropriately labeled.

## Acknowledgments

This project uses the [TextBlob](https://textblob.readthedocs.io/en/dev/) library for sentiment analysis. The code structure and approach were inspired by common practices in sentiment analysis and data processing.
