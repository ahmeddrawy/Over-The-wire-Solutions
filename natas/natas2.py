#!  usr/bin/env python
import requests
import re
username="natas2"
password="ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi"
url = "http://%s.natas.labs.overthewire.org/files" % username
response = requests.get(url , auth = (username , password))
print (response.text)