# coding: utf-8

from models.http.Login import *
from models.http.Password import *
from models.http.SecondFactor import *
from models.http.AddChild import *
from models.http.base.BasePatient import *
from models.http.base.BaseChild import *

# TODO Add fixtures


def test_add_child():
    # Request #1
    login = Login()
    login.send_request(payload=BasePatient.payload_login)

    assert login.response.status_code == 200
    assert login.response.json()['result']['name'] == "SMS_NOT_SEND"

    # Request #2
    password = Password()
    password.send_request(payload=BasePatient.payload_pass)
#   token = password.response.json()["sid"]

#   TODO Refactor all requests and add third and fourth requests SecondFactor && AddChild
    # Request 4
#    add_child = AddChild(token)
#    add_child.send_request(payload=BaseChild.payload)

#    assert add_child.response.status_code == 200
