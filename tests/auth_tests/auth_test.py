# coding: utf-8

from models.http.Auth import *
from models.http.Confirm import *
from models.http.AddChild import *
from models.http.base.BasePatient import *
from models.http.base.BaseChild import *

#TODO Add fixtures


def test_add_child():
    # Request #1
    auth = Auth()
    auth.send_request(payload=BasePatient.payload)

    assert auth.response.status_code == 200
    assert auth.response.json()['result']['name'] == "SMS_NOT_SEND"

    # Request #2
    confirm = Confirm()
    confirm.send_request(payload=BasePatient.payload)
    token = confirm.response.json()["sid"]

    # Request #3
    add_child = AddChild(token)
    add_child.send_request(payload=BaseChild.payload)

    assert add_child.response.status_code == 200
