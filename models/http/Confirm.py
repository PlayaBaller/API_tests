from models.http.base.BaseHttpModel import *


class Confirm(BaseHttpModel):
    url = 'https://qa1.helsi.me/api/healthy/confirm'

    def __init__(self):
        BaseHttpModel.__init__(self)
        pass

    def send_request(self, payload):
        BaseHttpModel.send_request(self, payload, "post")
