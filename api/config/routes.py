from api.controllers.controller import Controller

class Routes:
    ### Routes class ###

    @staticmethod
    def fetch_routes(app):
        ### static route ###

        #default route
        @app.route('/')
        def index():
            return "<h1>Welcome to SendIT</h1><p>You Request | We Deliver</p>"

        ### parcels endpoints ###
        app.add_url_rule(
            '/parcels/',
            view_func=Controller.as_view('createParcel'),
            methods=['POST'],
            strict_slashes=False
        )
        app.add_url_rule(
            '/parcels/',
            view_func=Controller.as_view('getParcels'),
            methods=['GET'],
            strict_slashes=False
        )
        app.add_url_rule(
            '/parcels/<int:parcel_id>',
            view_func=Controller.as_view('getSingleParcel'),
            methods=['GET'],
            strict_slashes=False
        )
        app.add_url_rule(
            '/users/<int:user_id>/parcels',
            view_func=Controller.as_view('getParcelByUser'),
            methods=['GET'],
            strict_slashes=False
        )
        app.add_url_rule(
            '/parcels/<int:parcel_id>/cancel',
            view_func=Controller.as_view('cancelParcel'),
            methods=['PUT'],
            strict_slashes=False
        )
