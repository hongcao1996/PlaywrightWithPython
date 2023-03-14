import allure
from features.steps.SubSteps import *
import sys
sys.path.insert(0, ".")
from behave import *
subSteps = SubSteps()


class Steps():
    @when('Init request with protocol={protocol} and domain={domain} and path={path} and method={method} and body={body}')
    def initRequest(self, protocol, domain, path, method, body):
        subSteps.initRequest(protocol, domain, path, method, body)

    @when('Set parameters')
    def setParameters(context):
        # get datatable
        datatable = context.table
        dict = {}
        for row in datatable:
            dict[row['key']] = row['value']
            print("key: "+row['key'] + "....."+"value: "+row['value']) # for log in console
        subSteps.setParameters(dict)

    @when('Set header')
    def setHeaders(context):
        #  get datatable
        datatable = context.table
        dict = {}
        for row in datatable:
            dict[row['key']] = row['value']
            print("key: "+row['key'] + "....."+"value: "+row['value']) # for log in console
        subSteps.setHeaders(dict)

    @when('Send request')
    def sentRequest(context):
        subSteps.sentRequest()

    @then('http code equal {value}')   
    def verifyResponseCodeEqualsValue(self, value):
        subSteps.verifyResponseCodeEqualsValue(value)

    def getSingleValueFromJsonPath(self, jsonPath):
        return subSteps.getSingleValueFromJsonPath(jsonPath)

    def insertVariableValueIntoStringText(self, stringText, values):
        return subSteps.setValueIntoText(stringText, values)
