"""
Module to return validations values
"""
from flask import jsonify

class DataValidation:
    """
    Class with methods to return validation values
    """

    error_msg = {"success":False, "error":{"message":""}}

    def __init__(self, req):
        """
        Class constructor for intiating a request object
        """
        self.req = req

    def string_error(self):
        """
        Method that checks for string errorss
        """
        if isinstance(self.req['pickup'], str) and isinstance(self.req['destination'], str):
            if isinstance(self.req['description'], str) and isinstance(self.req['product'], str):
                return True
        msg = 'Pickup, Destination, Description and Product should be Strings'
        DataValidation.error_msg['error']['message'] = msg
        return jsonify(DataValidation.error_msg), 400

    def integer_error(self):
        """
        Integer errors
        """
        if isinstance(self.req['user_id'], int) and isinstance(self.req['weight'], int):
            return True
        msg = 'User_id and Weight must be integers'
        DataValidation.error_msg['error']['message'] = msg
        return jsonify(DataValidation.error_msg), 400

    def empty_keys(self):
        """
        Blank
        """
        if self.req['user_id'] != '' and self.req['description'] != '' and self.req['product'] != '' and self.req['description'] != '' and self.req['pickup'] != '' and self.req['weight'] != '':
            return True
        msg = 'Blanks not allowed'
        DataValidation.error_msg['error']['message'] = msg
        return jsonify(DataValidation.error_msg), 400

    def lesser_zero(self):
        """
        Check user_id or weight is less than zero
        """
        if self.req['user_id'] > 0 and self.req['weight'] > 0:
            return True
        msg = 'user_id and weight should be greater than zero'
        DataValidation.error_msg['error']['message'] = msg
        return jsonify(DataValidation.error_msg), 400

    def validate(self):
        """
        Check  validity for posted data
        """
        if isinstance(self.string_error(), bool) and isinstance(self.integer_error(), bool):
            if isinstance(self.empty_keys(), bool) and isinstance(self.lesser_zero(), bool):
                return True
        return jsonify(DataValidation.error_msg), 400
