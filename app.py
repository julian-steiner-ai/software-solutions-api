"""
"""

import os

from flask import Flask
from flask import jsonify
from flask_cors import CORS

from cowfeedcalculator import CowFeedCalculator

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    """
    Hello World example.
    """
    return 'Hello, World!'

@app.route('/cowfeedcalculator', methods=["GET", "POST"])
def cowfeedcalculator():
    """
    Return the History for the Cow Feed Calculator.
    """
    calc = CowFeedCalculator().get_all_calculations()
    calc_json = [x.to_json() for x in calc]
    return jsonify(calc_json)

@app.route('/cowfeedcalculator/save', methods=['POST'])
def save_calculation():
    """
    Save a new entry for the Cow Feed Calculator.
    """
    return jsonify({'success': True})

if __name__ == "__main__":
    cert_file = os.getenv('FLASK_CERT', '') # fullchain.pem
    key_file = os.getenv('FLASK_CERT_KEY', '') # privatekey.pem
    history_directory = os.getenv('COWFEEDCALC_HISTORY_DIR', '')

    print(f'CERT_FILE: {cert_file}')
    print(f'KEY_FILE: {key_file}')
    print(f'COWFEEDCALC_HISTORY_DIR: {history_directory}')

    ssl_context = (cert_file, key_file)

    app.run(host='0.0.0.0', ssl_context=ssl_context)
