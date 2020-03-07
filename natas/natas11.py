#!  usr/bin/env python
import requests
import urllib
import base64
username="natas11"
password="U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK"
url = "http://%s.natas.labs.overthewire.org/" % username
session = requests.Session()
posst  = {"data" : {"showpassword" : "yes" , "bgcolor" : "#ffffff"}}
# cook = requests.cookies.create_cookie(data : "")
# response = session.post(url , auth = (username , password),cookies = cook)
# json.dumps
response = session.post(url ,cookies = {'data' : 'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK'} , auth = (username , password))
# response = session.get(url , params=get,auth = (username , password))
response = session.get(url , auth = (username , password))
# print session.headers
# response.set_cookie(cook)

# print ("\n")
# print (response.cookies.get_dict())
# print session.cookies["data"]

# print	 urllib.unquote(session.cookies["data"])
print (response.text)

