from unittest import TestCase
from flask import json
from api.tests.create_order import CreateOrder

class TestCreateProduct(TestCase):

    def test_create_order(self):

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
        self.assertEqual(resp['data']['product'], 'parcel')
        self.assertEqual(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 201)
