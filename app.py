"""
Julian Steiner Software Solutions Backend.
"""

from __future__ import print_function
import os
import sys

print('This is error output', file=sys.stderr)
print('This is standard output', file=sys.stdout)

from flask import Flask
from flask import jsonify
from flask_cors import CORS

from cowfeedcalculator.cowfeedcalculator import CowFeedCalculator

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

cert_file = os.getenv('FLASK_CERT', 'Test') # fullchain.pem
key_file = os.getenv('FLASK_CERT_KEY', 'Test') # privatekey.pem
history_directory = os.getenv('COWFEEDCALC_HISTORY_DIR', 'Test')

print(f'CERT_FILE: {cert_file}', file=sys.stdout)
print(f'KEY_FILE: {key_file}', file=sys.stdout)
print(f'COWFEEDCALC_HISTORY_DIR: {history_directory}', file=sys.stdout)

if __name__ == "__main__":
    ssl_context = (cert_file, key_file)
    app.run(host='0.0.0.0', ssl_context=ssl_context)
