import json
  
# Opening JSON file
f = open('data.json')
data = json.load(f)
# data=json.dumps(data, indent=4)
# print(data["status"],data["message"],data["data"][0]['employee_name'])
print(data["commits"][0]['author']['username'])
print(data['ref'])
print(data['commits'][0]['timestamp'])
# data["commits"][0]['name'],data['commits'][0]['username'],data['ref'],
# for i in data['emp_details']:
#     print(i)
  
# Closing file
f.close()