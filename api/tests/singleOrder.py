from unittest import TestCase
from api.tests.createOrder import CreateOrder
from flask import json
from api.models.model import Model

class singleOrder(TestCase):
    ### Class that return the test results for getting all orders ###
    def singleOrder(self):
       ### Method for testing endpoint of getting all orders ###
        Model.lsts.clear()
        Model.userLst.clear()
        
        CreateOrder().createOrder({
            'user_id':1,
            'pickup': 'kampala',
            'destination': 'kireka',
            'description': 'light',
            'weight': 10,
            'product': 'parcel',
        })
        CreateOrder().createOrder({
            'user_id':2,
            'pickup': 'kampala',
            'destination': 'kololo',
            'description': 'heavy',
            'weight': 20,
            'product': 'box',
        })
        CreateOrder().createOrder({
            'user_id':3,
            'pickup': 'kamwokya',
            'destination': 'mengo',
            'description': 'fragile',
            'weight': 30,
            'product': 'crate',
        })

        req = CreateOrder().client().get('/parcels/1')
        resp = json.loads(req.data.decode())
        self.assertEqual(resp['success'], True)
        self.assertEqual(resp['data']['destination'], 'kireka')
        self.assertEqual(req.status_code, 200)
