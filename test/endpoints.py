import pytest
import json
from Api import create_app
from tests import test


@pytest.fixture(scope='module')
def client():
    app = create_app('Testing')
    
    #Create a test client
    test_client = app.test_client()
    
    #Set the app client for testing
    cxt = app.app_context()
    cxt.push()
    yield test_client
    cxt.pop()


#Empty parcel order test
def test_empty_parcel_order_list(client):
    response = client.get('api/v1/parcels')
    assert b'Input a New order' in response.data


#Empty fields test
def test_post_parcel_orders_empty_fields(client):
    response = client.post('api/v1/parcels', data=json.dumps(test.empty_fields))
    assert response.status_code == 400
    assert json.loads(response.data)['error'] == 'All fields are required'


#Wrong inputs test
def test_check_invalid_fields_in_parcel_orders(client):
    response = client.post('api/v1/parcels', data=json.dumps(test.wrong_data))
    assert response.status_code == 400
    assert json.loads(response.data)['error'] == 'The parcel_name, description, destination, pickup must be Alpabetical letters'


#Blank spaces test
def test_white_spaces_in_post_parcel_orders(client):
    response = client.post('api/v1/parcels', data=json.dumps(test_data.blank_space))
    assert response.status_code == 400
    assert json.loads(response.data)['error'] == 'No blank spaces allowed'


#Accepted data test
def test_post_parcel_orders_endpoint(client):
    response = client.post('api/v1/parcels', data=json.dumps(test_data.accepted_data))
    assert response.status_code == 201
    assert json.loads(response.data)['message'] == 'Order Received'


#All orders test
def test_get_all_parcel_orders(client):
    response = client.post('api/v1/parcels', data=json.dumps(test_data.accepted_data))
    assert response.status_code == 201
    response = client.get('api/v1/parcels')
    assert response.status_code == 200
    assert json.loads(response.data)['parcel_orders'][0]['description'] == 'has two doors and checks out'


#Single order test
def test_get_single_parcel_orders(client):
    response = client.post('api/v1/parcels', data=json.dumps(test_data.accepted_data))
    assert response.status_code == 201
    response = client.get('api/v1/parcels/{}'.format(1))
    assert response.status_code == 200
    assert json.loads(response.data)['parcel_order']['parcel_id'] == 1
    
    #Invalid parcel order id test
    response = client.get('api/v1/parcels/{}'.format(4))
    assert response.status_code == 200
    assert json.loads(response.data)['message'] == 'No order found in your directory'


#Updating order status test
def test_put_order_status_endpoint(client):
    response = client.put('/api/v1/parcels/{}'.format(1), data=json.dumps({'status': 'cancel'}))
    assert response.status_code == 201
    assert json.loads(response.data)['message'] == 'Order successfully updated'


#invalid status test
def test_bad_wrong_status(client):
    response = client.put('/api/v1/parcels/{}'.format(1), data=json.dumps({'status': 'rear'}))
    assert response.status_code == 400
    assert json.loads(response.data)['error'] == 'Invalid status'
    
    #Invalid id test
    response = client.put('/api/v1/parcels/{}'.format(20), data=json.dumps({'status': 'cancel'}))
    assert response.status_code == 200
    assert json.loads(response.data)['message'] == 'you dont have such product'
