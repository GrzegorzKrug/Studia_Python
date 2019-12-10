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
			print(f'Average excecution time: {np.mean(T)} ms')
			return np.mean(T)
		return go
	return wrapper


class SecretShare:
	def __init__(self, shareNum, prog, secretInput=None, quiet=True):
		if not secretInput:
			self.secret = [bt for bt in get_random_bytes(10)]
		else:
			self.secret = [bt for bt in secretInput]
		
		self.complexity = len(self.secret)	# complexity in byte's num
		#print(f" complexity = {self.complexity}")
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
		self.p = nextprime(self.M)  # P tylko większe od M
		#self.p = nextprime(2**(self.complexity*8))		
		if (self.prog > self.shareNum):
			raise ValueError(f"Cieni mniej niż prog potrzebny do odtworzenia!")
		if self.p < self.M:
			raise ValueError(f"P jest mniejsze od M {self.p} < {self.M}")

		coeffs = [self.M]  # Wyraz wolny a0	
		for i in range(self.prog - 1):
			coeffs += [int.from_bytes(get_random_bytes(self.complexity),
						byteorder='big')]
		poly = Polynomial(coeffs)	
		self.shares = []

		for i in range(n):
			s, txt = poly(i+1)
			s = s % self.p
			self.shares += [s]
		return self.shares

	def reconstruct(self, shadows):		
		out = 0
		shadows = [{'xi': i+1, 'm': sh} for i, sh in enumerate(shadows)]
		
		random.shuffle(shadows)
		shadows = shadows[:self.prog]
		X = 0  # const, F(0) = M
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

	@time_it(1)
	def run(self, quiet=None):
		if not quiet is None:
			self.quiet = quiet
		out = None
		# if not self.quiet:			
		# 	print(f"\nSekret liczbowo:\n{self.M}")		

		self.createShares()
		if not self.quiet:
			for i, s in enumerate(self.shares):
				print(f"\tShare {i+1} = {s}")

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
		return None		

	def translateByteToText(self, textin):
		return ''.join([chr(o) for o in textin])

	def concatenateBytes(self, bts):
		out = b''
		for bt in bts:
			out += str(bt).encode()
		return out


class Polynomial:  # Wielomian, liczenie wartosci w punktach x
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
	size = 10
	SECRET = get_random_bytes(size)
	QUIET = False  # Wartość True dla pomiaru czasu

	dealer = SecretShare(secretInput=SECRET, shareNum=3, prog=3, quiet=True)
	print('\nPodzial Sekretu')		
	print(f"Sekret: {int.from_bytes(SECRET, byteorder='big')}")	
	T = [dealer.run()]  # Pomiar Czasu szyfracji dealera
	
	# s1 = str(S[0]).encode()  # konwersja cyfr w str na byte
	S = dealer.createShares()  # Stworzenie udzialow
	s1 = (S[0]).to_bytes(size, byteorder='big')
	s2 = (S[1]).to_bytes(size, byteorder='big')
	s3 = (S[2]).to_bytes(size, byteorder='big')

	# Definiowanie regionów
	region1 = SecretShare(secretInput=s1, shareNum=6, prog=3, quiet=QUIET)
	region2 = SecretShare(secretInput=s2, shareNum=4, prog=3, quiet=QUIET)
	region3 = SecretShare(secretInput=s3, shareNum=10, prog=6, quiet=QUIET)

	# Pomiar czasu 
	print('\nRegion 1')
	print(f"Sekret:\n{S[0]}")
	T += [region1.run()]

	# Pomiar czasu 
	print('\nRegion 2')
	print(f"Sekret:\n{S[1]}")
	T += [region2.run()]

	# Pomiar czasu 
	print('\nRegion 3')
	print(f"Sekret:\n{S[2]}")
	T += [region3.run()]
	
	# Suma 
	print(f"\nSum of times: {np.sum(T)} ms")

	# Rekonstrukcja 
	m1 = region1.reconstruct(region1.shares)
	m2 = region2.reconstruct(region2.shares)
	m3 = region3.reconstruct(region3.shares)
	M = dealer.reconstruct([m1, m2, m3])	

	print(f"\nOdzyskany sekret z cieni regionów:\n{M}")  # Odszyfrowana wiadomosc jest dziesietna
	if dealer.M == M:
		print('Deszyfracja prawidlowa.')
	else:
		print('Deszyfracja nieudana.')
	# Print w bytach
	# print(f"W Byte:\n{M.to_bytes(size, byteorder='big')}")
	# print(f" Sekret przed podzialem:\n{SECRET}")
	
	input('\nEnd....')
