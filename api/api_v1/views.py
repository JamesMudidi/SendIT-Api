from flask import request, jsonify
from ..api_v1 import api_v1
from ..models.parcels import ParcelOrders
from api.utilities import checks_blank_fields, check_field_types, removes_blank_spaces

@api_v1.route('/parcels', methods=['POST'])
def post_parcels():
    #Create json request
    json_data = request.get_json(force=True)

    parcel_order = ParcelOrders()
    #Check empty fields in the data
    if checks_blank_fields(json_data['parcel_name'], json_data['description'],
                           json_data['pickup'], json_data['destination']):
        return jsonify({'error': 'Some fields are blank'}), 400

    #Validates data types
    if not check_field_types(json_data['parcel_name'], json_data['description'],
                             json_data['destination'], json_data['pick_up']):
        return jsonify({'error': 'The parcel_name, description, destination, pickup must be Alphabetical letters'}), 400

    #Checks blank spaces in the field
    if removes_blank_spaces(json_data['parcel_name'],
                            json_data['description'],
                            json_data['pickup'],
                            json_data['destination']):
        return jsonify({'error': 'Some of your fields contain Blank spaces'}), 400

    #Create parcel methods
    parcel_order.create_orders(parcel_name=json_data['parcel_name'],
                               description=json_data['description'],
                               pick_up=json_data['pickup'],
                               destination=json_data['destination']
                               )
    return jsonify({'message': 'Order successfully created'}), 201
    
    #Get all parcel delivery orders
@api_v1.route('/parcels', methods=['GET'])
def get_all_parcel_orders():
    if len(parcel_orders) != 0:
        return jsonify({'parcel_orders': parcel_orders})
    else:
        return jsonify({'message': 'You dont have an orders yet'})
        
     #Get single parcel order
@api_v1.route('parcels/<int:parcel_id>', methods=['GET'])
def get_single_parcel_order(parcel_id):
    """function that fetches a single order from the list"""
    if 0 < parcel_id < len(parcel_orders):
        parcel_order = [parcel_order for parcel_order in parcel_orders if parcel_order['parcel_id'] == parcel_id]
        return jsonify({'parcel_order': parcel_order[0]}), 200
    else:
        return jsonify({'message': 'No order found in your directory'}), 200

    #Update parcel order status
@api_v1.route('parcels/<int:parcel_id>', methods=['PUT'])
def put_parcel_delivery_status(parcel_id):
    json_data = request.get_json(force=True)
    if validate_status(json_data['status']):
        return jsonify({'error': 'wrong status'}), 400
    if 0 < parcel_id < len(parcel_orders):
        delivery_order = [delivery_order for delivery_order in parcel_orders if delivery_order['parcel_id'] == parcel_id]
        delivery_order[0]['status'] = json_data['status']
        return jsonify({'message': 'Order successfully updated'}), 201
    else:
        return jsonify({'message': 'Order has not been placed'}), 200
        
