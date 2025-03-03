"""
Tweet classifier module for VeriBot.
Uses sentence embeddings to classify tweets into predefined categories.
"""

import numpy as np
from sentence_transformers import SentenceTransformer
from veribot.classification.categories import categories

# Initialize SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

# Pre-compute embeddings for each category
embeddings = {key: model.encode(value) for key, value in categories.items()}

def classify_tweet(tweet_text):
    """
    Classify tweet into one of the predefined categories.
    
    Args:
        tweet_text (str): The text of the tweet to classify
        
    Returns:
        str: The category the tweet belongs to
    """
    tweet_embedding = model.encode(tweet_text)
    
    # Calculate cosine similarity between tweet embedding and all category embeddings
    similarities = {
        category: np.max(np.dot(tweet_embedding, np.array(embeddings).T))
        for category, embeddings in embeddings.items()
    }
    best_match = max(similarities, key=similarities.get)
    
    return best_match if similarities[best_match] > 0.5 else "General Discussion" 