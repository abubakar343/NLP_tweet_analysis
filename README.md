# Sentiment Analysis of Tweets

This project focuses on performing sentiment analysis on a dataset of tweets using the TextBlob library. The code processes the tweet data, calculates polarity and subjectivity scores, and categorizes the sentiments as Positive, Negative, or Neutral.

## Features

- **Data Import**: The script allows users to upload an Excel file containing tweet data.
- **Data Preprocessing**: The script preprocesses the text data by splitting text into words and converting it to string format.
- **Sentiment Analysis**: 
  - **Polarity Calculation**: Determines the polarity of each tweet, indicating how positive or negative the text is.
  - **Subjectivity Calculation**: Measures the subjectivity of each tweet, indicating how subjective or objective the text is.
- **Sentiment Categorization**: Based on the polarity score, the script categorizes the sentiment of each tweet as Positive, Negative, or Neutral.
- **Export Results**: The processed data, including sentiment scores and categories, are exported to a new Excel file.

## Installation

1. Ensure you have Python installed on your system.
2. Install the required libraries by running:
   ```bash
   pip install pandas numpy matplotlib textblob
   ```
3. If you are using Google Colab, the `google.colab` library will be available by default.

## Usage

1. **Upload Data**: The script is designed to be run in Google Colab, where you can upload your Excel file containing the tweets using the file upload interface.
2. **Run the Script**: Execute the script in your environment. The code will process the data, calculate sentiment scores, and export the results to a new Excel file.

## Dependencies

- `pandas`: For data manipulation and analysis.
- `numpy`: For numerical operations.
- `matplotlib`: For plotting data (if needed).
- `textblob`: For performing sentiment analysis on the text data.
- `google.colab`: To handle file uploads within Google Colab.

## Notes

- The code was developed and tested in a Google Colab environment.
- Ensure your dataset is in the correct format, with the text data stored in a column named `text` and numerical data like `RetweetCount`, `Reach`, and `Likes` appropriately labeled.
  
## Acknowledgments

This project uses the [TextBlob](https://textblob.readthedocs.io/en/dev/) library for sentiment analysis. The code structure and approach were inspired by common practices in sentiment analysis and data processing.
