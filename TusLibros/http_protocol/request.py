class Request:
    HTTP_GET_METHOD = 'GET'
    HTTP_POST_METHOD = 'POST'

    def __init__(self, http_method, url, body):
        self.http_method = http_method
        self.url = url
        self.body = body

    def http_post_parameters_for(self, url):
        return self.body
