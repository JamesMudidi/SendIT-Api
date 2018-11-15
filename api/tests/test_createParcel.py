from unittest import TestCase
from flask import json
from api.tests.createOrder import createOrder

class createParcel(TestCase):

    def createParcel(self):

        order = {
            'user_id':1,
            'pickup': 'kampala',
            'destination': 'kireka',
            'description': 'light',
            'weight': 10,
            'product': 'parcel',
        }
        post = createOrder().createOrder(order)

        resp = json.loads(post.data.decode())
        self.assertEqual(resp['success'], True)
        self.assertEqual(resp['data']['product'], 'parcels/')
        self.assertEqual(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 201)
