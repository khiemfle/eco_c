from Crypto.Cipher import AES
import Crypto.Cipher.AES
from binascii import hexlify, unhexlify
import sys

# key = unhexlify('2b7e151628aed2a6abf7158809cf4f3c')
# key = unhexlify('000000000000001500000000f2000000')
IV = unhexlify('00000000000000000000000000000000')

# test = "ttm4536afasfasdd"
# cipher = AES.new(key,AES.MODE_CBC,IV)
# ciphertext = cipher.encrypt(test)

ciphertext = unhexlify('6fe1ad578ca4fcd3fcb68e241d0dab57cded9922190ed6e91af19c564541d93d119d35580e5aa28841f00c8b5825cbcb65120da301e6826703941e12dcd68c11')

def hstr(val):
    return '{:02x}'.format(val)

def split_task(s,e, fr):
    for i1 in range(s, e):
        if i1 < fr[0]:
            continue
        for i2 in range(256):
            if i2 < fr[1]:
                continue
            for i3 in range(256):
                if i3 < fr[2]:
                    continue
                for i5 in range(256):
                    if i5 < fr[3]:
                        continue
                    for i8 in range(256):
                        if i8 < fr[4]:
                            continue
                        for i13 in range(256):
                            if i13 < fr[5]:
                                continue
                            temp = hstr(i1)+ hstr(i2)+hstr(i3)+"00"+hstr(i5)+"0000" + hstr(i8) + "00000000"+ hstr(i13)+"000000"
                            key = unhexlify(temp)
                            print temp
                            decipher = AES.new(key,AES.MODE_CBC,IV)
                            plaintext = decipher.decrypt(ciphertext)
                            if plaintext.startswith('ttm4536{'):
                                print temp
                                print plaintext
                                sys.exit()

split_task(int(sys.argv[1]), int(sys.argv[2]))






