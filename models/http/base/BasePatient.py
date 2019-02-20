class BasePatient:
    payload_login = {
            'phone': '380925765675',
            'platform': 'PISWeb'
    }

    payload_pass = {
        "phone": "380925765675",
        "password": "7934851fF",
        "isRestoredPassword": "false",
        "isRegisteredWithoutPassword": "false",
        "platform": "PISWeb"
    }

    def __init__(self):
        pass

    def post_login(self, payload_login):
        return payload_login

    def post_pass(self, payload_pass):
        return payload_pass


