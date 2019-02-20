from models.http.base.BaseHttpModel import *


class Login(BaseHttpModel):
    url = 'https://qa1.helsi.me/api/healthy/accounts/login'

    def __init__(self):
        BaseHttpModel.__init__(self)
        pass

    def send_request(self, payload):
        BaseHttpModel.send_request(self, payload, "post")
