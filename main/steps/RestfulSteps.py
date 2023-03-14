import allure
from main.steps.RestfulSubSteps import *
import sys
sys.path.insert(0, ".")

restfulSubSteps = RestfulSubSteps()


class RestfulSteps:

    @allure.step('1. Init')
    def initRequest(self, protocol, domain, path, method, body):
        restfulSubSteps.initRequest(protocol, domain, path, method, body)

    @allure.step('2. Set parameters')
    def setParameters(self, parameters):
        restfulSubSteps.setParameters(parameters)

    @allure.step('3. Set header')
    def setHeaders(self, headers):
        restfulSubSteps.setHeaders(headers)

    @allure.step('4. Send request')
    def sentRequest(self, api_request_context):
        restfulSubSteps.sentRequest(api_request_context)

    @allure.step('5. verify http code equal {value}')   
    def verifyResponseCodeEqualsValue(self, value):
        restfulSubSteps.verifyResponseCodeEqualsValue(value)

    def getSingleValueFromJsonPath(self, jsonPath):
        return restfulSubSteps.getSingleValueFromJsonPath(jsonPath)

    def insertVariableValueIntoStringText(self, stringText, values):
        return restfulSubSteps.setValueIntoText(stringText, values)
