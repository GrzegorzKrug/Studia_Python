import numpy as np
# from binascii import hexlify
# from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
# from Crypto.Protocol.SecretSharing import Shamir

class SecretShare:
	def __init__(self, secretInput=None, shareNum=3):
		if not secretInput:
				self.secret = [bt for bt in get_random_bytes(10)]
		else:
			self.secret = [bt for bt in secretInput]
		
		self.complexity = len(self.secret)	
		self.shareNum = shareNum		
		#self.regions = [Region(3), Region(4), Region(10)]	
		self.M = int.from_bytes(self.secret, byteorder='big')
		self.S = None

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
		print(poly)		
		self.S = []
		for i in range(n):
			s, txt = poly(i+1)
			s = s % p
			self.S += [s]
			print(f"Share {i+1} = {s}")
		#print(f"Coeffs: {coeffs}")

	def inverse_modulo(a, n):
		g = [n, a, 0]	
		u = None


	def run(self):		
		A = ([bt ^ 125 for bt in self.secret])  # secret ^ 125
		#out = ([bt ^ 125 for bt in A])
		out = None
		print(f"\nSekret:\n{self.concatenateBytes(self.secret)}")
		print(f"Sekret liczbowo: {self.M}")

		self.createShares(self.shareNum)


		if out == self.secret:
			print("Secret is the same")
			print(f"Odtworzony sekret:\n{self.concatenateBytes(out)}")			
		else:
			print("Secret is not the same!")
			try:
				print(f"{self.concatenateBytes(out)}")
			except TypeError:
				print(f"{out}")
		

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


class Region:
	def __init__(self, senatorsNum=1):
		self.senators = []


if __name__ == '__main__':
	#app = SecretShare(secretInput=get_random_bytes(2))
	app = SecretShare(secretInput=b'\x0B', shareNum=5)
	app.run()

	app = SecretShare(secretInput=get_random_bytes(30))
	#app.run()

	input('End....')