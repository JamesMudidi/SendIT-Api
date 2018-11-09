"""
    Module for making tests on the application
"""
import unittest
import json
from run import APP

class TestViews(unittest.TestCase):
    """"
        Class for making tests
        params: unittest.testCase
    """

    def setUp(self):
        """
           Creating a client object
        """
        self.client = APP.test_client

    def test_make_a_parcel(self):
        """
            Test for post function which posts a parcel order
        """
        result = self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(dict(parcel_id=1, user_name="James",email="mudidi.jimmy@gmail.com", parcel_name="chair", pickup_location="Kampala",destination="kampala", price =10000 ,
                                                         )))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Parcel_orders', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 201)
        self.assertTrue(result.json["Parcel_orders"])

    def test_missing_field(self):
        """
            Test for missing field in the post function
        """
        result = self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(dict(parcel_id=18, user_name="James",email="mudidi.jimmy@gmail.com", parcel_name="chair", pickup="Kampala"  
                                                         )))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Blank space', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
    def test_wrong_email_address(self):
        """
            Test for wrong email in the post function
        """
        result = self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(dict(parcel_id=18, user_name="James",email="", parcel_name="chair", pickup="Kampala"  
                                                         )))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Blank space', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
    def test_fetch_all_parcels(self):
        """
           Test for get function which returns all parcel orders
        """
        result = self.client().get('api/v1/parcels')
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 200)
        self.assertIn('Parcels', respond)
        self.assertIsInstance(respond, dict)
    def test_get_a_Parcel(self):
        """
            Test for get function which returns only one parcel order
        """
        result = self.client().get('api/v1/parcels/17')
        result2 = self.client().get('api/v1/parcels/a')
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result2.status_code, 404)
        self.assertIsInstance(respond, dict)
        

