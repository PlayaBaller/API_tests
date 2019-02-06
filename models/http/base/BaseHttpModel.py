import requests
import json


class BaseHttpModel:
    url = None
    token = None
    headers = {
        'Content-Type': 'application/json;charset=UTF-8'
    }
    response = None

    def __init__(self, token=None):
        if token is not None:
            self.token = token
            self.headers = {
                'Content-Type': 'application/json;charset=UTF-8',
                'Authorization': 'Bearer ' + str(self.token)
            }
        pass

    def send_request(self, payload, method="get"):
        if method == "get":
            self.response = requests.get(
                self.url,
                # data=json.JSONEncoder().encode(payload),
                headers=self.headers
            )
        elif method == "post":
            self.response = requests.post(
                self.url,
                data=json.JSONEncoder().encode(payload),
                headers=self.headers
            )
        else:
            # TODO Add error handler
            return None

        # TODO Move to Log class
        print("\nPOST " + self.url)
        print("Headers: " + str(self.headers))
        print("Payload: " + str(payload))
        print("Status code: " + str(self.response.status_code))
        print("Response: " + self.response.text + "\n----------------------------\n")
