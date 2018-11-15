from unittest import TestCase
from api.tests.test_createOrder import createOrder
from flask import json
from api.models.model import Model

class noUserOrder(TestCase):

    def noUserOrder(self):
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

        req = createOrder().client().get('/users/1/parcels/')
        resp = json.loads(req.data.decode())
        self.assertEqual(resp['success'], False)
        self.assertEqual(resp['error']['message'], 'Order not found')
        self.assertEqual(req.status_code, 404)
