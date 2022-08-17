import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# responding to get request
@app.route('/', methods=['GET'])
def index():
    return json.dumps({
        'name': 'Peter',
        'surname': 'Parker'
    })

# responding to post request
@app.route('/', methods=['POST'])
def query_records():
    print(request.form['name'])
    return jsonify({"success": True})

app.run()