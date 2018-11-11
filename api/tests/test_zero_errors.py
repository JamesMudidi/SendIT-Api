from unittest import TestCase
from flask import json
from api.tests.create_order import CreateOrder

class TestZeroErrors(TestCase):

    def test_zero_errors(self):
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
        self.assertEqual(resp['error']['message'], 'User_id and Weight should not be less than zero')
        self.assertEqual(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)
