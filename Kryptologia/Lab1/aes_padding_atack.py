from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from functools import reduce
import re

print('CBC padding oracle attack demo')
print('Tekst jawny:')
data = input()

key = get_random_bytes(AES.block_size)
iv = get_random_bytes(AES.block_size)
encrypter = AES.new(key, AES.MODE_CBC, iv=iv)

padded_data = pad(data.encode(encoding="ascii",errors="replace"), AES.block_size)
ciphertext = encrypter.encrypt(padded_data)

print('Szyfrogram:')
print(re.sub("(.{32})", "\\1\n", ciphertext.hex().upper(), 0, re.DOTALL))

def oracle(ciphertext,key,iv):
    decrypter = AES.new(key, AES.MODE_CBC, iv=iv)
    try:
        unpad(decrypter.decrypt(ciphertext), AES.block_size)
        return True
    except ValueError:
        return False

def flat(list):
    return bytes([item for item in list])

blocks = [ciphertext[i:i+AES.block_size] for i in range(0, len(ciphertext), AES.block_size)]

cleartext = []
for block_num, (c1, c2) in enumerate(zip([iv]+blocks, blocks)):

    i2 = [0] * 16
    p2 = [0] * 16
    for i in range(15,-1,-1):
        for b in range(0,256):
            prefix = c1[:i]
            pad_byte = (AES.block_size-i)
            suffix = bytes([pad_byte ^ val for val in i2[i+1:]])
            evil_c1 = prefix + bytes([b]) + suffix

            if oracle(c2,key,evil_c1):
                i2[i] = evil_c1[i] ^ pad_byte
                p2[i] = c1[i] ^ i2[i]
                break
            else:
                pass

    cleartext+=p2

print(bytes(cleartext).decode(encoding="ascii", errors="replace"))
