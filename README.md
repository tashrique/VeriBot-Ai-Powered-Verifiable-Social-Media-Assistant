# VeriBot: AI-Powered Verifiable Social Media Assistant

VeriBot is an AI-powered social media assistant that monitors Twitter for relevant conversations about blockchain, crypto, and AI topics, and provides helpful, verifiable responses.


[![Maintainability](https://api.codeclimate.com/v1/badges/b384a1c1950ac229bb23/maintainability)](https://codeclimate.com/github/tashrique/VeriBot-Ai-Powered-Verifiable-Social-Media-Assistant/maintainability)

## Features

- **Tweet Classification**: Automatically categorizes tweets into relevant topics
- **AI Response Generation**: Generates informative responses using Gemini AI
- **Content Safety**: Filters responses to prevent harmful or misleading content
- **Mock Mode**: Test functionality without posting to Twitter

## Project Structure

The project follows a modular structure:

```
veribot/
├── __init__.py         # Package initialization
├── config.py           # Configuration and environment variables
├── main.py             # Main entry point
├── api/                # API interaction modules
│   ├── __init__.py
│   └── twitter.py      # Twitter API functions
├── classification/     # Classification modules
│   ├── __init__.py
│   ├── categories.py   # Classification categories and templates
│   └── classifier.py   # Tweet classification logic
├── ai/                 # AI modules
│   ├── __init__.py
│   └── responder.py    # AI response generation and filtering
└── utils/              # Utility modules
    ├── __init__.py
    └── logger.py       # Logging utilities
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/veribot.git
   cd veribot
   ```

2. Create a virtual environment:
   ```
   python -m venv veribot-env
   source veribot-env/bin/activate  # On Windows: veribot-env\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -e .
   ```

4. Create a `.env` file with your API keys:
   ```
   TWITTER_BEARER_TOKEN=your_twitter_bearer_token
   GEMINI_API_KEY=your_gemini_api_key
   ```

## Usage

Run the bot:

```
python -m veribot.main
```

Or use the command-line interface:

```
veribot --keyword "Flare Network" --count 10 --live
```

## Development

### Running Tests

```
pytest
```

### Building Documentation

```
cd docs
make html
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
