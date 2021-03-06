from unittest import TestCase
from flask import json
from api.models.model import Model
from api.tests.create_order import CreateOrder

class TestCancelOrder(TestCase):
    """ Canceling orders test results  """
    def test_cancel_order(self):
        Model.lsts.clear()
        Model.userLst.clear()

        CreateOrder().create_order({
            'user_id':1,
            'pickup': 'kampala',
            'destination': 'kireka',
            'description': 'light',
            'weight': 10,
            'product': 'parcel',
        })
        CreateOrder().create_order({
            'user_id':2,
            'pickup': 'kampala',
            'destination': 'kololo',
            'description': 'heavy',
            'weight': 20,
            'product': 'box',
        })
        CreateOrder().create_order({
            'user_id':3,
            'pickup': 'kamwokya',
            'destination': 'mengo',
            'description': 'fragile',
            'weight': 30,
            'product': 'crate',
        })

        req = CreateOrder().client().put('/api/v1/parcels/1/cancel/')
        self.assertEqual(resp['success'], True)
        self.assertEqual(resp['data']['status'], 'cancelled')
        self.assertEqual(req.status_code, 200)
