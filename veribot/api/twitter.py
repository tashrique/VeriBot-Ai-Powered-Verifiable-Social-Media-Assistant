"""
Twitter API module for VeriBot.
Handles interactions with the Twitter API.
"""

import json
import time
import tweepy
from datetime import datetime
from veribot.config import TWITTER_BEARER_TOKEN, MOCK_TWEETS_PATH, MOCK_REPLIES_LOG, RETRY_ATTEMPTS, RETRY_DELAY

# Authenticate using OAuth 2.0 (App-Only authentication)
client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

def fetch_tweets_with_retry(query, count=5, retries=RETRY_ATTEMPTS, delay=RETRY_DELAY):
    """
    Fetch tweets with built-in rate-limit handling.
    
    Args:
        query (str): The search query
        count (int): Number of tweets to fetch
        retries (int): Number of retry attempts
        delay (int): Initial delay between retries in seconds
        
    Returns:
        list: List of tweet dictionaries
    """
    attempt = 0
    while attempt < retries:
        try:
            tweets = client.search_tweets(q=query, count=count, tweet_mode="extended")
            return [{"id": tweet.id, "text": tweet.full_text, "author": tweet.user.screen_name} for tweet in tweets]
        except tweepy.TooManyRequests:
            print(f"Rate limit hit! Retrying in {delay} seconds...")
            time.sleep(delay)
            delay *= 2  # Exponential backoff
            attempt += 1
        except Exception as e:
            print(f"❌ ERROR: {e}")
            break
    return []

def fetch_tweets(keyword, count=1, use_mock=False):
    """
    Fetch recent tweets containing the given keyword.
    Use mock data if 'use_mock' is true
    
    Args:
        keyword (str): Keyword to search for
        count (int): Number of tweets to fetch
        use_mock (bool): Whether to use mock data
        
    Returns:
        list: List of tweet dictionaries
    """
    if use_mock:
        print("Using mock data...")
        return load_mock_tweets(count)
    try:
        tweets = client.search_recent_tweets(
            query=keyword, max_results=count, tweet_fields=["created_at", "author_id"])

        if tweets.data:
            return [
                {"id": tweet.id, "text": tweet.text,
                    "author": tweet.author_id}
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
    
    Args:
        count (int): Number of mock tweets to load
        
    Returns:
        list: List of mock tweet dictionaries
    """
    with open(MOCK_TWEETS_PATH, "r") as f:
        tweets = json.load(f)[:count]
    return tweets

def post_tweet_reply(tweet_id, username, reply_text, use_mock=True):
    """
    Post a reply to a tweet.
    
    Args:
        tweet_id (str): ID of the tweet to reply to
        username (str): Username of the tweet author
        reply_text (str): Text of the reply
        use_mock (bool): Whether to use mock posting
        
    Returns:
        bool: True if successful, False otherwise
    """
    reply_text = f"@{username} {reply_text}"
    attempt = 0
    max_attempts = 3

    if use_mock:
        print(f"✅ Successfully mock posted reply to {username}: {reply_text}")
        with open(MOCK_REPLIES_LOG, "a") as f:
            f.write(f"{datetime.now()}: {reply_text}\n")
        return True
    
    while attempt < max_attempts:
        try:
            client.create_tweet(in_reply_to_tweet_id=tweet_id, text=reply_text)
            print(f"✅ Successfully posted reply to {username}: {reply_text}")
            return True
        except Exception as e:
            print(f"❌ ERROR: {e}")
            attempt += 1
            time.sleep(2 ** attempt)
    print(f"❌ FAILED to post reply to {username}: {reply_text} after {max_attempts} attempts")
    return False 