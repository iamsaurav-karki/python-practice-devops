import requests
import json
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
# print(response.json()) 
# print(response.status_code)

complete_details = response.json()
for user_data in range(len(complete_details)):
    print(complete_details[user_data]['user']['login'])