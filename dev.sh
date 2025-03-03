#!/bin/bash

# VeriBot Development Script

echo "🚀 Starting VeriBot in development mode..."

# Activate virtual environment if it exists
if [ -d "veribot-env" ]; then
    echo "🔄 Activating virtual environment..."
    source veribot-env/bin/activate
fi

# Check if the bot is installed in development mode
if ! pip show veribot > /dev/null 2>&1; then
    echo "🔄 Installing VeriBot in development mode..."
    pip install -e .
fi

# Run the bot
echo "🚀 Running VeriBot..."
python run.py

echo "✅ VeriBot development session ended." 