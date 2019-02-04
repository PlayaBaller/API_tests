from models.http.base.BaseHttpModel import *


class AddChild(BaseHttpModel):
    url = 'https://qa1.helsi.me/api/healthy/patients'

    def __init__(self, token=None):
        BaseHttpModel.__init__(self, token)
        pass

    def send_request(self, payload):
        BaseHttpModel.send_request(self, payload, "post")
