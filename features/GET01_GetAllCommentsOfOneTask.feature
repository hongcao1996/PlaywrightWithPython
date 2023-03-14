Feature: Test getAllComments
    Background: Before Test Scenarios
    # Given Login
    Scenario: scenario 1
    When Init request with protocol="https" and domain="api.todoist.com" and path="/rest/v2/comments" and method="GET" and body="None"
    
    When Set parameters
    | key     | value     |
    | task_id | 6626011664|

    When Set header
    | key          | value|
    | Authorization| Bearer 59797f84915abb8edf1fd631aaafeed028186e11|
    | Content-Type | application/json|

    When Send request

    # Then http code equal "500"