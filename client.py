
import requests
from flask import Flask, request, jsonify
import time

# api-endpoint
API_ENDPOINT = "http://10.1.0.100:5000"

# sending post request and saving response as response object
r = requests.get(url = API_ENDPOINT + '/run')
data = r.json()
print(data)

time.sleep(10)

# sending post request and saving response as response object
r = requests.get(url = API_ENDPOINT + '/stop')
data = r.json()
print(data)