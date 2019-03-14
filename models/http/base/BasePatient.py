class BasePatient:
    payload = {
            'code': '0599042',
            'phone': '380925765675',
            'platform': 'PISWeb'
    }

    def __init__(self):
        pass

    def post_login(self, payload):
        return payload




