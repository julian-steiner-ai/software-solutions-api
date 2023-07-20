"""
Julian Steiner Software Solutions Backend.
"""

import os

import ssl

from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
from datetime import date

from cowfeedcalculator.cowfeedcalculator import CowFeedCalculator

app = Flask(__name__)

CORS(app)

@app.route('/test', methods=['GET'])
def test():
    return jsonify(
        {
            'CERT_FILE': os.getenv('FLASK_CERT', ''),
            'KEY_FILE': os.getenv('FLASK_CERT_KEY', '')
        }
    )

@app.route('/cowfeedcalculator/calculations', methods=["GET", "POST"])
def cowfeedcalculator():
    """
    Return the History for the Cow Feed Calculator.
    """
    return jsonify(CowFeedCalculator().get_all_calculations(os.getenv('COWFEEDCALC_HISTORY_DIR', '/')))

@app.route('/cowfeedcalculator/calculation/save', methods=['POST'])
def save_calculation():
    """
    Save a new entry for the Cow Feed Calculator.
    """
    directory = os.getenv('COWFEEDCALC_HISTORY_DIR', '/')
    filename=f'{date.today().strftime("%d%m%Y")}.json'

    feed_types = ''
    if 'feedTypes' in request.json: 
        feed_types = request.json['feedTypes']

    return jsonify(CowFeedCalculator().save_calculation(
        directory=directory,
        filname=filename,
        json_content=feed_types
    ))

if __name__ == "__main__":
    cert_file = os.getenv('FLASK_CERT', '') # fullchain.pem
    key_file = os.getenv('FLASK_CERT_KEY', '') # privatekey.pem

    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx.load_cert_chain(cert_file, key_file)

    app.run(host='0.0.0.0', ssl_context=ctx)
