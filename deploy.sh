#!/bin/bash

# VeriBot Deployment Script

echo "🚀 Deploying VeriBot..."

# Build the Docker image with no cache to ensure fresh dependencies
echo "🔨 Building Docker image..."
docker build --no-cache -t veribot:latest .

# Check if the build was successful
if [ $? -ne 0 ]; then
    echo "❌ Docker build failed. Exiting."
    exit 1
fi

echo "✅ Docker image built successfully."

# Check if a container with the same name is already running
if [ "$(docker ps -q -f name=veribot)" ]; then
    echo "🔄 Stopping existing VeriBot container..."
    docker stop veribot
    docker rm veribot
fi

# Run the Docker container
echo "🚀 Starting VeriBot container..."
docker run -d --name veribot \
    --restart unless-stopped \
    -v $(pwd)/.env:/app/.env \
    -v $(pwd)/mock_tweets.json:/app/mock_tweets.json \
    -v $(pwd)/mock_replies.log:/app/mock_replies.log \
    -v $(pwd)/veribot.log:/app/veribot.log \
    veribot:latest

# Check if the container started successfully
if [ $? -ne 0 ]; then
    echo "❌ Failed to start VeriBot container. Exiting."
    exit 1
fi

echo "✅ VeriBot deployed successfully!"
echo "📊 To view logs: docker logs -f veribot" 