"""
Command-line interface for VeriBot.
"""

import argparse
from veribot.main import process_tweets

def main():
    """
    Main entry point for the command-line interface.
    """
    parser = argparse.ArgumentParser(description="VeriBot - AI-Powered Verifiable Social Media Assistant")
    parser.add_argument("--keyword", type=str, default="Flare Network", 
                        help="Keyword to search for tweets")
    parser.add_argument("--count", type=int, default=6, 
                        help="Number of tweets to process")
    parser.add_argument("--live", action="store_true", 
                        help="Use live Twitter API instead of mock data")
    
    args = parser.parse_args()
    
    # Process tweets with the provided arguments
    processed = process_tweets(
        keyword=args.keyword,
        count=args.count,
        use_mock=not args.live
    )
    
    print(f"✅ Processed {processed} tweets")

if __name__ == "__main__":
    main() 