""" insert awesome sexy ascii manga here 
	Security Tube WAPChallenge 7
	By no means optimized for anything....
	Code produced by stoned monkeys, no cows were hurt.
	
	In theory this could have been used to break multiple
	digests in gigs of pcaps, but then there's Challenge 8
	so what can I do....

	@bytew0rm
"""

import hashlib
import dpkt
import sys

f=open(sys.argv[1],"rb")
	
pcap=dpkt.pcap.Reader(f)

for ts, buf in pcap:
  eth=dpkt.ethernet.Ethernet(buf)  
  if eth.type!=2048:    
  	continue         
  ip=eth.data
  if ip.p!=6:
  	continue
  tcp=ip.data

  if tcp.data=="":
  		continue	#nothing to do here

  try:
	http=dpkt.http.Request(tcp.data)
  	
  except Exception,e:
  	print "Exception during pcap processing: "+str(e) 

  else:
  	stuff=  http.headers["authorization"].split(',')
  	authInfo={}	
  	for s in stuff:
  		s=s.strip().split("=",1)
  		try:
  			authInfo[s[0].strip("\"")]=s[1].strip("\"")
  		except Exception, e:
  			print e
  		
  	if 'Digest username' in authInfo and 'realm' in authInfo and 'nc' in authInfo and 'qop' in authInfo and 'uri' in authInfo and 'cnonce' in authInfo:
  
  		print "Starting to crack digest for "+authInfo["realm"]+" / user "+authInfo["Digest username"]
  		
  		p=open(sys.argv[2],"rb")

  		for password in p:
  			password =  password.strip()
  			
  			hash1 = hashlib.md5(authInfo["Digest username"]+":"+authInfo["realm"]+":"+password).hexdigest()
  			hash2 =	hashlib.md5("GET:"+authInfo["uri"]).hexdigest()		
			testresponse = hashlib.md5(hash1+":"+authInfo["nonce"]+":"+authInfo["nc"]+":"+authInfo["cnonce"]+":"+authInfo["qop"]+":"+hash2).hexdigest()
			
  			if testresponse == authInfo['response']:
  				print "Cracked the digest, password is: " + password
  				break;

  		p.close()

  	else:
  		print "incomplete auth info!"

   
print e
f.close()
