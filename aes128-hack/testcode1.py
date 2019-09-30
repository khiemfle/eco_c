from Crypto.Cipher import AES
import Crypto.Cipher.AES
from binascii import hexlify, unhexlify
import sys
import time


# key = unhexlify('2b7e151628aed2a6abf7158809cf4f3c')
key = unhexlify('000000000000001500000000f2000000')
IV = unhexlify('00000000000000000000000000000000')

test = "ttm4536{afasfas "
cipher = AES.new(key,AES.MODE_CBC,IV)
ciphertext = cipher.encrypt(test)

print hexlify(ciphertext)

ciphertext = unhexlify("c7519737c05b90c32d3b94a121ec056c")
ciphertext = unhexlify("c7519737c05b90c32d3b94a121ec056cd195d738a1ab4d138f01aaf487fb6e8b")
decipher = AES.new(key,AES.MODE_CBC,IV)
plaintext = decipher.decrypt(ciphertext)
print plaintext