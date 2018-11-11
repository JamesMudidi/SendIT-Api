from unittest import TestCase
from flask import json
from api.models.model import Model
from api.tests.create_order import CreateOrder

class TestNoSingleOrder(TestCase):

    def test_no_single_order(self):

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

        req = CreateOrder().client().get('/api/v1/parcels/100')
        resp = json.loads(req.data.decode())
        self.assertEqual(resp['success'], False)
        self.assertEqual(resp['error']['message'], 'Order not found')
        self.assertEqual(req.status_code, 404)
