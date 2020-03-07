#!  usr/bin/env python
import requests
import re
username="natas1"
password="gtVrDuiDfck831PqWsLEZy5gyDz1clto"
url = "http://%s.natas.labs.overthewire.org/" % username
response = requests.get(url , auth = (username , password))
print (response.text)