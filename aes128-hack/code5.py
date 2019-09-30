from Crypto import Random 
from Crypto.Cipher import AES 
iv = "\x8C\xAE\x65\x24\xA8\x63\xE3\x0F\x9B\x9D\x8D\xA2\xED\x05\xAA\x48" 
ciphertext = "\x16\xD0\x7A\x30\x8E\x24\xED\xF8\xE7\x71\x57\x03\xC5\x74\xB6\xE3\x26\x40\x56\xE7\xE9\x56\xCF\x76\x61\xBD\x72\xE3\xC7\xFC\x6C\x15\x27\x3D\x2A\xED\xA6\xB6\xEA\x04\xF1\xCC\xFE\xF6\x77\xB4\x41"

ciphertext = ciphertext + "66".decode("hex")

# print ciphertext

def decrypt(key): 
    cipher = AES.new(key, AES.MODE_CBC, iv)
    result = cipher.decrypt(ciphertext)
    return result

def brute():
    for i in range(256):
        for j in range(256):
            key = "".join([chr(j), chr(i)]).ljust(16, "\x00")
            result = decrypt(key)
            if "flag" in result:
                print(result)
                print("key :", key.encode("hex"))
                return

brute()