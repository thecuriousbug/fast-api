# Use a slim Python base image for efficiency
FROM python:3.9-slim

# Set the working directory for the container
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt ./requirements.txt

# Install dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Copy your FastAPI app code
COPY . .

# Set the entrypoint to run your app (adjust 'main:app' if your main file has a different name)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
