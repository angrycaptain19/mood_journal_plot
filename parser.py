import re
from textblob import TextBlob
from time_service import TimeService


def get_tweets(statuses):
    return [
        dict(
            text=status.full_text,
            created_at=status.created_at.strftime("%-m/%-d/%Y"),
        )
        for status in statuses
    ]


def remove_twitter_url(tweet):
    return re.sub("(?P<url>https?://[^\s]+)", '', tweet)


def get_date_dictionary(tweets):
    date_dictionary = {}

    for tweet in tweets:
        tweet_date = tweet["created_at"]
        tweet_timestamp = TimeService().get_timestamp(tweet_date)
        tweet_content = remove_twitter_url(tweet["text"])

        if tweet_date in date_dictionary:
            date_dictionary[tweet_timestamp] += ' ' + tweet_content
        else:
            date_dictionary[tweet_timestamp] = tweet_content

    print(date_dictionary)
    return date_dictionary


def get_mood_dictionary(date_dictionary):
    mood_dictionary = {}

    for date in date_dictionary:
        english_time = TimeService().get_string_from_timestamp(date)
        print('------' + english_time)
        print(TextBlob(date_dictionary[date]))
        print(TextBlob(date_dictionary[date]).sentiment.polarity)
        print('-----------')
        mood_dictionary[date] = TextBlob(date_dictionary[date]).sentiment.polarity

    return mood_dictionary
