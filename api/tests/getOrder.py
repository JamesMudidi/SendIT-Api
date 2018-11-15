from unittest import TestCase
from flask import json
from api.models.model import Model
from api.createOrder import CreateOrder

class GetOrders(TestCase):

    def getOrders(self):
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

        req = CreateOrder().client().get('/parcels/')
        resp = json.loads(req.data.decode())
        self.assertEqual(resp['success'], True)
        self.assertEqual(len(resp['data']), 3)
        self.assertEqual(resp['data'][1]['destination'], 'kololo')
        self.assertEqual(req.status_code, 200)
