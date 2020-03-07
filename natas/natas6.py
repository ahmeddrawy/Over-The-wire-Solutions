#!  usr/bin/env python
import requests
import re
username="natas6"
password="aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"
# headers for http request 
# headers = {"Referer" : "http://natas5.natas.labs.overthewire.org/"}
url = "http://%s.natas.labs.overthewire.org/" % username
session = requests.Session()
# cook = {"loggedin" : "1"}
posst  = {"secret" : "FOEIUWGHFEEUHOFUOIU" , "submit" :"submit"}
# response = session.post(url , auth = (username , password),cookies = cook)
response = session.post(url ,data = posst , auth = (username , password))
print session.post

# print ("\n")

# print session.cookies
print (response.text)