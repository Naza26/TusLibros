class Request:
    def __init__(self):
        http_method = 'GET'
        url = None
        body = {}

    def http_get_parameters(self):
        return 1

    def http_post_parameters(self, url):
        if '/createCart' in url:
            body = {'client_id': None, 'password': None}

        return body
