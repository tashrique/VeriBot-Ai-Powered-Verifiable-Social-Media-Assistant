"""
Configuration module for VeriBot.
Handles loading environment variables and setting up global configurations.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Twitter API credentials
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
if not TWITTER_BEARER_TOKEN:
    raise ValueError("❌ ERROR: Bearer Token is missing! Check .env file.")

# Gemini API credentials
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("❌ ERROR: Gemini API Key is missing! Check .env file.")

# Constants
MAX_TWEET_LENGTH = 280
RETRY_ATTEMPTS = 3
RETRY_DELAY = 5

# Paths
MOCK_TWEETS_PATH = "mock_tweets.json"
MOCK_REPLIES_LOG = "mock_replies.log" 