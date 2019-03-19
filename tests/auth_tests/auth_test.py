# coding: utf-8

from models.http.Send import *
from models.http.Confirm import *
from models.http.AddChild import *
from models.http.base.BasePatient import *
from models.http.base.BaseChild import *
import pytest


def test_add_child():
    # Request #1
    send = Send()
    send.send_request(payload=BasePatient.payload)

    assert send.response.status_code == 200

    # Request #2
    confirm = Confirm()
    confirm.send_request(payload=BasePatient.payload)
    token = confirm.response.json()["sid"]
    print(token)
    assert confirm.response.status_code == 200

    # Request #3
    add_child = AddChild(token)
    add_child.send_request(payload=BaseChild.payload)
    assert add_child.response.status_code == 200


@pytest.fixture()
def auth():
    send = Send()
    send.send_request(payload=BasePatient.payload)

    confirm = Confirm()
    confirm.send_request(payload=BasePatient.payload)
    token = confirm.response.json()["sid"]
    print(token)
