from Crypto.Cipher import AES
import Crypto.Cipher.AES
from binascii import hexlify, unhexlify
key = unhexlify('2b7e151628aed2a6abf7158809cf4f3c')
IV = unhexlify('00000000000000000000000000000000')

# test = "abcdabcdabcdabcd"
# pl = test.encode('hex')
# print pl
# cipher = AES.new(key,AES.MODE_CBC,IV)
# ciphertext = cipher.encrypt(pl)
# hexlify(ciphertext)

ciphertext = unhexlify('6fe1ad578ca4fcd3fcb68e241d0dab57cded9922190ed6e91af19c564541d93d119d35580e5aa28841f00c8b5825cbcb65120da301e6826703941e12dcd68c11')
decipher = AES.new(key,AES.MODE_CBC,IV)

plaintext = decipher.decrypt(ciphertext)
hexlify(plaintext)
print plaintext.decode('hex')