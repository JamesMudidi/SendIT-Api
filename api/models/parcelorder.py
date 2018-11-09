""" Module for parcel orders
"""
class ParcelOrder():
    """
        class defining all methods
    """
    def __init__(self):
        self.parcelorders = []

    def add_parcel(self, user_name, email, parcel_name, pickup, destination, price                  , status,parcel_id):
        """
           Post requests
        """
        parcel_list = [order for order in self.parcelorders]

        id = len(parcel_list) + 1


        order = {
            'User_name': user_name,'email':email, 'parcel_name': parcel_name,
             'pickup': pickup, 'destination': destination,'price': price,'status':status,
            'id': id
        }
        self.parcelorders.append(order)
        return self.parcelorders

    def get_all_parcels(self):
        """
           All get requests of parcels
        """
        if not self.parcelorders:
            return True
        return self.parcelorders
        
    def get_one_parcel(self, parcel_id):
        """
           Getting single request
        """
        available_parcel_id = [
            order.__dict__ for order in self.parcelorders
            if order.__dict__['id'] == parcel_id]
        if not available_parcel_id:
            return {parcel_id:"Parcel_id doesnot exist"}
        return {'Requested order': [
            order.__dict__
            for order in self.parcelorders
            if order.__dict__['id'] == parcel_id]}