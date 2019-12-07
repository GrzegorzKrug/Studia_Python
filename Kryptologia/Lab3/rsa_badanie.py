from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


# Implementacja z Wikipedii
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm#Modular_inverse
class ModularInverse:
    @classmethod
    def xgcd(cls, a, b):
        """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
        x0, x1, y0, y1 = 0, 1, 1, 0
        while a != 0:
            q, b, a = b // a, a, b % a
            y0, y1 = y1, y0 - q * y1
            x0, x1 = x1, x0 - q * x1
        return b, x0, y0

    @classmethod
    def egcd(cls, a, b):
        """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = cls.egcd(b % a, a)
            return (g, y - (b // a) * x, x)

    @classmethod
    def mulinv(cls, a, b):
        """return x such that (x * a) % b == 1"""
        g, x, _ = cls.xgcd(a, b)
        if g == 1:
            return x % b
        else:
            raise ValueError("Not found modular inversion!")


secret_text = "my_secret_text"
secret_byte = secret_text.encode()
# b"abcde".decode("utf-8")

key = RSA.generate(2048)

private_key = key.export_key()
public_key = key.publickey()

# encrypted = public_key.encrypt(secret_text, 32)

# Encrypt the session key with the public RSA key
cipher_rsa = PKCS1_OAEP.new(public_key)
cipher_text = cipher_rsa.encrypt(secret_byte)

print(secret_byte)
# m = public_key **
# print(cipher_text)
# ModularInverse.mulinv()


# # Encrypt the data with the AES session key
# cipher_aes = AES.new(session_key, AES.MODE_EAX)
# ciphertext, tag = cipher_aes.encrypt_and_digest(secret)


# print(ciphertext.decode('utf-8'))

# for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext):
# print(x)
