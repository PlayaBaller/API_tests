# coding: utf-8
import requests
import json
import token
import pytest

from modules import Auth
from modules import Confirm
from modules import AddChild

base_url = 'https://qa1.helsi.me/'


# 1

payload = {
    'phone': '380925765675',
    'platform': 'PISWeb'
}
auth = Auth()
auth.send_request(payload=payload)
print(auth.response)


# 2


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


def test_confirm():
    assert token == token

# Request #3


payload = {
    "patient": {
        "lastName": "O'sheaaa",
        "firstName": "Jacksonssa",
        "middleName": "BallHustlaPlayaStunna323245777",
        "birthDate": "2018-05-27",
        "sex": True,
        "isAutoPhone": True
    },
    "linkType": "6",
}
add_child = AddChild()
add_child.send_request(payload, token)
print(add_child.response)


def test_add_child():
    assert add_child.response == add_child.response