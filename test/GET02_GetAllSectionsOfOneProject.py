import sys
sys.path.insert(0, ".")
from main.steps.RestfulSteps import *

# 1. Step set values in path
restfulSteps = RestfulSteps()
path = "/rest/v2/sections?project_id={projectId}&test_id={testId}"
valueParams = {
    "projectId": "2308134158",
    "testId": "12345"
}
path = restfulSteps.insertVariableValueIntoStringText(path, valueParams)
print("path: ", path)
# 1. Step init with protocol, domain, path, method, body
restfulSteps.initRequest("https", "api.todoist.com", path, "GET", None)

# 3. Step set headers for GET method
headers = {
    "Authorization": "Bearer 59797f84915abb8edf1fd631aaafeed028186e11",
    "Content-Type": "application/json"
}
restfulSteps.setHeaders(headers)

# 4. Step send request
restfulSteps.sentRequest()

# 5. Step verify
# # 5.1 get http code
code = restfulSteps.getHTTPCode()
print("http code: ", restfulSteps.getHTTPCode())
