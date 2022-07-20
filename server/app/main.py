from flask import Flask, request, jsonify, json, make_response
from flask_cors import CORS, cross_origin
import os
from dotenv import load_dotenv
import requests

load_dotenv()

application = app = Flask(__name__)
cors = CORS(app)

MY_KEY = os.getenv("HF_KEY")

API_URL = "https://api-inference.huggingface.co/models/matanbn/smsPhishing"
headers = {"Authorization": MY_KEY}


def query(payload):
    print(payload)
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


@app.route('/predict', methods=['POST', 'OPTIONS'])
def predict():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    elif request.method == 'POST':
        sms = request.form.get('sms', False)
        if sms is False:
            return jsonify({'error': 'SMS is empty'})
        if sms is None or sms == "":
            return jsonify({'error': 'no sms inserted'})
        try:
            label = query({"inputs": sms})
            return jsonify(label)
        except:
            return jsonify({'error': 'error during prediction'})
