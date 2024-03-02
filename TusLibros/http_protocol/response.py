class Response:
    OK_RESPONSE = 200
    BAD_REQUEST_RESPONSE = 400

    def __init__(self, status_code, body, headers=None):
        self._status_code = status_code
        self._headers = headers
        self._body = body

    def is_successful(self):
        return self._status_code == self.OK_RESPONSE

    def is_bad_request(self):
        return self._status_code == self.BAD_REQUEST_RESPONSE

    def failed_with_message(self, message):
        return self._body['errors'].split("|")[1] == message

    def content(self):
        return self._body['objects']
