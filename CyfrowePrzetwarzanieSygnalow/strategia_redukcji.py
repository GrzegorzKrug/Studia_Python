import numpy as np
from copy import copy, deepcopy
from sympy import Matrix, zeros, ones, eye, diag
from itertools import permutations

class ListArray:
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

        return ListArray(out)

    def __repr__(self):
        # self.__name__
        txt = '['
        for row in range(self.size[0]):
            if row == 0:
                txt += f"{'[':>1}"
            else:
                txt += f'\n{"[":>3}'

            for col in range(self.size[1]):
                txt += f' {self.array[self.size[1]*row +col]},'

            if row >= self.size[0] - 1:
                txt += ']'
            else:
                txt += f'],'
        txt += f']'
        # return str(self.array)
        return txt

    def __sub__(self, other):
        return ListArray([[
            self.array[r * self.size[1] + c] - other.array[r * self.size[1] + c]
            for c in range(self.size[1])
        ]
            for r in range(self.size[0])
        ])

    def __add__(self, other):
        return ListArray([[
            self.array[r * self.size[1] + c] + other.array[r * self.size[1] + c]
            for c in range(self.size[1])
        ]
            for r in range(self.size[0])
        ])

    def __mul__(self, other):
        pass
        # return ['mnożenie' for row in 

    def __eq__(self, other):
        return self.array == other.array

    def transp(self):
        return ListArray(self.array.T)
        
    def fit(self):
        if self.size[0] % 2 == 1 or self.size[1] % 2 == 1:
            raise ValueError("Matrix has to be even size!")

        # A | B
        # --|--
        # C | D 
        half_rows = int(self.size[0]/2)  
        half_cols = int(self.size[1]/2)  

        square_a = self[0:half_rows, 0:half_cols]
        square_b = self[0:half_rows, half_cols:self.size[1]]
        square_c = self[half_rows:self.size[0], 0:half_cols]
        square_d = self[half_rows:self.size[0], half_cols:self.size[1]]
        print("Matrix:\n", self)
        print('square a:\n', square_a)
        print('square b:\n', square_b)
        print('square c:\n', square_c)
        print('square d:\n', square_d)
        a = copy(square_a)
        square_b.size=(3,3)
        print("A == A:", square_a == square_a)
        print("A == B:", square_a == square_b)

if __name__ == "__main__":
    a = [['a', 'b', 'c', 'g'],
         ['d', 'e', 'f', 'x'],
         ['q', 't', 'i', 'y'],
         ['i', 'o', 'p', 's']]

    b = [['d', 'e', 'f'], ['g', 'h', 'i']]
    c = ['x', 'y', 'z']
    d = [['i', 'b', 'cd']]

    A = ListArray(a)
    B = ListArray(b)
    C = ListArray(c)
    D = ListArray(d)

    # print(f"A =\n{A}")



    # A = A[0:2, 0:2]
    # A3 = A[2:4, 2:5]

    t = Matrix(['a', 'b'])
    # print(t*t.T)

    print(A.fit())


