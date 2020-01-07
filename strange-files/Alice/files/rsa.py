#!/usr/bin/python2.7
#- *- coding: utf- 8 - *-
# The first line is to ensure that we will not get strange error messages
# if the name of the file have som specific language characters
import os, sys, Crypto
from Crypto.PublicKey import RSA

print os.getcwd()
f = open('file1','rb')
ciphertext1 = f.read()
f.close()
f = open('file2','rb')
ciphertext2 = f.read()
f.close()
# Let us make a list of all pem files and a list of all public keys that we can find in all subfilders
publickeys = []
files = []
CurrentDirectory = os.getcwd() + "/file3-dir"
# r=root, d=directories, f = files
for r, d, f in os.walk(CurrentDirectory):
	for file in f:
 		if '.pem' in file:
 			files.append(os.path.join(r, file))
for filename in files:
 # we import keys as public key objects with RSA.importKey
 pubKeyObj = RSA.importKey(open(filename, "rb"))
 publickeys.append(pubKeyObj)
for i in range(len(publickeys)-1):
	for j in range((i+1),len(publickeys)):
 	# we use the GCD function from Crypto.Util.number.GCD to check do two numbers has GCD bigger than 1
 	# note how we access the parts of the publickeys: publickeys[i].n . Other part is for example .e
		gcd = Crypto.Util.number.GCD(publickeys[i].n, publickeys[j].n)
 		if gcd != 1L:
 			First = i
 			Second = j
 			print "Found related keys. Key Nr.",i," and key Nr.",j, ", gcd = ", gcd
 			break
 # Notice the indentation of this 'else'. It is a trick how to exit many nested loops
	else:
 		continue
 	break

q = gcd
p1 = publickeys[First].n / q
p2 = publickeys[Second].n / q
# in RSA e * d = 1 mod (p - 1)*(q - 1)
# so, d = 1/e mod (p - 1)*(q - 1)
# we use here the powerfull function in Crypto module Crypto.Util.number.inverse
# to compute an inverse of a number, modulo some other number
d1 = Crypto.Util.number.inverse(publickeys[First].e, (p1 - 1)*(q - 1))
d2 = Crypto.Util.number.inverse(publickeys[Second].e, (p2 - 1)*(q - 1))
print d1
print d2
# Once we have all RSA components: n, e, d, p, q we use the function
# RSA.construct to construct a proper and standardized form of a full (private and public pair) RSA key
key1 = RSA.construct((p1*q, publickeys[First].e, d1, p1, q))
key2 = RSA.construct((p2*q, publickeys[Second].e, d2, p2, q))
print key1
print key2
# Once we have two complete RSA keys (private and public), we will try to use them to decrypt
# two ciphertexts that we got: ciphertext1 from file1 and ciphertext2 from file2
# But since it might be that we will try a wrong key for some of the ciphertexts, we have to use
# Python exceptions with the commads: try and except, where except in this case is 'ValueError'
try:
	decryptfile11 = key1.decrypt(ciphertext1)
	print decryptfile11
except ValueError:
	pass
try:
	decryptfile12 = key1.decrypt(ciphertext2)
	print decryptfile12
except ValueError:
	pass
try:
	decryptfile21 = key2.decrypt(ciphertext1)
	print decryptfile21
except ValueError:
	pass
try:
	decryptfile22 = key2.decrypt(ciphertext2)
	print decryptfile22
except ValueError:
	pass
