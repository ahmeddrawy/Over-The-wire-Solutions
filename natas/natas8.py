#!  usr/bin/env python
import requests
import re
username="natas8"
password="DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe"
# headers for http request 
# headers = {"Referer" : "http://natas5.natas.labs.overthewire.org/"}
url = "http://%s.natas.labs.overthewire.org/" % username
# get = {"page" : "/etc/natas_webpass/natas8"}
session = requests.Session()
# cook = {"loggedin" : "1"}
posst  = {"secret" : "oubWYf2kBq" , "submit" :"submit"}
# response = session.post(url , auth = (username , password),cookies = cook)
response = session.post(url ,data = posst , auth = (username , password))
# response = session.get(url , params=get,auth = (username , password))
# response = session.get(url , auth = (username , password))

# print session.headers

# print ("\n")

# print session.cookies
print (response.text)