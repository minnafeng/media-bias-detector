"""Performs sentiment analysis on news articles using TextBlob."""

from textblob import TextBlob


def find_sentiment(news_story):
    """Given a news summary, extracts polarity and subjectivity metrics, returning both in a readable format."""

    news = TextBlob(news_story)

    # Iterates over each sentence in the news, extracts the sentiment, and stores each inside of a list.
    polarity_data = []  # ranges from -1 to 1
    subjectivity_data = []  # ranges from 0 to 1
    for sentence in news.sentences:
        sentiment = sentence.sentiment # tuple of two values (polarity, subjectivity)
        polarity_data.append(sentiment[0])
        subjectivity_data.append(sentiment[1])

    # The averages of both sentiment lists are calculated.
    polarity_average = calculate_average(polarity_data)
    subjectivity_average = calculate_average(subjectivity_data)

    # Displays the sentiment that relates to the averages on the console.
    print()
    print("FINAL ANALYSIS")
    print("----------------------------------")
    print("Polarity: " + calculate_sentiment(polarity_average, "polarity"))
    print("Subjectivity: " + calculate_sentiment(subjectivity_average, "subjectivity"))


# Helper Methods (for the find_sentiment method)
# -------------------------------------------------------------


def calculate_average(list):
    """Calculates the average of a list of numbers."""
    return sum(list) / len(list)


def calculate_sentiment(sentiment, type):
    """Given an average polarity or subjectivity, uses intervals to calculate accurate sentiments.
    Polarity and Subjectivity in TextBlob fall in between -1 and 1, this method bases its intervals off of that.
    """
    sentiment_category = ""
    if type == "polarity":
        if sentiment > 0.75:
            sentiment_category = "Extremely positive."
        elif sentiment > 0.5:
            sentiment_category = "Significantly positive."
        elif sentiment > 0.3:
            sentiment_category = "Fairly positive."
        elif sentiment > 0.1:
            sentiment_category = "Slightly positive."
        elif sentiment < -0.1:
            sentiment_category = "Slightly negative."
        elif sentiment < -0.3:
            sentiment_category = "Fairly negative."
        elif sentiment < -0.5:
            sentiment_category = "Significantly negative."
        elif sentiment < -0.75:
            sentiment_category = "Extremely negative."
        else:
            sentiment_category = "Neutral."
        return sentiment_category
    elif type == "subjectivity":
        if sentiment > 0.75:
            sentiment_category = "Extremely subjective."
        elif sentiment > 0.5:
            sentiment_category = "Fairly subjective."
        elif sentiment > 0.3:
            sentiment_category = "Fairly objective."
        elif sentiment > 0.1:
            sentiment_category = "Extremely objective."
        return sentiment_category
    else:
        print("Invalid Input.")
