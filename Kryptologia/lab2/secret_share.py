import numpy as np
from sympy import nextprime
from Crypto.Random import get_random_bytes
import random
import sys
import time


def time_it(N):
	def wrapper(some_fun):
		def go(*args, **kwargs):
			T  = []
			n = N
			if n < 0:
				n = 1
			for i in range(n):
				t0 = time.time()
				out = some_fun(*args, **kwargs)
				t_end = time.time() - t0
				t_end_ms = round(t_end * 1000, 6)
				T += [t_end_ms]
				
				# if i== 0 or (i+1)%10 == 0:
				# 	print(f"Loop {i+1} of {n}")
				# 	print(f"Encoding and decoding time: {t_end_ms} ms")
			print(f'Average time: {np.mean(T)} ms')
			return out
		return go
	return wrapper


class SecretShare:
	def __init__(self, shareNum, prog, secretInput=None, quiet=True):
		if not secretInput:
			self.secret = [bt for bt in get_random_bytes(10)]
		else:
			self.secret = [bt for bt in secretInput]
		
		self.complexity = len(self.secret)	# complexity in byte's num
		#print(f"Complex: {self.complexity}")
		self.shareNum = shareNum
		self.prog = prog		
		self.quiet = quiet

		#self.regions = [Region(3), Region(4), Region(10)]	
		self.M = int.from_bytes(self.secret, byteorder='big')
		#print(f" suma {sum(self.secret)}")
		#print(f" M {self.M}")
		self.shares = None
		self.p = None
		

	def createShares(self):		
		n = self.shareNum				
		self.p = nextprime(self.M)
		# if not self.quiet:
			# print(f"P = {self.p}")
		if (self.prog > self.shareNum):
			raise ValueError(f"Cieni mniej niż prog potrzebny do odworzenia!")

		coeffs = [self.M]		
		for i in range(self.prog - 1):
			coeffs += [int.from_bytes(get_random_bytes(self.complexity),
						byteorder='big')]
		poly = Polynomial(coeffs)
		# if not self.quiet:
		# 	print(poly)		
		self.shares = []

		for i in range(n):
			s, txt = poly(i+1)
			s = s % self.p
			self.shares += [s]
		return self.shares

	def reconstruct(self, shadows):		
		out = 0
		shadows = [{'xi': i+1, 'm': sh} for i, sh in enumerate(shadows)]
		
		#print(f"shadows {shadows}")
		random.shuffle(shadows)
		shadows = shadows[:self.prog]
		X = 0  # const
		for i, sh in enumerate(shadows):
			res = 1
			for j in range(len(shadows)):
				if j == i:
					continue
				a = (X - shadows[j]['xi']) % self.p
				b = sh['xi'] - shadows[j]['xi']
				if b < 0:
					b += self.p
				b = ModularInverse.mulinv(b, self.p)
				res *=  a * b

			out += (sh['m'] * res)
		return out % self.p

	@time_it(30)
	def run(self, quiet=None):
		if not quiet is None:
			self.quiet = quiet
		out = None
		if not self.quiet:			
			print(f"\nSekret liczbowo: {self.M}")
			#print(f"Sekret:\n{self.concatenateBytes(self.secret)}")

		self.createShares()
		if not self.quiet:
			for i, s in enumerate(self.shares):
				print(f"Share {i+1} = {s}")

		out = self.reconstruct(self.shares)
		if not self.quiet:
			if out == self.M:			
				print(f"Secret is the same:\n{out}")			
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


# class Region:
# 	def __init__(self, senatorsNum=1):
# 		self.senators = []


if __name__ == '__main__':
	size = 30
	SECRET = get_random_bytes(size)
	QUIET = True

	dealer = SecretShare(secretInput=SECRET, shareNum=3, prog=3, quiet=True)
	print('\nPodzial Sekretu')		
	print(f"Sekret: {int.from_bytes(SECRET, byteorder='big')}")
	dealer.run()

	S = dealer.createShares()	
	## s1 = str(S[0]).encode()  # konwersja cyfr
	s1 = (S[0]).to_bytes(size, byteorder='big')
	s2 = (S[1]).to_bytes(size, byteorder='big')
	s3 = (S[2]).to_bytes(size, byteorder='big')

	# Same Secret Time Checking
	# s1 = SECRET
	# s2 = s1
	# s3 = s1
	# S = [s1, s1, s1]
	
	region1 = SecretShare(secretInput=s1, shareNum=6, prog=3, quiet=QUIET)
	region2 = SecretShare(secretInput=s2, shareNum=4, prog=3, quiet=QUIET)
	region3 = SecretShare(secretInput=s3, shareNum=10, prog=6, quiet=QUIET)

	
	print('\nRegion 1')
	print(f"Sekret: {S[0]}")
	region1.run()

	print('\nRegion 2')
	print(f"Sekret: {S[1]}")
	region2.run()

	print('\nRegion 3')
	print(f"Sekret: {S[2]}")
	region3.run()
	
	#app = SecretShare(secretInput=get_random_bytes(5), shareNum=15, prog=10, quiet=False)
	#app.run()
	input('\nEnd....')
