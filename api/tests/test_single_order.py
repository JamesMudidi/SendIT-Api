from unittest import TestCase
from api.tests.create_order import CreateOrder
from flask import json
from api.models.model import Model

class TestSingleOrder(TestCase):
    """
    Class that return the test results for getting all orders
    """
    def test_single_order(self):
        """
        Method for testing endpoint of getting all orders
        """
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

        req = CreateOrder().client().get('/api/v1/parcels/1')
        self.assertEqual(resp['success'], True)
        self.assertEqual(resp['data']['destination'], 'kireka')
        self.assertEqual(req.status_code, 200)
