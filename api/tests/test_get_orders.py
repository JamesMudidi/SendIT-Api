from unittest import TestCase
from flask import json
from api.models.model import Model
from api.tests.create_order import CreateOrder

class TestGetOrders(TestCase):

    def test_get_orders(self):
        Model.lsts.clear()
        Model.userLst.clear()

        CreateOrder().create_order({
            'user_id':1,
            'pickup': 'kampala',
            'destination': 'kireka',
            'description': 'fragile',
            'weight': 10,
            'product': 'parcel',
        })
        CreateOrder().create_order({
            'user_id':2,
            'pickup': 'kampala',
            'destination': 'kololo',
            'description': 'fragile',
            'weight': 20,
            'product': 'parcel',
        })
        CreateOrder().create_order({
            'user_id':3,
            'pickup': 'kamwokya',
            'destination': 'mengo',
            'description': 'fragile',
            'weight': 30,
            'product': 'parcel',
        })

        req = CreateOrder().client().get('/api/v1/parcels/')
        resp = json.loads(req.data.decode())
        self.assertEqual(resp['success'], True)
        self.assertEqual(len(resp['data']), 3)
        self.assertEqual(resp['data'][1]['destination'], 'mengo')
        self.assertEqual(req.status_code, 200)
