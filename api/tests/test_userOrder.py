from unittest import TestCase
from flask import json
from api.models.model import Model
from api.tests.test_createOrder import createOrder

class userOrder(TestCase):

    def userOrder(self):
        Model.lsts.clear()
        Model.userLst.clear()

        createOrder().createOrder({
            'user_id':1,
            'pickup': 'kampala',
            'destination': 'kireka',
            'description': 'light',
            'weight': 10,
            'product': 'parcel',
        })
        
        createOrder().createOrder({
            'user_id':2,
            'pickup': 'kampala',
            'destination': 'kololo',
            'description': 'heavy',
            'weight': 20,
            'product': 'box',
        })
        
        createOrder().createOrder({
            'user_id':3,
            'pickup': 'kamwokya',
            'destination': 'mengo',
            'description': 'fragile',
            'weight': 30,
            'product': 'crate',
        })

        req = createOrder().client().get('/users/2/parcels/')
        resp = json.loads(req.data.decode())
        self.assertEqual(resp['success'], True)
        self.assertEqual(resp['data'][0]['product'], 'crate')
        self.assertEqual(req.status_code, 200)
