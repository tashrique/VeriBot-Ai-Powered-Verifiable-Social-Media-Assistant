"""
Main module for VeriBot.
Ties together all components and provides the main entry point.
"""

from veribot.api.twitter import fetch_tweets, post_tweet_reply
from veribot.classification.classifier import classify_tweet
from veribot.ai.responder import generate_ai_response, filter_ai_response
from veribot.utils.logger import (
    log_tweet, log_classification, log_response, 
    log_safety_check, log_reply, log_separator
)

def process_tweets(keyword="Flare Network", count=6, use_mock=True):
    """
    Process tweets matching the given keyword.
    
    Args:
        keyword (str): Keyword to search for
        count (int): Number of tweets to process
        use_mock (bool): Whether to use mock data
        
    Returns:
        int: Number of tweets processed
    """
    print("🚀 Starting VeriBot...")

    tweets = fetch_tweets(keyword, count, use_mock=use_mock)

    if not tweets:
        print("❌ No tweets found. Exiting...")
        return 0

    processed_count = 0
    for tweet in tweets:
        log_tweet(tweet)

        # Classify the tweet first
        category = classify_tweet(tweet["text"])
        log_classification(category)

        # Only respond to specific categories
        if category in ["AI Question", "Blockchain Question", "DeFi & Crypto Investment", 
                        "NFT & Metaverse", "Web3 & dApp Development"]:
            ai_response = generate_ai_response(tweet["text"], category)
            log_response(ai_response)

            # Apply safety filter
            safe_response = filter_ai_response(ai_response)
            log_safety_check(safe_response)

            if "⚠️ This response was flagged" in safe_response:
                print("❌ AI response flagged. Skipping reply.")
            else:
                post_tweet_reply(tweet["id"], tweet["author"], safe_response, use_mock=use_mock)
                log_reply(tweet["author"], safe_response)
                processed_count += 1
        else:
            print("⏭️ Skipping tweet as it doesn't match any specific category.")

        log_separator()
    
    return processed_count

if __name__ == "__main__":
    process_tweets() 