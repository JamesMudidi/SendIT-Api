from unittest import TestCase
from flask import json
from api.models.model import Model
from api.tests.createOrder import createOrder

class cancelOrder(TestCase):
    ### Canceling orders test results ###
    def cancel_order(self):
        Model.lsts.clear()
        Model.userLst.clear()

        createOrder().create_order({
            'user_id':1,
            'pickup': 'kampala',
            'destination': 'kireka',
            'description': 'light',
            'weight': 10,
            'product': 'parcel',
        })
        
        createOrder().create_order({
            'user_id':2,
            'pickup': 'kampala',
            'destination': 'kololo',
            'description': 'heavy',
            'weight': 20,
            'product': 'box',
        })
        
        createOrder().create_order({
            'user_id':3,
            'pickup': 'kamwokya',
            'destination': 'mengo',
            'description': 'fragile',
            'weight': 30,
            'product': 'crate',
        })

        req = create_order().client().put('/parcels/1/cancel/')
        resp = json.loads(req.data.decode())
        self.assertEqual(resp['success'], True)
        self.assertEqual(resp['data']['status'], 'cancelled')
        self.assertEqual(req.status_code, 200)
