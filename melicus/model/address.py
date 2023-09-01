"""
Module for Adress Object.
"""

class Address:
    """
    Class to define Address Object.
    """
    def __init__(
        self,
        lastname,
        firstname,
        street,
        postcode,
        place,
        nation,
        company
    ):
        self.lastname = lastname
        self.firstname = firstname
        self.street = street
        self.postcode = postcode
        self.place = place
        self.nation = nation
        self.company = company

    @staticmethod
    def create_from_json(json_address):
        """
        Create an Address Object from a JSON Parameter.
        """
        return Address(
            lastname=json_address['lastname'],
            firstname=json_address['firstname'],
            street=json_address['street'],
            postcode=json_address['postcode'],
            place=json_address['place'],
            nation=json_address['nation'],
            company=json_address['company']
        )
