"""
Classification categories and prompt templates for VeriBot.
"""

# Categories for tweet classification with example texts
categories = {
    "AI Question": [
        "What is AI?", "How does AI work?", "Explain machine learning", "What is deep learning?",
        "How does AI impact blockchain?", "What are neural networks?", "What is natural language processing?",
        "How can AI be used in finance?", "What is reinforcement learning?", "What are LLMs?",
        "How do transformers work in AI?", "What is generative AI?", "What is fine-tuning in AI?",
        "Can AI predict stock prices?", "What are ethical concerns in AI?", "Is AI dangerous?",
        "How do recommendation systems work?", "How does AI automate trading?",
        "How can AI help in cybersecurity?", "What is federated learning?"
    ],
    
    "Blockchain Question": [
        "What is Flare?", "How does Flare Blockchain work?", "What are DeFi projects?", 
        "What are smart contracts?", "How does Ethereum work?", "What is staking in blockchain?",
        "What is proof of stake vs proof of work?", "How do oracles work in blockchain?",
        "What are layer 2 solutions?", "What is the future of blockchain?", 
        "How does blockchain handle transactions?", "What is gas fee in Ethereum?",
        "What are rollups in blockchain?", "What is a DAO?", "How does Flare ensure security?",
        "What are bridges in blockchain?", "How does Flare integrate with other blockchains?",
        "What is FTSO in Flare?", "What is Songbird Network?", "How does Flare handle interoperability?"
    ],
    
    "DeFi & Crypto Investment": [
        "What is yield farming?", "How do liquidity pools work?", "What is a decentralized exchange?",
        "How do I earn passive income in crypto?", "What is impermanent loss?",
        "Is DeFi better than traditional finance?", "How do flash loans work?",
        "What is a stablecoin?", "How do crypto lending platforms work?", 
        "What are the best DeFi projects on Flare?", "How does staking work in DeFi?",
        "Is crypto a good investment?", "What are tokenomics?", "What is a rug pull?",
        "How do I avoid scams in crypto?", "What are the risks of DeFi?", "What is yield aggregation?",
        "Which crypto wallets are safest?", "What is an airdrop?", "Is Bitcoin or Ethereum better?",
        "What is market cap in crypto?", "How do I analyze crypto charts?",
        "What is the difference between CeFi and DeFi?"
    ],
    
    "NFT & Metaverse": [
        "What is an NFT?", "How do NFTs work?", "How do I create an NFT?", "What is OpenSea?",
        "Are NFTs a good investment?", "What are gas fees for NFTs?", "How do I mint an NFT?",
        "What is a metaverse?", "What are virtual lands in the metaverse?",
        "What is the future of NFTs?", "What is a profile picture NFT (PFP)?",
        "Are gaming NFTs valuable?", "Which blockchain is best for NFTs?",
        "How do royalties work in NFTs?", "What is an NFT marketplace?",
        "What are the biggest NFT projects?", "How does Flare support NFTs?",
        "Can I sell my NFTs on multiple platforms?", "What is fractionalized NFT ownership?"
    ],
    
    "Web3 & dApp Development": [
        "How do I build a dApp?", "What programming languages are used in blockchain?",
        "How does Solidity work?", "What is a smart contract audit?",
        "How do I interact with a smart contract?", "How do I deploy a smart contract?",
        "What is Web3.js?", "What is IPFS?", "How do I use The Graph in Web3?",
        "What is ENS (Ethereum Name Service)?", "What are decentralized storage solutions?",
        "How does Web3 authentication work?", "What is Moralis?",
        "What are the best tools for dApp development?", "What are smart contract vulnerabilities?",
        "How do I prevent reentrancy attacks?", "How do I fetch blockchain data in a dApp?"
    ],
    
    "Spam/Offensive": [
        "Buy now!", "Get rich quick", "Scam alert", "Free crypto giveaway!", 
        "Click this link for free Bitcoin!", "Earn $1000 per day with crypto!", 
        "Sign up for instant gains!", "Invest in this new token before it's too late!",
        "Massive gains guaranteed!", "Pump and dump strategy!", "This token will 100x!",
        "Join our exclusive trading group!", "Crypto millionaire secrets revealed!",
        "Spammy message with no context", "All caps aggressive promotional text",
        "Random emojis with no meaning", "Fake celebrity endorsements"
    ],
    
    "General Discussion": [
        "Flare is amazing", "I love crypto", "Blockchain is the future", "Crypto is the best investment",
        "What do you think about crypto regulations?", "Why is Bitcoin pumping?", 
        "Which is better, Bitcoin or Ethereum?", "Who is the best crypto influencer?",
        "Will blockchain replace banks?", "What is the biggest crypto innovation?",
        "Crypto is dead!", "How do I convince my friends to buy crypto?", 
        "The government is scared of crypto!", "What are your thoughts on Web3?",
        "What is your favorite blockchain?", "Can blockchain help in real-world problems?",
        "I just made my first NFT!", "Why do gas fees keep increasing?", "Where can I buy crypto?"
    ],
    
    "Meme & Viral Content": [
        "Meme alert", "Meme of the day", "Meme of the week", "This crypto is going to the moon!",
        "WAGMI", "HODL", "When Lambo?", "To the moon!", "Crypto winter is here!",
        "I just bought the dip!", "Why is my portfolio all red?", "I'm becoming a crypto millionaire!",
        "When will Bitcoin hit 100k?", "My crypto holdings be like...", 
        "That moment when you buy high and sell low", "Degen trading is life",
        "All my bags are in one coin", "This chart looks bullish af!", 
        "Only legends bought Bitcoin at $10", "I'm ready for the next bull run!",
        "FOMO kicking in!", "The crypto rollercoaster continues!"
    ]
}

