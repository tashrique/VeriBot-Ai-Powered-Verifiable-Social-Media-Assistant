"""
AI responder module for VeriBot.
Handles AI response generation and verification.
"""

import random
import re
from google import genai
from veribot.config import GEMINI_API_KEY
from veribot.classification.categories import prompt_templates, DEFI_PROJECTS

# Initialize Gemini client
gemini = genai.Client(api_key=GEMINI_API_KEY)

def generate_ai_response(tweet_text, category):
    """
    Generate AI response to the given tweet.
    
    Args:
        tweet_text (str): The text of the tweet
        category (str): The category of the tweet
        
    Returns:
        str: The AI-generated response
    """
    if category in prompt_templates:
        prompt = prompt_templates[category].format(tweet=tweet_text) + "\n\nBe concise and short and direct."
    else:
        prompt = f"Respond to this tweet in an informative way:\n\nTweet: {tweet_text}\nResponse:"
    try:
        response = gemini.models.generate_content(
            model="gemini-2.0-flash", contents=prompt)
        response_text = response.text
        response_text = inject_real_projects(response_text)
        return response_text
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return "Unable to generate AI response. Please try again later."

def filter_ai_response(ai_response):
    """
    Filters AI-generated responses to prevent harmful or misleading content.
    
    Args:
        ai_response (str): The AI-generated response
        
    Returns:
        str: The filtered response or a warning message
    """
    banned_words = ["scam", "fraud", "hustle", "pump", "dump", "rug pull", "fake", "exploit", "manipulation"]
    
    # Use regex to detect banned words even if slightly altered
    for word in banned_words:
        if re.search(rf"\b{word}\b", ai_response, re.IGNORECASE):
            return "⚠️ This response was flagged for potential harmful content and will not be posted."
    
    # Ensure response isn't too long for Twitter
    if len(ai_response) > 280:
        ai_response = ai_response[:277] + "..."  # Trim to fit Twitter limit
    
    return ai_response

def inject_real_projects(response_text):
    """
    Replace placeholders in AI-generated text with real DeFi projects.
    
    Args:
        response_text (str): The AI-generated response
        
    Returns:
        str: The response with real project names
    """
    if "[Project A]" in response_text or "[Project B]" in response_text:
        selected_projects = random.sample(DEFI_PROJECTS, 2)  # Pick two random projects
        response_text = response_text.replace("[Project A]", selected_projects[0]["name"])
        response_text = response_text.replace("[Project B]", selected_projects[1]["name"])
    return response_text

def mock_tee_verification():
    """
    Simulates TEE verification process.
    
    Returns:
        bool: True if verification successful, False otherwise
    """
    verified = random.choice([True, False])  # Randomly simulate TEE success/failure
    return verified 