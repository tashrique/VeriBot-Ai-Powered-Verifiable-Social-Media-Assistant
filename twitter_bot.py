import os
import tweepy
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API credentials
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
if not BEARER_TOKEN:
    raise ValueError("❌ ERROR: Bearer Token is missing! Check .env file.")

# Authenticate using OAuth 2.0 (App-Only authentication)
client = tweepy.Client(bearer_token=BEARER_TOKEN)


def fetch_tweets(keyword, count=1, use_mock=False):
    """
    Fetch recent tweets containing the given keyword.
    Use mock data if 'use_mock' is true
    """
    if use_mock:
        print("Using mock data...")
        return load_mock_tweets(count)
    try:
        tweets = client.search_recent_tweets(
            query=keyword, max_results=count, tweet_fields=["created_at", "author_id"])

        if tweets.data:
            return [
                {"id": tweet.id, "text": tweet.text_content,
                    "author_id": tweet.author_id}
                for tweet in tweets.data
            ]
        else:
            print("No tweets found.")
            return []
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return []


def load_mock_tweets(count):
    """
    Load mock tweets for testing purposes.
    """
    with open("mock_tweets.json", "r") as f:
        tweets = json.load(f)[:count]
    return tweets


if __name__ == "__main__":
    tweets = fetch_tweets("Flare Blockchain", 2, use_mock=True)
    for tweet in tweets:
        print(tweet)
