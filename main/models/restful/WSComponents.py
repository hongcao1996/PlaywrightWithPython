class WSComponents:
    # contructors
    def __init__(self):
        self._uri = ""
        self._method = ""
        self._body = ""
        self._headers = None
        self._parameters = None

    def getUri(self):
        return self._uri

    def setUri(self, uri):
        self._uri = uri

    def getMethod(self):
        return self._method

    def setMethod(self, method):
        self._method = method

    def getBody(self):
        return self._body

    def setBody(self, body):
        self._body = body

    def getHeaders(self):
        return self._headers

    def setHeaders(self, headers):
        self._headers = headers

    def getParameters(self):
        return self._parameters

    def setParameters(self, parameters):
        self._parameters = parameters
