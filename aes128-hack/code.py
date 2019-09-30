from Crypto.Cipher import AES
import Crypto.Cipher.AES
from binascii import hexlify, unhexlify
key = unhexlify('2b7e151628aed2a6abf7158809cf4f3c')
IV = unhexlify('00000000000000000000000000000000')

test = "abcdabcdabcdabcd"
# pl = test.encode('hex')
# print pl
# plaintext1 = unhexlify('6bc1bee22e409f96e93d7e117393172a')
cipher = AES.new(key,AES.MODE_CBC,IV)
ciphertext = cipher.encrypt(test)
hexlify(ciphertext)

# ciphertext = unhexlify('6fe1ad578ca4fcd3fcb68e241d0dab57cded992190ed6e91af19c564541d93d119d35580e5aa28841f00c8b5825cbcb65120da301e6826703941e12dcd68c11')
decipher = AES.new(key,AES.MODE_CBC,IV)

plaintext = decipher.decrypt(ciphertext)
print plaintext
# plaintext == plaintext1 + plaintext2 + plaintext3  # test if decryption was successful
# True
# hexlify(plaintext)
# print plaintext.decode('hex')
# b'6bc1bee22e409f96e93d7e117393172aae2d8a571e03ac9c9eb76fac45af8e5130c81c46a35ce411e5fbc1191a0a52ef'