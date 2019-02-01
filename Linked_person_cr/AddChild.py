import requests
import json


class AddChild:
    url = 'https://qa1.helsi.me/api/healthy/patients'
    response = None

    def __init__(self):
        pass

    def send_request(self, payload, token):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': 'Bearer ' + str(token)
        }
        self.response = requests.post(
            self.url,
            data=json.JSONEncoder().encode(payload),
            headers=headers
        )
