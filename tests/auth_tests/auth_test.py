# coding: utf-8

from models.http.Send import *
from models.http.Confirm import *
from models.http.AddChild import *
from models.http.base.BasePatient import *
from models.http.base.BaseChild import *
import pytest


"""def test_add_child():
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
"""


@pytest.fixture()
def config_child_name():
    payload = {
        "patient": {
            "lastName": "Hustler",
            "firstName": "BALLERKilleR",
            "middleName": "Balfgfdgffffededff",
            "birthDate": "2009-05-25",
            "sex": True,
            "isAutoPhone": True
        },
        "linkType": "6",
    }
    return payload


def test_add_child(config_child_name):
    send = Send()
    send.send_request(payload=BasePatient.payload)

    confirm = Confirm()
    confirm.send_request(payload=BasePatient.payload)
    token = confirm.response.json()["sid"]
    print(token)
    assert confirm.response.status_code == 200

    add_child = AddChild(token)
    add_child.send_request(payload=config_child_name)
    assert add_child.response.status_code == 200



