from Crypto.Cipher import AES
from Crypto import Random
# import sys


#def __init__(self):
KEY_LENGTH = 16  # AES128
BLOCK_SIZE = AES.block_size
_random_gen = Random.new()
_key = _random_gen.read(KEY_LENGTH)

def _add_padding(plain):
    pad_len = BLOCK_SIZE - (len(plain) % BLOCK_SIZE)
##    if pad_len == 0:
##        pad_len = 16
    padding = bytes([pad_len]) * pad_len
    return plain + padding

def _remove_padding(data):
    pad_len = data[-1]	
    if pad_len < 1 or pad_len > BLOCK_SIZE:  # read padding from last pos
            return None #raise ValueError
        
    for i in range(1, pad_len):  # Check padding bytes
            if data[-i-1] != pad_len: 
                    return None                
    return data[:-pad_len]

def encrypt(msg):  # ok iv + msg + padding
    iv = _random_gen.read(AES.block_size)
    cipher = AES.new(_key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(_add_padding(msg))

def _decrypt(data):
        iv = data[:BLOCK_SIZE]  # slice prev blocks
        decryptor = AES.new(_key, AES.MODE_CBC, iv)  #make decryptor
        return _remove_padding(decryptor.decrypt(data[BLOCK_SIZE:]))

def is_padding_ok(data):
        return _decrypt(data) is not None

if __name__ == '__main__':
	print("nothing...")
        	
