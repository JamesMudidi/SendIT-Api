from unittest import TestCase
from flask import json
from run import APP

class TestView(TestCase):

    ### TestCase for TDD ###
    def setUp(self):
        ### Flask object initiate ###
        self.app = APP
        self.client = self.app.test_client
        self.client().post(
            '/auth/signup',
            data=json.dumps(dict(
                username='james',
                email='mudidi.jimmy@gmail.com',
                password='test'
            )),
            content_type='application/json'
        )

        login = self.client().post(
            '/auth/login',
            data=json.dumps(dict(
                username='james',
                password='test'
            )),
            content_type='application/json'
        )

    def test_create_order(self):
        ### Create order ##
        post = self.client().post(
            '/parcels',
            data=json.dumps(dict(
                pickup='Kampala',
                destination='Kireka',
                description='box',
                weight=10,
                product='crate',
            )),
            content_type='application/json',
        )

        resp = json.loads(post.data)
        self.assertEqual(resp['data']['status'], 'pending')
        self.assertEqual(resp['success'], True)
        self.assertEqual(post.status_code, 201)

    def test_int_error(self):
        ### Integers ###
        post = self.client().post(
            '/parcels',
           data=json.dumps(dict(
                pickup='Kampala',
                destination='Kireka',
                description='box',
                weight=10,
                product='crate',
            )),
            content_type='application/json',
        )

        resp = json.loads(post.data)
        self.assertEqual(resp['success'], False)
        self.assertEqual(resp['error']['message'], 'Weight is an integer')
        self.assertEqual(post.status_code, 400)

    def test_string_error(self):
        ### String errors ###
        post = self.client().post(
            '/parcels',
            data=json.dumps(dict(
                pickup='Kampala',
                destination='Kireka',
                description='parcel',
                weight=15,
                product=1,
            )),
            content_type='application/json',
        )

        resp = json.loads(post.data)
        self.assertEqual(resp['success'], False)
        self.assertEqual(resp['error']['message'], 'Description, Destination, Pickup, and Product should be a strings')
        self.assertEqual(post.status_code, 400)

    def test_empty_error(self):
        ### Blank fields ###
        post = self.client().post(
            '/parcels',
            data=json.dumps(dict(
                pickup='Kampala',
                destination='',
                description='Parcel',
                weight=12,
                product='crate',
            )),
            content_type='application/json',
        )

        resp = json.loads(post.data)
        self.assertEqual(resp['success'], False)
        self.assertEqual(resp['error']['message'], 'All fields are required')
        self.assertEqual(post.status_code, 400)

    def test_key_error(self):
        ### Missing fields ###
        post = self.client().post(
            '/parcels',
            data=json.dumps(dict(
                pickup='Kampala',
                destination='',
                description='parcel',
                weight=8,
            )),
            content_type='application/json',
        )

        resp = json.loads(post.data)
        self.assertEqual(resp['success'], False)
        self.assertEqual(resp['error']['message'], 'Fields missing')
        self.assertEqual(post.status_code, 400)

    def test_content_error(self):
        ### Missing content ###
        post = self.client().post(
            '/parcels',
            data=json.dumps(dict(
                pickup='Kampala',
                destination='',
                description='parcel',
                weight=15,
            )),
            content_type='application/javascript',
        )

        resp = json.loads(post.data)
        self.assertEqual(resp['success'], False)
        self.assertEqual(resp['error']['message'], 'Jason required')
        self.assertEqual(post.status_code, 400)

    def test_get_orders(self):
        ### Get orders ###
        post = self.client().get(
            '/parcels',
            content_type='application/json',
        )

        resp = json.loads(post.data)
        self.assertEqual(resp['success'], True)
        self.assertEqual(post.status_code, 200)

    def test_single_order(self):
        ### single error ###
        post = self.client().get(
            '/parcels/1',
            content_type='application/json',
        )

        resp = json.loads(post.data)
        self.assertEqual(resp['success'], False)
        self.assertEqual(post.status_code, 404)

    def test_user_order(self):
        ### User order ###
        post = self.client().get(
            '/users/1/parcels',
            content_type='application/json',
        )

        resp = json.loads(post.data)
        self.assertEqual(resp['success'], False)
        self.assertEqual(post.status_code, 404)

    def test_cancel_order(self):
        ### cancel order ###
        post = self.client().put(
            '/parcels/1/cancel',
            content_type='application/json',
        )

        resp = json.loads(post.data)
        self.assertEqual(resp['success'], False)
        self.assertEqual(post.status_code, 404)
