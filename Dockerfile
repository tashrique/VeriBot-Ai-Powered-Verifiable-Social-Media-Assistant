FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies required for numpy and other packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /app/

# Install the package in development mode
RUN pip install -e .

# Verify numpy is installed
RUN python -c "import numpy; print(f'NumPy version: {numpy.__version__}')"

EXPOSE 8000

# Run the bot using the run.py script
CMD ["python", "run.py"]