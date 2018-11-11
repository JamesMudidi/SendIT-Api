from flask import Blueprint

#Blueprint for app
api_v1 = Blueprint('api_v1', __name__)
from api_v1 import views.py
