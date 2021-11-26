from flask.globals import request
import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 78, "name": "Joe", "views": 100000},
        {"likes": 10000, "name": "How to make REST", "views": 80000},
        {"likes": 10, "name": "Tim", "views": 2000}]

for i in range(len (data)):
    response=requests.put(BASE + "video/"+str(i), data[i])
    print(response.json())

input()

response= requests.post(BASE + "video/2", {"views":2, "likes":101})
print(response.json())
input()

response=requests.get(BASE + "video/2")
print(response.json())