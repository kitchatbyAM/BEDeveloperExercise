import json
import requests
from requests.auth import HTTPBasicAuth

url = 'http://localhost:1337/tasks/'


data1 = {'tasktitle':'Assignment', 'taskdescription':'1. API 2. Docker 3. Python script', 'taskstate': 'To do', 'taskduedate':'2020-07-14'}
data2 = {'tasktitle':'Leetcode', 'taskdescription':'Strings, List', 'taskstate': 'To do', 'taskduedate':'2020-07-19'}
data3 = {'tasktitle':'Django API', 'taskdescription':'Views, Models, Serializers, URLs', 'taskstate': 'To do', 'taskduedate':'2020-07-20'}
data4 = {'tasktitle':'Docker', 'taskdescription':'Postgres, Gunicorn, Nginx', 'taskstate': 'To do', 'taskduedate':'2020-07-16'}
print("Posting data to form")
r1 = requests.post(url, auth=HTTPBasicAuth('beprojectuser','1234pass'), data=data1, verify=False)
r2 = requests.post(url, auth=HTTPBasicAuth('beprojectuser','1234pass'), data=data2, verify=False)
r3 = requests.post(url, auth=HTTPBasicAuth('beprojectuser','1234pass'), data=data3, verify=False)
r4 = requests.post(url, auth=HTTPBasicAuth('beprojectuser','1234pass'), data=data4, verify=False)
print("----------------Printing Data after post ------------")
response = requests.get(url, auth=('beprojectuser', '1234pass'))
print(response.text)

print("Updating Data with id 2")
r = requests.put('http://localhost:1337/tasks/2/', auth=HTTPBasicAuth('beprojectuser','1234pass'), data={'taskstate':'In progress', 'taskduedate':'2020-07-20'})
print(r.content)
print("----------------Printing Data after update ------------")
response = requests.get(url, auth=('beprojectuser', '1234pass'))
print(response.text)

print("Deleting record with id 4")
res = requests.delete('http://localhost:1337/tasks/6/', auth=HTTPBasicAuth('beprojectuser','1234pass'))

print("----------------Printing Data after deletion ------------")
response = requests.get(url, auth=('beprojectuser', '1234pass'))
print(response.text)
