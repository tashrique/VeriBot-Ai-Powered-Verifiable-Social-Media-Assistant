"""
Logger module for VeriBot.
Provides consistent logging functionality.
"""

import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("veribot.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("veribot")

def log_tweet(tweet):
    """
    Log a tweet.
    
    Args:
        tweet (dict): The tweet to log
    """
    logger.info(f"📝 Tweet: {tweet['text']}")

def log_classification(category):
    """
    Log a tweet classification.
    
    Args:
        category (str): The category of the tweet
    """
    logger.info(f"🔍 Classified as: {category}")

def log_response(response):
    """
    Log an AI response.
    
    Args:
        response (str): The AI-generated response
    """
    logger.info(f"🤖 AI Response: {response}")

def log_safety_check(result):
    """
    Log a safety check result.
    
    Args:
        result (str): The safety check result
    """
    logger.info(f"🚨 Safety Check: {result}")

def log_reply(username, reply_text):
    """
    Log a tweet reply.
    
    Args:
        username (str): The username of the tweet author
        reply_text (str): The text of the reply
    """
    logger.info(f"✅ Reply to {username}: {reply_text}")

def log_error(error):
    """
    Log an error.
    
    Args:
        error (Exception): The error to log
    """
    logger.error(f"❌ ERROR: {error}")

def log_separator():
    """
    Log a separator line.
    """
    logger.info("-" * 50) 