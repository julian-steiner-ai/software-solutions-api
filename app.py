"""
"""

import os
from flask import Flask
from flask import jsonify

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/cowfeedcalculator', methods=["GET", "POST"])
def cowfeedcalculator():
    response = jsonify([{'Name': 'Julian'}, {'Name': 'Julian'}, {'Name': 'Julian'}])
    return response

if __name__ == "__main__":
    cert_file = os.getenv('FLASK_CERT', '') # fullchain.pem
    key_file = os.getenv('FLASK_CERT_KEY', '') # privatekey.pem

    ssl_context = (cert_file, key_file)

    app.run(host='0.0.0.0', ssl_context=ssl_context)
