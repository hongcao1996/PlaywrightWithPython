import sys
sys.path.insert(0, ".")
from main.steps.RestfulSteps import *

restfulSteps = RestfulSteps()
# 1. Step init with protocol, domain, path, method, body
restfulSteps.initRequest("https", "api.todoist.com",
                         "/rest/v2/comments", "GET", None)

# 2. Step set parameters for GET method
# parameters stored in dict
parameters = {
    "task_id": "6626011664"
}
restfulSteps.setParameters(parameters)

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

# # 5.2 get value in response body
pathid1 = "$.[0].id"
valueid1 = restfulSteps.getSingleValueFromJsonPath(pathid1)
print("value id 1: ", valueid1)
