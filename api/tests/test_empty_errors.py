from unittest import TestCase
from flask import json
from api.tests.create_order import CreateOrder

class TestEmptyErrors(TestCase):

    def test_empty_errors(self):
        """
        Test blank spaces
        """
        order = {
           'user_id':1,
            'pickup': 'kampala',
            'destination': 'kireka',
            'description': 'light',
            'weight': 10,
            'product': 'parcel',
        }
        post = CreateOrder().create_order(order)

        resp = json.loads(post.data.decode())
        self.assertEqual(resp['success'], True)
        self.assertEqual(resp['error_msg']['message'], 'No blank spaces allowed')
        self.assertEqual(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)
