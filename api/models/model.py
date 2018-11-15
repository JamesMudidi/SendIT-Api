from flask import jsonify

class Model:
    ### Add data ###
    lsts = []
    userLst = []

    def getOrder(self, order_id=None):
        ### Get data ###
        if order_id is None:
            return jsonify({"success":True, "data":Model.lsts}), 200
        for order in Model.lsts:
            if order.get('order_id') == order_id:
                return jsonify({"success":True, "data":order}), 200
        return jsonify({"success":False, "error":{"message": "Order not found"}}), 404

    def userOrder(self, user_id):
        ### Get data posted by a specific user ###
        for order in Model.lsts:
            if order.get('user_id') == user_id:
                Model.userLst.append(order)
            else:
                Model.userLst.clear()
        if len(Model.userLst) > 0:
            return jsonify({"success":True, "data":Model.userLst}), 200
        return jsonify({"success":False, "error":{"message": "Order not found"}}), 404


    def cancelOrder(self, order_id):
        ### Cancel order ###
        for order in Model.lsts:
            if order.get('order_id') == order_id:
                order['status'] = 'cancelled'
                return jsonify({"success":True, "data":order}), 200
        return jsonify({"success":False, "error":{"message": "Order canceled"}}), 404

    def createOrder(self, order):
        ### Add an order ###
        Model.lsts.append(order)
        return jsonify({"success":True, "data":order}), 201
