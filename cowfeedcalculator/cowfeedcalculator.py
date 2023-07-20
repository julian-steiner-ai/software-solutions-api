"""
Backend functions for Cow Feed Calculator.
"""

from os import listdir
from os.path import isfile, join, exists

import json

class CowFeedCalculator:
    """
    CowFeedCalculator.
    """
    def get_all_calculations(self, directory):
        """
        Return all the saved calculations.
        """
        return self.read_history_files(directory)

    def save_calculation(self, directory, filname, json_content):
        """
        Save a JSON Object from a Calculation in the directory.
        """
        try:
            if exists(directory):
                with open(join(directory, filname), "w", encoding="UTF-8") as file:
                    json.dump(json_content, file)
                    return {'success': True}
            else:
                return {'success': False, 'msg': f'Directory {directory} does not exist!'}
        except Exception as exp:
            return {'success': False, 'msg': str(exp)}

    def read_history_files(self, directory):
        """
        Read all the Files and Return the content as JSON.
        """
        data = []
        try:
            if exists(directory):
                for path in listdir(directory):
                    if isfile(join(directory, path)):
                        with open(join(directory, path), 'r', encoding='UTF-8') as file:
                            data.append({
                                'name': path,
                                'feedTypes': file.read()
                            })
                return {'success': True, 'data': data}
            else:
                return {'success': False, 'data': data, 'msg': f'Directory {directory} does not exist!'}
        except Exception as exp:
            return {'success': False, 'data': data, 'msg': str(exp)}
