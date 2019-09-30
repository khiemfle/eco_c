from fractions import gcd
from binascii import hexlify, unhexlify

arr = []
arr2 = []
f = open("note11.txt", "r")

str = "1"
while str.strip() != "":
    str = f.readline()
    if str.strip() == "":
        break
    nu = int(str, 16)
    arr.append(nu)
    arr2.append(str)

print "Start"
i1 = 0
i2 = 0
while i1 < len(arr):
    while i2 < len(arr):
        m1 = arr[i1]
        m2 = arr[i2]
        if m1 != m2:
            # print "{}, {}".format(m1, m2)
            cd = gcd(m1, m2)
            if cd != 1:
                print "{} \n {} \n {} \n".format(m1, m2, cd)
                print "{} {}".format(arr2[i1], arr2[i2])
                print "{}, {}".format(i1, i2)
        i2 = i2 + 1
    i1 = i1 + 1
    i2 = 0