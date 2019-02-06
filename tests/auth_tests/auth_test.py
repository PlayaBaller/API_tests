# coding: utf-8

from models.http.Auth import *
from models.http.Confirm import *
from models.http.AddChild import *
from models.http.base.BasePatient import *


def test_add_child():
    # Request #1
    auth = Auth()
    auth.send_request(payload=BasePatient.payload)

    assert auth.response.status_code == 200
    assert auth.response.json()['result']['name'] == "SMS_NOT_SEND"

    # Request #2
    confirm = Confirm()
    confirm.send_request(payload=BasePatient.payload)
    token = confirm.response.json()['sid']

    # assert token == token

    # Request #3
    # TODO Move test child entity data to separate class
    payload = {
        "patient": {
            "lastName": "Sean",
            "firstName": "Combssss33223$$$$",
            "middleName": "PDiddy",
            "birthDate": "2018-05-26",
            "sex": True,
            "isAutoPhone": True
        },
        "linkType": "6",
    }
    add_child = AddChild(token)
    add_child.send_request(payload)

    # assert add_child.response == add_child.response
