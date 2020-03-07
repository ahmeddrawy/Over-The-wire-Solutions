#!  usr/bin/env python
import requests
import re
username="natas0"
password="natas0"
url = "http://natas0.natas.labs.overthewire.org/"
response = requests.get(url , auth = (username , password))
print (response.text)