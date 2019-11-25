import numpy as np
from sympy import Matrix, zeros, ones, eye, diag

class listArray:
	def __init__(self, array):
		if type(array) == int:
			array = [[array]]
		elif type(array[0]) != int:
			array = [array]
		
		self.array = Matrix(array)
		self.size = (len(array), len(array[0]))

	def __repr__(self):
		#self.__name__
		txt = '['
		for i in range(self.size[0]):
			if i == 0:
				txt += '['
			else:
				txt += '\n['
			for j in range(self.size[1]):
				txt +=  f' {self.size[0]*i +j}'
			if i == self.size[1]-1:
				txt += ']'
			else:
				txt +=  f'],'
		txt +=  f']'
		return txt				


	def __subs__(self):
		pass
			
# 			for col in row:
# 				txt +=  f' {col}'
# 			if i == len(self.elements)-1:
# 				txt += ']'
# 			else:
# 				txt +=  f'],'
# 		txt +=  f']'
# 		return txt

# 	def __len__(self):
# 		return (len(self.elements) * len(self.elements[0]))


# 	def __add__(self, other):
# 		out = []

# 		if self.size == other.size:
# 			return True
# 		return None


a = [['a','b', 'c'],
	['d', 'e', 'f'],
	['g', 'h', 'i']]

A = listArray(a)
print(A)
#print(A[1,2])
print(A*A-A)
# for row in spA:
	# print(row)

# print(spA.det())
#print(spA[3, 3])



