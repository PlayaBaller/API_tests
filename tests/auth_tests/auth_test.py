# coding: utf-8

from models.http.Send import *
from models.http.Confirm import *
from models.http.AddChild import *
from models.http.base.BasePatient import *
from models.http.base.BaseChild import *
import pytest

"""  # Test scope before implementing fixtures with test data 
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
"""


@pytest.fixture()
def config_base_user():
    payload = {
        'code': '0599042',
        'phone': '380925765675',
        'platform': 'PISWeb'
    }
    return payload


def test_auth_config_base_user(config_base_user):  # passing fixture function as an attribute to test function
    send = Send()
    send.send_request(payload=config_base_user)

    confirm = Confirm()
    confirm.send_request(payload=config_base_user)  # passing fixture function data to send request method (instead data from BasePatient class)
    token = confirm.response.json()["sid"]
    print(token)
    assert confirm.response.status_code == 200


@pytest.fixture()
def config_child_name():
    payload = {
        "patient": {
            "lastName": "2chainz111",
            "firstName": "Hairwavezzkillerzzxxsxscvcv",
            "middleName": "22222chainzzzz",
            "birthDate": "2009-05-25",
            "sex": True,
            "isAutoPhone": True
        },
        "linkType": "6",
    }
    return payload


def test_add_child(config_child_name):  # passing fixture function as an attribute to test function
    send = Send()
    send.send_request(payload=BasePatient.payload)

    confirm = Confirm()
    confirm.send_request(payload=BasePatient.payload)
    token = confirm.response.json()["sid"]
    print(token)
    assert confirm.response.status_code == 200

    add_child = AddChild(token)
    add_child.send_request(payload=config_child_name)  # passing fixture function data to send request method
    assert add_child.response.status_code == 200
