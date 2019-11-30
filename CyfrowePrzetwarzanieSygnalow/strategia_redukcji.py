import numpy as np
from sympy import Matrix, zeros, ones, eye, diag

class listArray:
	def __init__(self, array):
		if type(array) == int:
			array = [[array]]
		elif type(array[0]) == int:
			array = [array]
		
		self.array = Matrix(array)
		print("Starting", array)
		# if type(array) == Zero:
		# 	self.size = (0, 0)
		# else:
		self.size = (len(array), len(array[0]))
		
	def __getitem__(self, i):
		if type(i) == slice:
			pass
		else:
			slic1 = i[0]
			slic2 = i[1]
		print(f"Type {type(i)}")
		return None

	def __repr__(self):
		#self.__name__
		txt = '['
		for i in range(self.size[0]):
			if i == 0:
				txt += f"{'[':>2}"
			else:
				txt += f'\n{"[":>3}'
			for j in range(self.size[1]):
				txt +=  f' {self.array[self.size[0]*i +j]}'				
			if i == self.size[1] - 1:
				txt += ']'
			else:
				txt +=  f'],'
		txt +=  f']'
		# return str(self.array)
		return txt				


	def __sub__(self, other):
		return listArray(self.array - other.array)

	def __add__(self, other):
		return listArray(self.array + other.array)
			


a = [['a','b', 'c'],
	['d', 'e', 'f'],
	['g', 'h', 'i']]

A = listArray(a)
print(A)
print(A[:,1:2])

# print(A - A)
# print(A + A)

