import numpy as np
from binascii import hexlify
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.SecretSharing import Shamir

class SecretShare:
	def __init__(self, secretInput=None):
		if not secretInput:
				self.secret = [bt for bt in get_random_bytes(10)]
		else:
			self.secret = [bt for bt in secretInput]

		self.regions = [Region(3), Region(4), Region(10)]	
		self.complexity = len(self.secret)	
		self.S = None

	def createShares(self, n):
		self.S = []
		for i in range(n):
			self.S += [get_random_bytes(self.complexity)]


	def run(self):		
		A = ([bt ^ 125 for bt in self.secret])  # secret ^ 125
		#out = ([bt ^ 125 for bt in A])
		out = None
		print(f"\nSekret:\n{self.concatenateBytes(self.secret)}")

		self.createShares(len(self.regions))



		

		if out == self.secret:
			print("Secret is the same")
			print(f"Odtworzony sekret:\n{self.concatenateBytes(out)}")			
		else:
			print("Can not decrypt. Secret is not the same!")
			try:
				print(f"Odtworzony sekret:\n{self.concatenateBytes(out)}")
			except TypeError:
				print(f"Odtworzony sekret:\n{out}")
		

	def translateByteToText(self, textin):
		return ''.join([chr(o) for o in textin])

	def concatenateBytes(self, bts):
		out = b''
		for bt in bts:
			out += str(bt).encode()
		return out

class Region:
	def __init__(self, senatorsNum=1):
		self.senators = []


if __name__ == '__main__':
	app = SecretShare(secretInput=None)
	app.run()

	app = SecretShare(secretInput=get_random_bytes(30))
	app.run()
	input('End....')