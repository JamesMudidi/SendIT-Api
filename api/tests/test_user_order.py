from unittest import TestCase
from flask import json
from api.models.model import Model
from api.tests.create_order import CreateOrder

class TestUserOrder(TestCase):

    def test_user_order(self):
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
            'user_id':1,
            'pickup': 'kampala',
            'destination': 'kololo',
            'description': 'fragile',
            'weight': 20,
            'product': 'parcel',
        })
        CreateOrder().create_order({
            'user_id':2,
            'pickup': 'kamwokya',
            'destination': 'mengo',
            'description': 'fragile',
            'weight': 30,
            'product': 'Parcels',
        })

        req = CreateOrder().client().get('/api/v1/users/2/parcels/')
        resp = json.loads(req.data.decode())
        self.assertEqual(resp['success'], True)
        self.assertEqual(resp['data'][0]['product'], 'Parcels')
        self.assertEqual(req.status_code, 200)
