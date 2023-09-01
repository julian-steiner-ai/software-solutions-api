"""
Module to create functions for the melicus-musikverlag backend.
"""

from flask import jsonify

from melicus.model.order import Order
from melicus.license.pdf_licenser import PDFLicenser

def license_music_sheet(json_data):
    """
    Create a licensed PDF.
    """
    success, handled_params = _handle_params(json_data=json_data)
    licensed_pdfs = []

    if success:
        try:
            success, licensed_pdfs = _license_music_sheets(order=handled_params)
        except Exception as exp:
            success = False
            message = str(exp)
    else:
        success = False
        message = ''
    
    return success, licensed_pdfs, message

def _handle_params(json_data):
    try:
        if json_data:
            return True, Order.create_from_json_object(
                order_number=json_data['order_number'],
                order_date=json_data['order_date'],
                json_address=json_data['address'],
                json_articles=json_data['articles']
            )
    except Exception as exp:
        return False, str(exp)

def _license_music_sheets(order : Order):
    pdf_licenser = PDFLicenser(
        company_logo_pic_path='C:\\Users\\steinerj\\Documents\\Projects\\Software-Solutions\\software-solutions-api\\melicus\\assets\\melicus-musikverlag.jpg',
        order=order
    )

    return pdf_licenser.license_articles()
