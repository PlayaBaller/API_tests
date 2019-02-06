import requests
import json
from models.http.base.BaseHttpModel import *
from models.http.AddChild import *


class Patient(BaseHttpModel):
    payload = {
        'phone': '380925765675',
        'platform': 'PISWeb'
    }

    def __init__(self, payload):
        pass
