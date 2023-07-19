"""
"""

import os
from flask import Flask
from flask import Response
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/cowfeedcalculator')
def cowfeedcalculator():
    return jsonify([{'Name': 'Julian'}, {'Name': 'Julian'}, {'Name': 'Julian'}])

if __name__ == "__main__":
    cert_file = os.getenv('FLASK_CERT', '') # fullchain.pem
    key_file = os.getenv('FLASK_CERT_KEY', '') # privatekey.pem

    ssl_context = (cert_file, key_file)

    app.run(host='0.0.0.0', ssl_context=ssl_context)
