from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os

app = FastAPI()

# Define a Pydantic model to validate the request body
class ContentRequest(BaseModel):
    content: str

# Your existing logic to interact with the AI model
def analyze_log(content):
    api_key = os.environ.get('API_KEY')
    api_token = os.environ.get('API_TOKEN')
    account_id = os.environ.get('ACCOUNT_ID')
    model = "@cf/tinyllama/tinyllama-1.1b-chat-v1.0"
    messages = [
        {"role": "system", "content": "You are a system administrator and log analyzer tasked with providing guidance to beginner users. Analyze the log entries in a concise manner, summarizing each in 5 lines. For each log entry, provide the cause of the issue and a solution, ensuring that an equal amount of knowledge is provided for both the cause and the solution to empower beginner users to understand and address the errors effectively."},
        {"role": "user", "content": content}
    ]

    # Make the API request
    response = requests.post(
        f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/{model}",
        headers={"Authorization": f"Bearer {api_token}"},
        json={"messages": messages}
    )

    # Parse the response
    inference = response.json()

    # Extract the response from the inference
    result = inference.get("result")
    if result:
        response = result.get("response")
        if response:
            return response
    # If the response couldn't be extracted, return an error message
    return {"error": "Failed to analyze log."}

# Endpoint to handle incoming requests
@app.post("/analyze_log")
def analyze_log_endpoint(content_request: ContentRequest):
    # Extract content from the request
    content = content_request.content

    # Your logic to interact with the AI model
    response = analyze_log(content)

    return response


@app.get('/')
def welcome():
    return {'Hello' : 'visit /analyze_log  for the work'}
