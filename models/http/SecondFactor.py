from models.http.base.BaseHttpModel import *


class SecondFactor(BaseHttpModel):
    url = 'https://qa1.helsi.me/api/healthy/accounts/ca5eca21-8048-4aea-b435-89c0d8c42dfd/secondfactor?debug=true'

    def __init__(self):
        BaseHttpModel.__init__(self)
        pass

    def send_request(self, payload):
        BaseHttpModel.send_request(self, payload, "post")
