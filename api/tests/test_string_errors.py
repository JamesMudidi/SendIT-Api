from unittest import TestCase
from flask import json
from api.tests.create_order import CreateOrder

class TestStringErrors(TestCase):

    def test_string_errors(self):
        order = {
            'user_id':1,
            'pickup': 100,
            'destination': 'kireka',
            'description': 'light',
            'weight': 10,
            'product': 'parcel',
        }
        post = CreateOrder().create_order(order)

        self.assertEqual(resp['success'], False)
        self.assertEqual(resp['error']['message'], 'Pickup, Destination, Description and Product should be Strings')
        self.assertEqual(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)