# Prompt templates for AI response generation
prompt_templates = {
    "AI Question": (
        "Generate a **brief, engaging, and tweet-friendly** response to this AI-related question.\n"
        "Keep it under 280 characters. Use simple language, and add a relevant example if possible.\n"
        "Tweet: {tweet}\n"
        "Reply:"
    ),
    "Blockchain Question": (
        "Give a short, Twitter-friendly response to this blockchain-related question.\n"
        "Make it engaging and concise. If relevant, add a key fact or example.\n"
        "Tweet: {tweet}\n"
        "Reply:"
    ),
    "DeFi & Crypto Investment": (
        "Provide a short, engaging tweet reply about this DeFi topic.\n"
        "Keep it under 280 characters. Highlight risks & benefits briefly.\n"
        "Tweet: {tweet}\n"
        "Reply:"
    ),
    "NFT & Metaverse": (
        "Generate a concise, tweet-friendly response about NFTs or the Metaverse.\n"
        "Keep it fun & engaging! Use emojis if relevant.\n"
        "Tweet: {tweet}\n"
        "Reply:"
    ),
    "Web3 & dApp Development": (
        "Write a short, insightful tweet reply about Web3 development.\n"
        "Make it informative but friendly.\n"
        "Tweet: {tweet}\n"
        "Reply:"
    ),
    "Spam/Offensive": "This tweet is likely spam. No response needed.",
    "Meme": "This is a meme. No response needed.",
    "General Discussion": "This is a general discussion tweet. No response needed."
}

# Example DeFi projects for reference
DEFI_PROJECTS = [
    {"name": "Pangolin (FlareX)", "type": "DEX", "url": "https://app.pangolin.exchange/"},
    {"name": "FSwap", "type": "DEX", "url": "https://fswap.io/"},
    {"name": "ExFi", "type": "Lending", "url": "https://exfi.flr.finance/"},
    {"name": "YFLoans", "type": "Lending", "url": ""},
    {"name": "Flare Farm", "type": "Yield Farming", "url": "https://flarefarm.com/"},
] 