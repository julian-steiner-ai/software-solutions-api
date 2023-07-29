from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"running": True})
