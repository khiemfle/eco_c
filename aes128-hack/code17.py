from Crypto.Cipher import AES
import Crypto.Cipher.AES
from binascii import hexlify, unhexlify
import sys
import time

# key = unhexlify('2b7e151628aed2a6abf7158809cf4f3c')
# key = unhexlify('000000000000001500000000f2000000')
IV = unhexlify('00000000000000000000000000000000')

# test = "TTM4536{afasfas}"
# cipher = AES.new(key,AES.MODE_CBC,IV)
# ciphertext = cipher.encrypt(test)

ciphertext = unhexlify('6fe1ad578ca4fcd3fcb68e241d0dab57cded9922190ed6e91af19c564541d93d119d35580e5aa28841f00c8b5825cbcb65120da301e6826703941e12dcd68c11')

def hstr(val):
    return '{:02x}'.format(val)

def split_task(s,e, fr):
    start = time.time()
    for i1 in range(s, e):
        if i1 < fr[0]:
            continue
        for i2 in range(256):
            if i1 == fr[0] and i2 < fr[1]:
                continue
            for i3 in range(256):
                if i1 == fr[0] and i2 == fr[1] and i3 < fr[2]:
                    continue
                end = time.time()
                print(end - start)
                status = hstr(i1)+ hstr(i2)+hstr(i3)
                print status
                start = time.time()
                for i5 in range(256):
                    if i1 == fr[0] and i2 == fr[1] and i3 == fr[2] and i5 < fr[3]:
                        continue
                    for i8 in range(256):
                        if i1 == fr[0] and i2 == fr[1] and i3 == fr[2] and i5 == fr[3] and i8 < fr[4]:
                            continue
                        for i13 in range(256):
                            if i1 == fr[0] and i2 == fr[1] and i3 == fr[2] and i5 == fr[3] and i8 == fr[4] and i13 < fr[5]:
                                continue
                            temp = hstr(i1)+ hstr(i2)+hstr(i3)+"00"+hstr(i5)+"0000" + hstr(i8) + "00000000"+ hstr(i13)+"000000"
                            key = unhexlify(temp)
                            decipher = AES.new(key,AES.MODE_CBC,IV)
                            plaintext = decipher.decrypt(ciphertext)
                            if plaintext.lower().startswith('ttm4536{'):
                                print temp
                                print plaintext
                                sys.exit()

fr = [int(sys.argv[3], 16),int(sys.argv[4], 16),int(sys.argv[5], 16),int(sys.argv[6], 16),int(sys.argv[7], 16),int(sys.argv[8], 16)]
split_task(int(sys.argv[1]), int(sys.argv[2]), fr)






