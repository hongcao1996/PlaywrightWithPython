1. GET01_GetAllCommentsOfOneTask:
get all comments of one task
https://api.todoist.com/rest/v2/comments?task_id=6626011664
curl: 
curl --location 'https://api.todoist.com/rest/v2/comments?task_id=6626011664' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer 59797f84915abb8edf1fd631aaafeed028186e11' \
--header 'Cookie: csrf=99de50dc7ff24c91be7496037c7444f1'
response: 
[ { "id": "3225914511", "task_id": "6626011664", "project_id": null, "content": "comment 1", "posted_at": "2023-02-17T07:24:40.606489Z", "attachment": null }, { "id": "3225914521", "task_id": "6626011664", "project_id": null, "content": "comment 2", "posted_at": "2023-02-17T07:24:45.555845Z", "attachment": null } ]

2. GET02_GetAllSectionsOfOneProject:
get all sections of one project
https://api.todoist.com/rest/v2/sections?project_id=2308134158
curl:
curl --location 'https://api.todoist.com/rest/v2/sections?project_id=2308134158' \
--header 'Authorization: Bearer 59797f84915abb8edf1fd631aaafeed028186e11' \
--header 'Cookie: csrf=e28fb4294edb47c09a38122bb0c7e912'
response:
[ { "id": "116066662", "project_id": "2308134158", "order": 1, "name": "Section 1" }, { "id": "116066706", "project_id": "2308134158", "order": 2, "name": "Section 2" } ]

3. POST01_PostCreateAProject:
post to create a project
curl:
curl --location 'https://api.todoist.com/rest/v2/projects' \
--header 'Content-Type: application/json' \
--header 'X-Request-Id: $(uuidgen)' \
--header 'Authorization: Bearer 59797f84915abb8edf1fd631aaafeed028186e11' \
--header 'Cookie: csrf=99de50dc7ff24c91be7496037c7444f1' \
--data '{"name": "Shopping List"}'
response:
{ "id": "2308188027", "parent_id": null, "order": 4, "color": "charcoal", "name": "Shopping List", "comment_count": 0, "is_shared": false, "is_favorite": false, "is_inbox_project": false, "is_team_inbox": false, "url": "https://todoist.com/showProject?id=2308188027", "view_style": "list" }

4. POST02_CreateASection:
- get all projects available
- create a new section inside one of the project
https://api.todoist.com/rest/v2/sections
curl: 
curl --location 'https://api.todoist.com/rest/v2/sections' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer 20359a53f2d264e2cbb0b538385c314b8d29ef3c' \
--header 'Cookie: csrf=e28fb4294edb47c09a38122bb0c7e912' \
--data '{"project_id":"2203306141", "name":"Groceries"}'
response:
{ "id": "116074868", "project_id": "2308134158", "order": 3, "name": "Groceries" }



How to run:
1. each test case(.py file - function having "test_" or "_test")
pytest ..\PlaywrightWithPython\test\POST02_CreateASection.py -s --alluredir=allure_report
-s : show log(all print())
--alluredir=allure_report: generate log for allure
2. show allure-report:
allure serve ..\PlaywrightWithPython\allure_report
3. clean report
allure generate --clean --output ..\PlaywrightWithPython\allure_report

Run Behave - Python
behave --no-capture // -> to print output
config settings.json to navigate step definitions

Run Behave - Allure
behave -f allure_behave.formatter:AllureFormatter -o reports/​​ ..\PlaywrightWithPython\features\test.feature
allure serve ..\PlaywrightWithPython\reports 