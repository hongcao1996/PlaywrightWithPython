import sys
sys.path.insert(0, ".")
from main.steps.RestfulSteps import *

restfulSteps = RestfulSteps()

# 1. get project index 2
# 1.1 Step init with protocol, domain, path, method, body
restfulSteps.initRequest("https", "api.todoist.com",
                         "/rest/v2/projects", "GET", None)

# 1.2 Step set headers for GET method
headers = {
    "Authorization": "Bearer 59797f84915abb8edf1fd631aaafeed028186e11",
    "Content-Type": "application/json"
}
restfulSteps.setHeaders(headers)

# 1.3 Step send request
restfulSteps.sentRequest()

# 1.4 Step verify
# # 1.4.1 get http code
code = restfulSteps.getHTTPCode()
print("http code: ", restfulSteps.getHTTPCode())

# # 1.4.2 get id project with index 2
pathid = "$.[1].id"
projectId = restfulSteps.getSingleValueFromJsonPath(pathid)

# 2. create a section
# 2.1 Step init with protocol, domain, path, method, body
body = "{\"project_id\":\"{projectId}\", \"name\":\"Groceries 1\"}"
valueParams = {
    "projectId": ""+projectId+""
}
body = restfulSteps.insertVariableValueIntoStringText(body, valueParams)
print("new body: ", body)
restfulSteps.initRequest("https", "api.todoist.com",
                         "/rest/v2/sections", "POST", body)

# 2.2 Step set headers
headers = {
    "Authorization": "Bearer 59797f84915abb8edf1fd631aaafeed028186e11",
    "Content-Type": "application/json"
}
restfulSteps.setHeaders(headers)

# 2.3 Step send request
restfulSteps.sentRequest()

# 2.4 Step verify
# # 2.4.1 get http code
code = restfulSteps.getHTTPCode()
print("http code: ", restfulSteps.getHTTPCode())

# # 2.4.2 get value in response body
pathName = "$.name"
name = restfulSteps.getSingleValueFromJsonPath(pathName)
print("name: ", name)
