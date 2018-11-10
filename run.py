"""
   Module for running the app
"""
import os
from flask import Flask
from api.routes.urls import Urls

if __name__ == '__main__':
    Urls.fetch_urls(app)
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='127.0.0.1', port=port)
