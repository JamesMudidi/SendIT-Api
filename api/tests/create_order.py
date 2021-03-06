from flask import json
from run import APP

class CreateOrder:
    """
    Create Order
    """

    def __init__(self):
        """
        Initiating flask object
        """
        self.app = APP
        self.client = self.app.test_client

    def create_order(self, data):
        """
        Create order
        """
        post = self.client().post(
            '/api/v1/parcels/',
            data=json.dumps(dict(
                user_id=data['user_id'],
                pickup=data['pickup'],
                destination=data['destination'],
                description=data['description'],
                weight=data['weight'],
                product=data['product']
            )),
            content_type='application/json'
        )
        return post
