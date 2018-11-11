from api.utilities import serial_generator

parcel_orders = []

class ParcelOrders:
    """class responsible for creating the parcel orders"""

    def __init__(self):
        pass

    def create_orders(self, parcel_name, description, pickup, destination):
        str_price = str(0)
        """function creates the parcel order list """
        serial = serial_generator()
        parcel_order = {
            'parcel_id': len(parcel_orders) + 1,
            'parcel_name': parcel_name,
            'description': description,
            'pickup': pickup,
            'destination': destination,
            'status': "pending",
            'serial_no': serial,
            "delivery_price": str_price+"UGX"
        }
        parcel_orders.append(parcel_order)
        return parcel_orders
