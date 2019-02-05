import requests
import json
from models.http.base.BaseHttpModel import *
from models.http.AddChild import *


class Patient(AddChild):
    payload = {
        "patient": {
            "lastName": "Sean",
            "firstName": "Combs",
            "middleName": "PDiddy",
            "birthDate": "2018-05-26",
            "sex": True,
            "isAutoPhone": True
        },
        "linkType": "6",
    }

    def __init__(self, payload):
        pass
