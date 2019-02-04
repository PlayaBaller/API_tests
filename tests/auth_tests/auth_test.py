# coding: utf-8

from models.http.Auth import *
from models.http.Confirm import *
from models.http.AddChild import *


def test_add_child():
    # Request #1
    payload = {
        'code': '060z2',
        'phone': '380925765675',
        'platform': 'PISWeb'
    }
    auth = Auth()
    auth.send_request(payload=payload)

    assert auth.response.status_code == 200

    # Request #2
    payload = {
        'code': auth.response.json()['debug']['code'],
        'phone': "380925765675",
        'personalDataStatusWeb': None,
        'platform': "PISWeb"
    }
    confirm = Confirm()
    confirm.send_request(payload=payload)
    token = confirm.response
    print(confirm.response)
    token = token.json()['sid']
    print(token)

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
    print(add_child.response)

    # assert add_child.response == add_child.response
