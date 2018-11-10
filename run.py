from flask import Flask
from api.routes.urls import Urls
app = Flask(__name__)
Urls.fetch_urls(app)
if __name__ == '__main__':
   
   if port == 5000:
        app.debug = True
   
   app.run(host='127.0.0.1', port=port)
