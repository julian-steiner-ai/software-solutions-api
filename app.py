from flask import Flask
from flask import jsonify
from flask import request, json

from melicus.melicus import license_music_sheet

app = Flask(__name__)

@app.route('/state', methods=['GET'])
def state():
    """
    Return the State of the Backend.
    """
    return _handle_api_return(
        True,
        None,
        'Running'
    )

@app.route('/melicus-musikverlag/order/license', methods=['POST'])
def melicus_musikverlag_license_pdf():
    """
    License PDF for melicus-musikverlag
    """
    lic
    return license_music_sheet(
        json_data=json.loads(request.json)
    )

@app.route('/melicus-musikverlag/orders/', methods=['GET'])
def melicus_musikverlag_get_licensed_music_sheet():
    """
    Return a Licensed Music Sheet
    """
    return jsonify({
        'NotImplemented': True
    })

def _handle_api_return(success, data, message):
    return jsonify({
        'success': success,
        'data': data,
        'message': message
    })
