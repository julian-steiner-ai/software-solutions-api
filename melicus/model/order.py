"""
Module for Order Object.
"""

from typing import List
from melicus.model.article import Article
from melicus.model.address import Address

class Order:
    """
    Class to define Order Object.
    """
    def __init__(
        self,
        order_number : str,
        order_date : str,
        address : Address,
        articles : List[Article]
    ):
        self.order_number = order_number
        self.order_date = order_date
        self.address = address
        self.articles = articles

    def name(self):
        """
        Return the name of the customer for the license.
        """
        return self.address.company if self.address.company and self.address.company != '' else f'{self.address.lastname}, {self.address.firstname}'

    def get_license_name(self):
        """
        Return the license name for an order.
        """
        return f"Lizenziert für {self.name()} - {self.address.street} - {self.address.postcode} - {self.address.place} - ({self.order_number} vom {self.order_number})"

    @staticmethod
    def create_from_json_object(
        order_number,
        order_date,
        json_address,
        json_articles
    ):
        """
        Create a Order Object from a JSON Parameter.
        """
        return Order(
            order_number=order_number,
            order_date=order_date,
            address=Address.create_from_json(json_address=json_address),
            articles=[Article.create_from_json(json_article=json_article)
                      for json_article
                      in json_articles
            ]
        )
