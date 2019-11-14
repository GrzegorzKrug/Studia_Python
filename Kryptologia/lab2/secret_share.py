import numpy as np
# from binascii import hexlify
# from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
# from Crypto.Protocol.SecretSharing import Shamir

class SecretShare:
	def __init__(self, secretInput=None, shareNum=3, quiet=True):
		if not secretInput:
				self.secret = [bt for bt in get_random_bytes(10)]
		else:
			self.secret = [bt for bt in secretInput]
		
		self.complexity = len(self.secret)	
		self.shareNum = shareNum		
		#self.regions = [Region(3), Region(4), Region(10)]	
		self.M = int.from_bytes(self.secret, byteorder='big')
		self.S = None
		self.quiet = quiet

	def createShares(self, n):		
		p = 2*self.M + 1
		p = 13 # FIX
		if not (self.M > n and self.M < p):
			print(f"Error: M < n or M > p")

		coeffs = [self.M]
		coeffs = [11, 8, 7] # FIX
		# for i in range(n-1):
		# 	coeffs += [int.from_bytes(get_random_bytes(self.complexity),
		# 				byteorder='big')]
		poly = Polynomial(coeffs)
		if not self.quiet:
			print(poly)		
		self.S = []

		for i in range(n):
			s, txt = poly(i+1)
			s = s % p
			self.S += [s]
			# print(f"Share {i+1} = {s}")

		#print(f"Coeffs: {coeffs}")

	def run(self):		
		A = ([bt ^ 125 for bt in self.secret])  # secret ^ 125
		#out = ([bt ^ 125 for bt in A])
		out = None
		if not self.quiet:
			print(f"\nSekret:\n{self.concatenateBytes(self.secret)}")
			print(f"Sekret liczbowo: {self.M}")

		self.createShares(self.shareNum)
		if not self.quiet:
			for i, s in enumerate(self.S):
				print(f"Share {i+1} = {s}")

		if out == self.secret:
			print("Secret is the same")
			print(f"Odtworzony sekret:\n{self.concatenateBytes(out)}")			
		else:
			print("Secret is not the same!")
			try:
				print(f"{self.concatenateBytes(out)}")
			except TypeError:
				print(f"{out}")
		x = ModularInverse.mulinv(17, 43)  # TO DO
		print(f"Inverse modulo 17^-1%43 = {x}")

	def translateByteToText(self, textin):
		return ''.join([chr(o) for o in textin])

	def concatenateBytes(self, bts):
		out = b''
		for bt in bts:
			out += str(bt).encode()
		return out


class Polynomial:
	def __init__(self, coeffs):
		self.coeffs = coeffs
		#print(f"New coeffs {self.coeffs}")

	def __repr__(self):
		txt = 'f(x) ='
		for i in range(len(self.coeffs)-1, 0, -1):
			txt += f' {self.coeffs[i]} *x^{i} +'
		txt = txt[:-2] + f' + {self.coeffs[0]}'
		return txt

	def __call__(self, x):
		y = 0
		for i, coeff in enumerate(self.coeffs):
			y += x**i * coeff
		return y, f'f({x}) = {y}'


# Wikipedia
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


class Region:
	def __init__(self, senatorsNum=1):
		self.senators = []


if __name__ == '__main__':
	#app = SecretShare(secretInput=get_random_bytes(2))
	app = SecretShare(secretInput=b'\x0B', shareNum=5)
	app.run()

	app = SecretShare(secretInput=get_random_bytes(30))
	#app.run()

	#a = ModularInverse.mulinv(17, 43)
	input('End....')