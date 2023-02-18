from main.steps.RestfulSubSteps import *
import sys
sys.path.insert(0, ".")

restfulSubSteps = RestfulSubSteps()


class RestfulSteps:

    def initRequest(self, protocol, domain, path, method, body):
        restfulSubSteps.initRequest(protocol, domain, path, method, body)

    def setParameters(self, parameters):
        restfulSubSteps.setParameters(parameters)

    def setHeaders(self, headers):
        restfulSubSteps.setHeaders(headers)

    def sentRequest(self):
        restfulSubSteps.sentRequest()

    def getHTTPCode(self):
        return restfulSubSteps.getHTTPCode()

    def getSingleValueFromJsonPath(self, jsonPath):
        return restfulSubSteps.getSingleValueFromJsonPath(jsonPath)

    def insertVariableValueIntoStringText(self, stringText, values):
        return restfulSubSteps.setValueIntoText(stringText, values)
