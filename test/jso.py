import json
  
# Opening JSON file
f = open('data44.json')
data = json.load(f)
# data=json.dumps(data, indent=4)
# print(data["status"],data["message"],data["data"][0]['employee_name'])
# ===========================================================
# print(data["commits"][0]['author']['username'])
# print(data['ref'])
# print(data['commits'][0]['timestamp'])
# ==========================================================
# data["commits"][0]['name'],data['commits'][0]['username'],data['ref'],
# for i in data['emp_details']:
#     print(i)
if data["action"] == "opened":
    print("Pull_Request")
    print("AUTHOR")
    print(data["pull_request"]["base"]['label'])
    print("TO -" )
    print(data["pull_request"]["head"]["ref"]  )
    print("FROM - ")
    print(data["pull_request"]["base"]["ref"])
    print( 'Time')
    print(data["pull_request"]["updated_at"])
if data["action"] == "closed":
    print("Marge")
    print("AUTHOR")
    print(data["pull_request"]["base"]['label'])
    print("TO -" )
    print(data["pull_request"]["head"]["ref"]  )
    print("FROM - ")
    print(data["pull_request"]["base"]["ref"])
    print( 'Time')
    print(data["pull_request"]["updated_at"])
else:
    print('nothing')