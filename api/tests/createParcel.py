from unittest import TestCase
from flask import json
from api.createOrder import CreateOrder

class TestCreateParcel(TestCase):

    def createParcel(self):

        order = {
            'user_id':1,
            'pickup': 'kampala',
            'destination': 'kireka',
            'description': 'light',
            'weight': 10,
            'product': 'parcel',
        }
        post = CreateOrder().createOrder(order)

        resp = json.loads(post.data.decode())
        self.assertEqual(resp['success'], True)
        self.assertEqual(resp['data']['product'], 'parcel')
        self.assertEqual(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 201)
