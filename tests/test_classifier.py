"""
Tests for the classifier module.
"""

import pytest
from veribot.classification.classifier import classify_tweet

def test_classify_ai_question():
    """Test classification of AI questions."""
    tweet = "What is the difference between AI and machine learning?"
    category = classify_tweet(tweet)
    assert category == "AI Question"

def test_classify_blockchain_question():
    """Test classification of blockchain questions."""
    tweet = "How does Flare Network handle cross-chain interoperability?"
    category = classify_tweet(tweet)
    assert category == "Blockchain Question"

def test_classify_defi_question():
    """Test classification of DeFi questions."""
    tweet = "What is yield farming and how can I get started?"
    category = classify_tweet(tweet)
    assert category == "DeFi & Crypto Investment"

def test_classify_spam():
    """Test classification of spam."""
    tweet = "FREE CRYPTO GIVEAWAY! Send 0.1 BTC to get 1 BTC back!"
    category = classify_tweet(tweet)
    assert category == "Spam/Offensive"

def test_classify_general_discussion():
    """Test classification of general discussion."""
    tweet = "I think blockchain technology is really interesting."
    category = classify_tweet(tweet)
    assert category == "General Discussion" 