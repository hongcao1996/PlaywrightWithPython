from main.models.restful.WSComponents import *
import requests
import json
from jsonpath_ng import jsonpath, parse
import sys
sys.path.insert(0, ".")

wsComponents = WSComponents()
response = ""


class RestfulSubSteps():

    def initRequest(self, protocol, domain, path, method, body):
        # set uri
        uri = protocol + "://" + domain + path
        wsComponents.setUri(uri)
        # set method
        wsComponents.setMethod(method)
        # set body
        if (body != None):
            wsComponents.setBody(body)

        # log in console
        print("uri: " + wsComponents.getUri())
        print("method: " + wsComponents.getMethod())

    def setParameters(self, params):
        wsComponents.setParameters(params)
        print("params: ", wsComponents.getParameters())

    def setHeaders(self, headers):
        wsComponents.setHeaders(headers)
        print("headers: ", wsComponents.getHeaders())

    def sentRequest(self):
        method = wsComponents.getMethod().upper()
        global response
        if (method == "GET"):
            response = self.getRequest()
        elif (method == "POST"):
            response = self.postRequest()
        else:
            print("new method!!!")
        print("request: ", requests)
        print("response: ", response.text)

    # do GET request
    def getRequest(self):
        return requests.get(wsComponents.getUri(), params=wsComponents.getParameters(),
                            headers=wsComponents.getHeaders())

    # do POST request
    def postRequest(self):
        return requests.post(wsComponents.getUri(), data=wsComponents.getBody(),
                             headers=wsComponents.getHeaders())

    # get HTTP code
    def getHTTPCode(self):
        return response.status_code

    # get single value from json path
    def getSingleValueFromJsonPath(self, jsonPath):
        jsonResponse = response.json()
        jsonpath_expression = parse(jsonPath)
        match = jsonpath_expression.find(jsonResponse)
        print("match: ", match)
        return match[0].value

    #     # for multi matches
    #     # for match in jsonpath_expression.find(response):
    #     #     return match.value

    # insert values into string
    def setValueIntoText(self, stringText, values):
        for key, value in values.items():
            stringText = stringText.replace("{"+ key+ "}", value)
        return stringText
