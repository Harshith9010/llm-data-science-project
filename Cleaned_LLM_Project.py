LLAMA 3.1
groq pypi
!pip install groq==0.9.0

import os

# Set your API key as an environment variable before running
# Example (Linux/macOS): export GROQ_API_KEY="your_api_key_here"
# Example (Windows PowerShell): setx GROQ_API_KEY "your_api_key_here"

from groq import Groq

API_KEY = os.getenv("GROQ_API_KEY")  # Read key from environment
BASE_URL = "https://api.groq.com/"

client = Groq(api_key = API_KEY,
  base_url = BASE_URL)

response = client.chat.completions.create(
    messages =[
        {"role": "user", "content" :"tell me about fruits"}
    ],
    model = "llama-3.1-8b-instant"
)

response

output= response.choices[0].message.content

print(output)

LANGCHAIN (langchain pypi)
===============
(langchain-groq 0.1.9========0.1.6)
!pip install langchain-groq==0.1.9

import os

# Set your API key as an environment variable before running
# Example (Linux/macOS): export GROQ_API_KEY="your_api_key_here"
# Example (Windows PowerShell): setx GROQ_API_KEY "your_api_key_here"

from langchain_groq import ChatGroq

llm= ChatGroq(
    model = "llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

response =llm.invoke("print odd numbers")

response

output= response.content

print(output)