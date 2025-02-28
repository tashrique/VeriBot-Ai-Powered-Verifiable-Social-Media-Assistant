# VeriBot - AI-Powered Verifiable Social Media Assistant

Live Deployment: [Under Construction]()
Video Demo: [UnderConstruction]()

## 📌 Overview
**VeriBot** is an AI-powered Twitter assistant that monitors tweets related to Flare, Blockchain, and AI, classifies them, generates intelligent responses, and verifies AI-generated responses using blockchain. The goal is to enhance transparency and prevent misinformation by leveraging AI and blockchain.

## 🚀 Features
- **Monitors Tweets** related to Web3, Blockchain, and Flare.
- **Classifies tweets** using AI models.
- **Generates AI-powered responses** with GPT-4 or Gemini.
- **Logs responses on-chain** for transparency and integrity.
- **Uses Flare’s TEE verification** to ensure verifiable AI execution.

## 🔧 Tech Stack
| **Component**  | **Technology** |
|--------------|---------------|
| Backend API | FastAPI (Python) |
| AI Processing | OpenAI GPT-4 / Gemini |
| Blockchain | Flare Network, Solidity |
| Database (Optional) | PostgreSQL / Firebase |
| Twitter API | Tweepy (Python) |

## 🏗️ Setup Guide
### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/veribot.git
cd veribot
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Set Up Twitter API Keys**
- Register on [Twitter Developer Portal](https://developer.twitter.com/)
- Add API credentials in `.env` file

### **4. Deploy Smart Contract**
- Use Remix IDE or Hardhat to deploy `AIResponseLogger.sol`
- Update contract address in `config.py`

### **5. Run the Bot**
```bash
python main.py
```

## 📌 Contribution
Feel free to submit PRs or open issues to improve VeriBot!

## 🏆 License
This project is licensed under the **MIT License**.
