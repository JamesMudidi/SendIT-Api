from flask import Blueprint

#Blueprint for app
api_v1 = Blueprint('api_v1', __name__)
import sys
sys.path.insert(0, r'/SendIT-Api/api/api_v1')
