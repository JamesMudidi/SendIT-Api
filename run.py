from flask import Flask
from api.config import config
from api.config.routes import routes

class Loader:
    @staticmethod
    def create_app(env_name):

        #app initiliazation
        app = Flask(__name__)
        app.config.from_object(config.APP_CONFIG[env_name])

        #Directing to Routes
        routes.fetch_routes(app)

        return app

APP = Loader.create_app('development')

if __name__ == '__main__':
    APP.run(port=5000)
