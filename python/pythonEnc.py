from Crypto import Random
from Crypto.Cipher import AES
import timeit

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=256):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")

def encrypt_file(file_name, key):
    start_time = timeit.default_timer()
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(plaintext, key)
    with open(file_name + ".enc", 'wb') as fo:
        fo.write(enc)
    print timeit.default_timer() - start_time

def decrypt_file(file_name, key):
    start_time = timeit.default_timer()
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext, key)
    with open(file_name + ".txt", 'wb') as fo:
        fo.write(dec)
    print timeit.default_timer() - start_time


key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'

#encrypt_file('File5.txt', key)
decrypt_file('File5.txt.enc', key)       
