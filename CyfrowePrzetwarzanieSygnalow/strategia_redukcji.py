import numpy as np
from copy import copy, deepcopy
from sympy import Matrix, zeros, ones, eye, diag
from itertools import permutations


class ListArray:
    def __init__(self, array):
        if type(array) == int:
            array = [array]

        if type(array[0]) != list:
            self.single = True
            self.size = (1, len(array))
            array = [array]  # Matrix always uses 2d !
        else:
            self.single = False
            self.size = (len(array), len(array[0]))

        for row in array:
            if type(row[0]) == list:
                print('To deep Array:', array)
                break

        self.array = Matrix(array)
        self.history = [{'created': array}]

    def __getitem__(self, i):
        # Condition to extract row!
        if type(i) is slice:
            rstart = i.start if i.start else 0
            rstop = i.stop if i.stop else self.size[0]
            rstep = i.step if i.step else 1

            cstart = 0
            cstop = self.size[1]
            cstep = 1

        # Condition to Slice with number -> one Row
        elif type(i) is int:
            rstart = i
            rstop = i + 1
            rstep = 1

            cstart = 0
            cstop = self.size[1]
            cstep = 1

        # Condition Double slice
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
            raise ValueError(f"Incorrect Slice params: {i}")

        array = self.array
        if self.single:
            # array = array]
            out = [
                array[r * self.size[1] + c]
                for c in range(cstart, cstop, cstep)

                for r in range(rstart, rstop, rstep)
            ]
        else:
            out = [[
                array[r * self.size[1] + c]
                for c in range(cstart, cstop, cstep)
            ]
                for r in range(rstart, rstop, rstep)
            ]

        return ListArray(out)

    def __repr__(self):
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
        return txt

    def __sub__(self, other):
        return ListArray([[
            self.array[r * self.size[1] + c] -
            other.array[r * self.size[1] + c]
            for c in range(self.size[1])
        ]
            for r in range(self.size[0])
        ])

    def __add__(self, other):
        return ListArray([[
            self.array[r * self.size[1] + c] +
            other.array[r * self.size[1] + c]
            for c in range(self.size[1])
        ]
            for r in range(self.size[0])
        ])

    def __mul__(self, other):
        result = self.array * other.array
        result = [result[other.size[1]*row: other.size[1]*row + other.size[1]]
                  for row in range(self.size[0])
                  ]
        return ListArray(result)

    def __eq__(self, other):
        return self.array == other.array

    def switch_Rows(self):
        print("Finish this")

    def switch_cols(self):
        print("Finish this")

    def transp(self):
        c = self.size[0]
        r = self.size[1]
        array_t = self.array.T
        return ListArray([array_t[row*c:row*c + c] for row in range(r)])

    def fit(self):
        # A | B
        # --|--
        # C | D
        if self.size[0] % 2 == 1 or self.size[1] % 2 == 1:
            raise ValueError("Matrix has to be even size!")

        half_rows = int(self.size[0]/2)
        half_cols = int(self.size[1]/2)

        square_a = self[0:half_rows, 0:half_cols]
        square_b = self[0:half_rows, half_cols:self.size[1]]
        square_c = self[half_rows:self.size[0], 0:half_cols]
        square_d = self[half_rows:self.size[0], half_cols:self.size[1]]

        return any([
            square_a == square_b,
            square_a == square_c,
            square_a == square_d,
            square_b == square_c,
            square_b == square_d,
            square_c == square_d
        ])


if __name__ == "__main__":
    a = [['a', 'b', 'c', 'g'],
         ['d', 'e', 'f', 'x'],
         ['q', 't', 'i', 'y'],
         ['i', 'o', 'p', 's']]

    b = [['d', 'e', 'f'], ['g', 'h', 'i']]
    c = ['x', 'y', 'z']
    d = [['i', 'b', 'c', 'd']]

    A = ListArray(a)
    B = ListArray(b)
    C = ListArray(c)
    D = ListArray(d)
    print(A[0])
    print(C[0])
    print(D[0])
