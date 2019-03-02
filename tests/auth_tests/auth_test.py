# coding: utf-8

from models.http.Login import *
from models.http.Password import *
from models.http.SecondFactor import *
from models.http.Confirm import *
from models.http.AddChild import *
from models.http.base.BasePatient import *
from models.http.base.BaseChild import *


def test_add_child():
    # Request #1
    login = Login()
    login.send_request(payload=BasePatient.payload_login)

    assert login.response.status_code == 200

    # Request #2
    password = Password()
    password.send_request(payload=BasePatient.payload_pass)
    assert password.response.status_code == 202

    # Request #3
    second_factor = SecondFactor()
    second_factor.send_request(payload=BasePatient.payload_pass)
    assert second_factor.response.status_code == 200

    # Request #4
#    token = second_factor.response.json(['sid'])
#    add_child = AddChild(token)
#    add_child.send_request(payload=BaseChild.payload)
#    assert add_child.response.status_code == 200
