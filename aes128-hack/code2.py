from base64 import urlsafe_b64encode, urlsafe_b64decode
from Crypto.Cipher import AES
from Crypto import Random


BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

base64pad = lambda s: s + '=' * (4 - len(s) % 4)
base64unpad = lambda s: s.rstrip("=")
encrypt_key = 'LKHlhb899Y09olUi'


def encrypt(key, msg):
    iv = 16 * '00'.decode('hex')
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=AES.block_size * 8)
    encrypted_msg = cipher.encrypt(pad(str(msg)))
    return base64unpad(urlsafe_b64encode(iv + encrypted_msg))


# when incorrect encryption key is used, `decrypt` will return empty string
def decrypt(key, msg):
    decoded_msg = urlsafe_b64decode(base64pad(msg))
    iv = 16 * '00'.decode('hex')
    encrypted_msg = decoded_msg[BS:] 
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=AES.block_size * 8)
    return unpad(cipher.decrypt(encrypted_msg))

hidden_msg = encrypt(encrypt_key, "Hello World")
print decrypt(encrypt_key, hidden_msg) # Hello World