# coding: utf-8

from models.http.Send import *
from models.http.Confirm import *
from models.http.AddChild import *
from models.http.base.BasePatient import *
from models.http.base.BaseChild import *


def test_add_child():
    # Request #1
    send = Send()
    send.send_request(payload=BasePatient.post_login)

    assert send.response.status_code == 200

    # Request #2
    confirm = Confirm()
    confirm.send_request(payload=BasePatient.post_login)
    assert confirm.response.status_code == 200

    # Request #4
#    token = second_factor.response.json(['sid'])
#    add_child = AddChild(token)
#    add_child.send_request(payload=BaseChild.payload)
#    assert add_child.response.status_code == 200
