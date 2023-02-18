import sys
sys.path.insert(0, ".")
from main.steps.RestfulSteps import *

restfulSteps = RestfulSteps()
# 1. Step init with protocol, domain, path, method, body
body = "{\"name\": \"Shopping List 1\"}"
restfulSteps.initRequest("https", "api.todoist.com",
                         "/rest/v2/projects", "POST", body)

# 2. Step set headers for GET method
headers = {
    "Authorization": "Bearer 59797f84915abb8edf1fd631aaafeed028186e11",
    "Content-Type": "application/json"
}
restfulSteps.setHeaders(headers)

# 3. Step send request
restfulSteps.sentRequest()

# 4. Step verify
# # 4.1 get http code
code = restfulSteps.getHTTPCode()
print("http code: ", restfulSteps.getHTTPCode())

# # 4.2 get value in response body
pathName = "$.name"
name = restfulSteps.getSingleValueFromJsonPath(pathName)
print("name: ", name)
