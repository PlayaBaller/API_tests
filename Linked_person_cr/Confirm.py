import requests
import json


class Confirm:
    url = 'https://qa1.helsi.me/api/healthy/confirm'
    headers = {
        'Content-Type': 'application/json;charset=UTF-8'
    }
    response = None

    def __init__(self):
        pass

    def send_request(self, payload):
        self.response = requests.post(
            self.url,
            data=json.JSONEncoder().encode(payload),
            headers=self.headers
        )