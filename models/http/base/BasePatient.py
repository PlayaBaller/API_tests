import requests
import json
from models.http.base.BaseHttpModel import *
from models.http.AddChild import *


class BasePatient:
    payload = {
            'code': '168w8',
            'phone': '380925765675',
            'platform': 'PISWeb'
    }

    def __init__(self, payload):
        return payload


