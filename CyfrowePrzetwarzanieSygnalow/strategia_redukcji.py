import numpy as np
from sympy import Matrix, zeros, ones, eye, diag


class listArray:
    def __init__(self, array):
        # if array is None or array == []:
        #     pass
        if type(array) == int:
            array = [[array]]
        elif type(array[0]) != list:
            array = [array]

        self.array = Matrix(array)
        self.size = (len(array), len(array[0]))

    def __getitem__(self, i):
        # if type(i) is int:
        # 1 Slice Extracting rows!
        if type(i) is slice:
            rstart = i.start if i.start else 0
            rstop = i.stop if i.stop else self.size[0]
            rstep = i.step if i.step else 1

            cstart = 0
            cstop = self.size[1]
            cstep = 1

        # Slice with number -> one Row
        elif type(i) is int:
            rstart = i
            rstop = i + 1
            rstep = 1

            cstart = 0
            cstop = self.size[1]
            cstep = 1

        # Double slice -> 
        elif type(i[0]) is slice and type(i[1]) is slice:
            rslice = i[0]
            cslice = i[1]

            rstart = rslice.start if rslice.start else 0
            rstop = rslice.stop if rslice.stop else self.size[0]
            rstep = rslice.step if rslice.step else 1

            cstart = cslice.start if cslice.start else 0
            cstop = cslice.stop if cslice.stop else self.size[1]
            cstep = cslice.step if cslice.step else 1
        else:
            raise ValueError("Incorrect Slice with list Array")

        out = [[
            self.array[r * self.size[1] + c]
            for c in range(cstart, cstop, cstep)
        ]
            for r in range(rstart, rstop, rstep)
        ]
       
        return listArray(out)

    def __repr__(self):
        # self.__name__
        txt = '['
        for row in range(self.size[0]):
            if row == 0:
                txt += f"{'[':>1}"
            else:
                txt += f'\n{"[":>2}'

            for col in range(self.size[1]):
                txt += f' {self.array[self.size[1]*row +col]}'

            if row >= self.size[0] - 1:
                txt += ']'
            else:
                txt += f'],'
        txt += f']'
        # return str(self.array)
        return txt

    def __sub__(self, other):
        return listArray(self.array - other.array)

    def __add__(self, other):
        return listArray(self.array + other.array)


a = [['a', 'b', 'c', 'g', 'h'],
     ['d', 'e', 'f', 'x', 'u'],
     ['q', 't', 'i', 'a', 'h'],
     ['i', 'o', 'p', 's', 'r']]

b = [['d', 'e', 'f'], ['g', 'h', 'i']]
c = ['x', 'y', 'z']
d = [['i', 'b', 'cd']]

A = listArray(a)
B = listArray(b)
C = listArray(c)
D = listArray(d)

print(f"A =\n{A}")
# print(f"B =\n{B}")
# print(f"C =\n{C}")
# print(f"D =\n{D}")

A2 = A[0:2, 0:3]
A3 = A[2:4, 2:5]


print(A2)
print(A3)

print(A2 + A3)
