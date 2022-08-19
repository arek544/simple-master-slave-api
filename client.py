
import requests
from flask import Flask, request, jsonify

# api-endpoint
API_ENDPOINT = "http://10.1.0.100:5000"

# sending get request and saving the response as response object
r = requests.get(url = API_ENDPOINT)
data = r.json()
print(data)

# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)
data = r.json()
print(data)