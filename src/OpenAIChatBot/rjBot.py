'''
Created on Aug 26, 2023

@author: Admin
'''
import requests

URL = "https://api.openai.com/v1/chat/completions"

payload = {
"model": "gpt-3.5-turbo",
"messages": [{"role": "user", "content": f"What is the first computer in the world?"}],
"temperature" : 1.0,
"top_p":1.0,
"n" : 1,
"stream": False,
"presence_penalty":0,
"frequency_penalty":0,
}

headers = {
"Content-Type": "application/json",
"Authorization": f"Bearer Key received from openapi"
}

response = requests.post(URL, headers=headers, json=payload, stream=False)