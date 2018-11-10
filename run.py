"""
   Module for running the app
"""
from flask import Flask
from api.routes.urls import Urls
app = Flask(__name__)
Urls.fetch_urls(APP)
if __name__ == '__main__':
    app.run()
    
