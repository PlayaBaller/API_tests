class BasePatient:
    payload = {
            'phone': '380925765675',
            'code': '7934851',
            'platform': 'PISWeb'
    }

    def __init__(self):
        pass

    def post_info(self, payload):
        return payload


