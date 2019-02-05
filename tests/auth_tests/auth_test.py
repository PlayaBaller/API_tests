# coding: utf-8

from models.http.Auth import *
from models.http.Confirm import *
from models.http.AddChild import *


def test_add_child():
    # Request #1
    payload = {
        'phone': '380925765675',
        'platform': 'PISWeb'
    }
    auth = Auth()
    auth.send_request(payload=payload)

    assert auth.response.status_code == 200
    assert auth.response.json()['result']['name'] == "SMS_NOT_SEND"

    # Request #2
    payload = {
        'code': '683J2',
        'phone': "380925765675",
        'platform': "PISWeb"
        # 'personalDataStatusWeb': None,
    }
    confirm = Confirm()
    confirm.send_request(payload=payload)
    token = confirm.response.json()['sid']

    # assert token == token

    # Request #3
    payload = {
        "patient": {
            "lastName": "O'sheaaa",
            "firstName": "Jacksonssffdfa",
            "middleName": "BallHustlaPlayaStunna323245777",
            "birthDate": "2018-05-27",
            "sex": True,
            "isAutoPhone": True
        },
        "linkType": "6",
    }
    add_child = AddChild(token)
    add_child.send_request(payload)

    # assert add_child.response == add_child.response
