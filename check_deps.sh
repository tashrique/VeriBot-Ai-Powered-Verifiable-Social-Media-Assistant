#!/bin/bash

# Script to check dependencies in the Docker container

echo "🔍 Checking dependencies in the VeriBot Docker container..."

# Run a Python script to check dependencies
docker exec veribot python -c "
import sys
print('Python version:', sys.version)
print('\\nChecking required packages:')
packages = [
    'numpy', 
    'sentence_transformers', 
    'tweepy', 
    'google.generativeai', 
    'torch'
]
for package in packages:
    try:
        module = __import__(package)
        print(f'✅ {package} is installed')
        if hasattr(module, '__version__'):
            print(f'   Version: {module.__version__}')
    except ImportError:
        print(f'❌ {package} is NOT installed')
"

echo -e "\n🔍 Checking pip list in container:"
docker exec veribot pip list | grep -E 'numpy|sentence-transformers|tweepy|google-generativeai|torch' 