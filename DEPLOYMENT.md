# VeriBot Deployment Guide

This guide explains how to deploy VeriBot in different environments.

## Prerequisites

- Python 3.8 or higher
- Docker (for containerized deployment)
- Twitter API credentials
- Gemini API key

## Local Development

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/veribot.git
   cd veribot
   ```

2. Set up a virtual environment:
   ```
   python -m venv veribot-env
   source veribot-env/bin/activate  # On Windows: veribot-env\Scripts\activate
   ```

3. Install in development mode:
   ```
   pip install -e .
   ```

4. Create a `.env` file with your API keys:
   ```
   TWITTER_BEARER_TOKEN=your_twitter_bearer_token
   GEMINI_API_KEY=your_gemini_api_key
   ```

5. Run the development script:
   ```
   ./dev.sh
   ```

## Docker Deployment

1. Make sure Docker is installed and running.

2. Create a `.env` file with your API keys (as above).

3. Run the deployment script:
   ```
   ./deploy.sh
   ```

4. Check the logs:
   ```
   docker logs -f veribot
   ```

## Manual Deployment

1. Install the package:
   ```
   pip install .
   ```

2. Create a `.env` file with your API keys (as above).

3. Run the bot:
   ```
   python -m veribot.main
   ```

## Cloud Deployment

### AWS EC2

1. Launch an EC2 instance with Amazon Linux 2.

2. Install Docker:
   ```
   sudo yum update -y
   sudo amazon-linux-extras install docker
   sudo service docker start
   sudo usermod -a -G docker ec2-user
   ```

3. Clone the repository and deploy:
   ```
   git clone https://github.com/yourusername/veribot.git
   cd veribot
   ./deploy.sh
   ```

### Google Cloud Run

1. Build and push the Docker image:
   ```
   gcloud builds submit --tag gcr.io/your-project/veribot
   ```

2. Deploy to Cloud Run:
   ```
   gcloud run deploy veribot \
     --image gcr.io/your-project/veribot \
     --platform managed \
     --set-env-vars "TWITTER_BEARER_TOKEN=your_token,GEMINI_API_KEY=your_key"
   ```

## Troubleshooting

- **API Rate Limits**: If you encounter rate limit issues, adjust the `RETRY_DELAY` in `config.py`.
- **Docker Issues**: Make sure Docker is running with `docker ps`.
- **Log Files**: Check `veribot.log` for detailed logs. 