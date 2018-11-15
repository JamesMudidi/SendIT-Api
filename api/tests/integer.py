from unittest import TestCase
from flask import json
from api.tests.create_order import CreateOrder

class Integer(TestCase):

    def integer(self):
        order = {
            'user_id':'1',
            'pickup': 'kampala',
            'destination': 'kireka',
            'description': 'light',
            'weight': 10,
            'product': 'parcel',
        }
        post = CreateOrder().createOrder(order)
        resp = json.loads(post.data.decode())
        self.assertEqual(resp['success'], False)
        self.assertEqual(resp['error']['message'], 'User_id and Weight must be integers')
        self.assertEqual(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)
