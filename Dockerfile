FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app/ ./app/
COPY models/ ./models/
COPY audio_samples/ ./audio_samples/
COPY config.yaml .
COPY run.py .

# Command to run the application
CMD ["python", "run.py"]