"""
Module for Article Object.
"""

import base64

class Article:
    """
    Class to define Article Object.
    """
    def __init__(
        self,
        article_number,
        music_sheet
    ):
        self.article_number = article_number
        self.music_sheet = music_sheet
    
    @staticmethod
    def create_from_json(
        json_article
    ):
        """
        Create an Article Object from a JSON Parameter.
        """
        return Article(
            article_number=json_article['article_number'],
            music_sheet=base64.b64decode(json_article['music_sheet'])
        )
