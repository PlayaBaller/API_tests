class BasePatient:
    payload = {
            'phone': '380925765675',
            'code': 'r9281',
            'platform': 'PISWeb'
    }

    def __init__(self):
        pass

    def pass_info(self, payload):
        return payload
# TODO add separate from __init__ method for passing payload dict data

