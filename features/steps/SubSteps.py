from jsonpath_ng import parse
import sys
sys.path.insert(0, ".")
from main.models.restful.WSComponents import *
from typing import Generator
import pytest
import playwright
from playwright.sync_api import Playwright, APIRequestContext, expect

# @pytest.fixture(scope="session")
# def api_request_context(
#     playwright: Playwright,
# ) -> Generator[APIRequestContext, None, None]:
#     request_context = playwright.request.new_context()
#     yield request_context
#     request_context.dispose()
api_request_context = playwright.request.new_context()
# from playwright.sync_api import sync_playwright
# with sync_playwright() as p:
#     api_request_context = p.request.new_context()

wsComponents = WSComponents()
response = ""
# context = None


class SubSteps():

    def initRequest(self, protocol, domain, path, method, body) -> None:
        # set uri
        uri = protocol + "://" + domain + path
        wsComponents.setUri(uri)
        # set method
        wsComponents.setMethod(method)
        # set body
        if (body != None):
            wsComponents.setBody(body)

        # log in console
        print("")
        print("uri: " + wsComponents.getUri())
        print("method: " + wsComponents.getMethod())

    def setParameters(self, params) -> None:
        wsComponents.setParameters(params)
        print("params: ", wsComponents.getParameters())

    def setHeaders(self, headers) -> None:
        wsComponents.setHeaders(headers)
        print("headers: ", wsComponents.getHeaders())

    # do GET request
    def getRequest(self, api_request_context: APIRequestContext):
        return  api_request_context.get(wsComponents.getUri(), params=wsComponents.getParameters(),
                           headers=wsComponents.getHeaders())

    # do POST request
    def postRequest(self, api_request_context: APIRequestContext):
        return api_request_context.post(wsComponents.getUri(), data=wsComponents.getBody(),
                            headers=wsComponents.getHeaders())

    def sentRequest(self) -> None:
        method = wsComponents.getMethod().upper()
        global response
        if ("GET" in method):
            print("api_request_context: ",api_request_context)
            response = self.getRequest(api_request_context)
        elif ("POST" in method):
            response = self.postRequest(api_request_context)
        else:
            print("new method!!!")
            response = self.getRequest(api_request_context)
        # print("request: ", requests)
        print("response: ", response.text)

    # get HTTP code
    def getHTTPCode(self):
        return response.status
    
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
            stringText = stringText.replace("{" + key + "}", value)
        return stringText

    def verifyResponseCodeEqualsValue(self, value):
        code = self.getHTTPCode()
        print("code = ", code)
        message = "actual value= " + str(code) + ", but expected value= " + str(value)
        assert code == value, message