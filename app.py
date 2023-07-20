"""
Julian Steiner Software Solutions Backend.
"""

import os

from OpenSSL import SSL

from datetime import date
from flask import Flask, request
from flask import jsonify
from flask_cors import CORS

from cowfeedcalculator.cowfeedcalculator import CowFeedCalculator

app = Flask(__name__)

CORS(app)

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
    key_file = os.getenv('PRIVKEY_FILE', '') #privkey
    fullchain_file = os.getenv('FULLCHAIN_FILE', '') #fullchain
    cert_file = os.getenv('CERT_FILE', '') #cert

    context = SSL.Context(SSL.TLS1_3_VERSION)

    context.use_privatekey_file(key_file)
    context.use_certificate_chain_file(fullchain_file)
    context.use_certificate_file(cert_file)

    app.run(ssl_context=context)
