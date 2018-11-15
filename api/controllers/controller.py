from flask import request
from flask.views import MethodView
from api.models.model import Model
from api.config.validation import validation

class Controller(MethodView):

    def __init__(self):
        ### Initialise model object ###
        self.parcel = Model()

    def post(self):
        ### Add data ###
        post_data = request.get_json()
        value = validation(post_data).validate()

        if isinstance(value, bool):
            data = {
                'order_id': len(self.parcel.lsts) + 1,
                'user_id': post_data['user_id'],
                'pickup': post_data['pickup'],
                'destination': post_data['destination'],
                'description': post_data['description'],
                'weight': post_data['weight'],
                'product': post_data['product'],
                'status': 'in-transit'
            }
            return self.parcel.createOrder(data)
        return value

    def get(self, parcel_id=None, user_id=None):
        ### Retrieve data ###
        if parcel_id is None and user_id is None:
            return self.parcel.getOrder()
        if user_id is None:
            return self.parcel.getOrder(parcel_id)
        return self.parcel.userOrder(user_id)

    def put(self, parcel_id):
        ### Update data in ###
        return self.parcel.cancelOrder(parcel_id)
