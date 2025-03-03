#!/usr/bin/env python
"""
Simple script to run VeriBot.
"""

from veribot.main import process_tweets

if __name__ == "__main__":
    print("=" * 50)
    print("VeriBot - AI-Powered Verifiable Social Media Assistant")
    print("=" * 50)
    
    # Process tweets with default settings (mock mode)
    processed = process_tweets()
    
    print("=" * 50)
    print(f"✅ Processed {processed} tweets")
    print("=" * 50) 