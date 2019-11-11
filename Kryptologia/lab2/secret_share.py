import numpy as np
from binascii import hexlify
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.secret_sharing import Shamir


key = get_random_bytes(16)
shares = Shamir.split(2, 5, key)
