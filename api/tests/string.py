from unittest import TestCase
from flask import json
from api.tests.createOrder import CreateOrder

class string(TestCase):

    def string(self):
        order = {
            'user_id':1,
            'pickup': 100,
            'destination': 'kireka',
            'description': 'light',
            'weight': 10,
            'product': 'parcel',
        }
        post = CreateOrder().createOrder(order)

        resp = json.loads(post.data.decode())
        self.assertEqual(resp['success'], False)
        self.assertEqual(resp['error']['message'], 'Pickup, Destination, Description and Product should be Strings')
        self.assertEqual(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)
