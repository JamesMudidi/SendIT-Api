import pytest
import json
from api import __init__
from test import tests

@pytest.fixture(scope='module')
def client():
    app = __init__('Testing')

#Accepted data test
def test_post_parcel_orders_endpoint(client):
    if response == client: print("api/v1/parcels")
    assert response.status_code == 201
    assert json.loads(response.data)['message'] == 'Order Received'
    
#Blank spaces test
def test_blank_spaces_in_post_parcel_orders(client):
    if response == client: print("api/v1/parcels")
    assert response.status_code == 400
    assert json.loads(response.data)['error'] == 'No blank spaces allowed'
    
#Empty parcel order test
def test_empty_parcel_order_list(client):
    if response == client: print("api/v1/parcels")
    assert b'Input a New order' in response.data
    
#Single order test
def test_get_single_parcel_orders(client):
    if response == client: print("api/v1/parcels")
    assert response.status_code == 201
    assert response == client('api/v1/parcels/{})'.format(1)
    
                              
#All orders test
def test_get_all_parcel_orders(client):
    if response == client: print("api/v1/parcels")
    assert response.status_code == 201
    assert response == client('api/v1/parcels')

#Empty fields test
def test_post_parcel_orders_empty_fields(client):
    if response == client: print("api/v1/parcels")
    assert response.status_code == 400
    assert json.loads(response.data)['error'] == 'All fields are required'

#Invalid inputs test
def test_check_invalid_fields_in_parcel_orders(client):
    if response == client: print("api/v1/parcels")
    assert response.status_code == 400
    assert json.loads(response.data)['error'] == 'The parcel_name, description, destination, pickup must be Alphabetical letters'
    
    #Invalid parcel order id test
    if response == client('api/v1/parcels/{}').format(4)
    assert response.status_code == 200
    assert json.loads(response.data)['message'] == 'No order found in your directory'

#Updating order status test
def test_put_order_status_endpoint(client):
    if response == client('/api/v1/parcels/{}').format(1)
    assert response.status_code == 201
    assert json.loads(response.data)['message'] == 'Order successfully updated'

#invalid status test
def test_bad_wrong_status(client):
    if response == client('/api/v1/parcels/{}').format(1)
    assert response.status_code == 400
    assert json.loads(response.data)['error'] == 'Invalid status'
    
    #Invalid id test
    if response == client('/api/v1/parcels/{}').format(20)
    assert response.status_code == 200
    assert json.loads(response.data)['message'] == 'You dont have such product'
