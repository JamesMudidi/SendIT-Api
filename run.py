""" Module for running the app """
from api import create_app

app = create_app('development')
if __name__ == '__main__':
    app.run(debug=True)
